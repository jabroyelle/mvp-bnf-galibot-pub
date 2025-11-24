import smtplib
from email.message import EmailMessage
from ibm_watsonx_orchestrate.agent_builder.tools import tool, ToolPermission
from ibm_watsonx_orchestrate.agent_builder.connections.types import ExpectedCredentials
from ibm_watsonx_orchestrate.agent_builder.connections.connections import ConnectionType
from unified_connection_utils import get_mailjet_credentials

@tool(
    name="send_email_mailjet",
    description="Send an email using Mailjet SMTP with credentials from connection.",
    permission=ToolPermission.READ_WRITE,
    expected_credentials=[
        ExpectedCredentials(app_id="email_mailjet", type=ConnectionType.KEY_VALUE)
    ],
)
def send_email_mailjet(email_subject: str) -> str:
    creds = get_mailjet_credentials()

    msg = EmailMessage()
    msg["Subject"] = email_subject
    msg["From"] = creds["from_email"]
    msg["To"] = creds["to_email"]
    msg.set_content(
        "Ceci est un test envoyé via Mailjet SMTP depuis Python avec connexion sécurisée."
    )

    try:
        with smtplib.SMTP("in-v3.mailjet.com", 587) as smtp:
            smtp.starttls()
            smtp.login(creds["apikey"], creds["secretkey"])
            smtp.send_message(msg)
            return "✅ Email envoyé avec succès."
    except Exception as e:
        return f"❌ Erreur lors de l'envoi : {e}"
    
## TEST
if __name__ == "__main__":
    import datetime
    print(send_email_mailjet(f"Hello world-{datetime.date.today()}"))
