# -*- coding: utf-8 -*-
from app import app
import unittest

class Test(unittest.TestCase):
    def setUp(self):
        # cria uma instância do unittest, precisa do nome "setUp"
        self.app = app.test_client()

        # envia uma requisicao GET para a URL
        self.result = self.app.get('/')

    def test_requisicao(self):
        # compara o status da requisicao (precisa ser igual a 200)
        self.assertEqual(self.result.status_code, 200)

    def test_conteudo(self):
        # verifica o retorno do conteudo da pagina
        self.assertEqual(self.result.data.decode('utf-8'), """<!DOCTYPE html>
<html>
<body>
<h2>Hello World</h2>
<blockquote class="imgur-embed-pub" lang="en" data-id="a/ETkM7Gm" data-context="false" ><a href="//imgur.com/a/ETkM7Gm"></a></blockquote><script async src="//s.imgur.com/min/embed.js" charset="utf-8"></script>
</body>
</html>
""")