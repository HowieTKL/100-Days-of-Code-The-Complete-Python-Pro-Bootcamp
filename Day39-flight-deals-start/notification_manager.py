import os
from twilio.rest import Client

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        pass

    def send_notification(self, flight, city):
        account_sid = os.environ['TWILIO_SID']
        auth_token = os.environ['TWILIO_AUTH_TOKEN']
        client = Client(account_sid, auth_token)
        # whatsapp
        message = client.messages.create(
            from_='whatsapp:+14155238886',
            body=f"Cheap flight {flight['price']['grandTotal']} on {flight['lastTicketingDate']} to {city['city']}",
            to='whatsapp:+17033001497'
        )
