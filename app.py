from flask import Flask
from chatnet import chatnet
from whatsapp_routes import whatsapp_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(whatsapp_bp)

    @app.route("/livechat")
    def func_chat():
        return "API de Atendimento EditaFlex está rodando."

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000, debug=True)
