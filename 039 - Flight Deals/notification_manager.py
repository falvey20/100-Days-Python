from twilio.rest import Client

TWILIO_SID = ""  # TwilioTrial
TWILIO_AUTH_TOKEN = ""  # TwilioTrial
TWILIO_VIRTUAL_NUMBER = '' # Twilio Number
TWILIO_VERIFIED_NUMBER = '' # Test Number


class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages \
            .create(body=message,
                    from_=TWILIO_VIRTUAL_NUMBER,  # TwilioNo.
                    to=TWILIO_VERIFIED_NUMBER  # TestNo.
        )

        print(message.status)