# Without DIP

class EmailService:
    def send_email(self, message):
        print(f"Sending email: {message}")

class Notification:
    def __init__(self):
        self.email_service = EmailService()  # Tight coupling

    def send(self, message):
        self.email_service.send_email(message)

# Main code
notification = Notification()
notification.send("Hello World!")
