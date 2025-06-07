from flask import Blueprint, request
from twilio.twiml.messaging_response import MessagingResponse
from chatnet import chatnet

whatsapp_bp = Blueprint("whatsapp", __name__)

@whatsapp_bp.route("/whatsapp", methods=["POST"])
def responder_whatsapp():
    msg_recebida = request.form.get("Body")
    print(f"Mensagem recebida: {msg_recebida}")

    resposta = chatnet(msg_recebida)
    print(f"Resposta gerada: {resposta}")

    twilio_resp = MessagingResponse()
    twilio_resp.message(resposta)
    return str(twilio_resp)
