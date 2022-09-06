from flask import Flask
import os
from flask_wtf.csrf import CSRFProtect

if __name__ == '__main__':
    app.run()

app = Flask(__name__)

csrf = CSRFProtect(app)

@app.route("/")
def pagina_inicial():
    return """<!DOCTYPE html>
<html>
<body>
<h2 style="text-align:center;">Toddy World - Docker.</h2>
<img style="margin: 0% 25%;" src="https://i.imgur.com/XZJuWmA.jpeg" width="50%" height="500px"></img>
<p><span style="font-size: 40px;">D</span>oggo ipsum floofs noodle horse clouds fluffer puggo borkf, such treat you are doing me the shock maximum borkdrive the neighborhood pupper. Porgo yapper shooberino heck you are doing me a frighten extremely cuuuuuute, borkf doing me a frighten borkf mlem. You are doing me the shock ur givin me a spook porgo pupperino heckin angery woofer corgo long woofer, maximum borkdrive yapper noodle horse adorable doggo what a nice floof. Very taste wow stop it fren doggorino heckin angery woofer vvv floofs much ruin diet, very taste wow long woofer smol borking doggo with a long snoot for pats corgo thicc. Doggo big ol pupper you are doing me the shock bork porgo super chub, floofs doggorino extremely cuuuuuute big ol.</p>
</body>
</html>
"""



if __name__ == '__main__':
    port = os.getenv('PORT')
    app.run('0.0.0.0', port=port)