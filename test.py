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
<h2 style="text-align:center;">Toddy World - Docker.</h2>
<img style="margin: 0% 25%;" src="https://i.imgur.com/XZJuWmA.jpeg" width="50%"></img>
<p><span style="font-size: 40px;">D</span>oggo ipsum floofs noodle horse clouds fluffer puggo borkf, such treat you are doing me the shock maximum borkdrive the neighborhood pupper. Porgo yapper shooberino heck you are doing me a frighten extremely cuuuuuute, borkf doing me a frighten borkf mlem. You are doing me the shock ur givin me a spook porgo pupperino heckin angery woofer corgo long woofer, maximum borkdrive yapper noodle horse adorable doggo what a nice floof. Very taste wow stop it fren doggorino heckin angery woofer vvv floofs much ruin diet, very taste wow long woofer smol borking doggo with a long snoot for pats corgo thicc. Doggo big ol pupper you are doing me the shock bork porgo super chub, floofs doggorino extremely cuuuuuute big ol.</p>
</body>
</html>
""")