from flask import Flask
import os   

app = Flask(__name__)

@approute('/')
def home():
    return {
        "status": "online",
        "marca" : "GuIIoTiT",
        "mensagem" : "Hospedado com sucesso"
    }
if __name__ == '__main__':
    # Garante que o app use a porta do servidor (Render) ou a 5000 localmente
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
    