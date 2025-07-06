import json
from flask import Flask

app = Flask(__name__)

@app.route('/getmyinfo')
def getmyinfo():
    value = {
        "nombre": "Fernando Costa",
        "linkedin": "https://www.linkedin.com/in/fernando-costa-9bb982247",
        "mensaje": "Hola, esta es mi API en Flask dentro de Docker"
    }
    return json.dumps(value)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)