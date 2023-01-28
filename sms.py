import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()


def SendSMS(messageText: str):
    try:
        token = os.getenv("TWILIO_AUTH_TOKEN")
        account_sid = "ACb36d95fa5cfa3cbbdec26df81bd2526e"
        auth_token = token
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            body=f"{messageText}",
            from_="+16088796253",
            to="+16475635190"
        )
    except:
        print("Failing sending the message")
