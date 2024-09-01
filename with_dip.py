# With DIP

from abc import ABC, abstractmethod

class MessageService(ABC):
    @abstractmethod
    def send_message(self, message):
        pass

class EmailService(MessageService):
    def send_message(self, message):
        print(f"Sending email: {message}")

class SMSService(MessageService):
    def send_message(self, message):
        print(f"Sending SMS: {message}")

class Notification:
    def __init__(self, message_service: MessageService):
        self.message_service = message_service  # Dependency injection

    def send(self, message):
        self.message_service.send_message(message)

# Main code
email_service = EmailService()
notification_email = Notification(email_service)
notification_email.send("Hello World!")

sms_service = SMSService()
notification_sms = Notification(sms_service)
notification_sms.send("Hello World!")
