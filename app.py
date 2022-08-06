from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return """<!DOCTYPE html>
<html>
<body>
<h2>Hello World</h2>
<blockquote class="imgur-embed-pub" lang="en" data-id="a/ETkM7Gm" data-context="false" ><a href="//imgur.com/a/ETkM7Gm"></a></blockquote><script async src="//s.imgur.com/min/embed.js" charset="utf-8"></script>
</body>
</html>
"""

if __name__ == '__main__':
    app.run()