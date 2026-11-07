class EmailNotification:
    def send(self, message):
        print("Email Sent:", message)


class SMSNotification:
    def send(self, message):
        print("SMS Sent:", message)


class PushNotification:
    def send(self, message):
        print("Push Notification:", message)


# Common function
def send_notification(notification, message):
    notification.send(message)


# Creating objects
email = EmailNotification()
sms = SMSNotification()
push = PushNotification()

# Calling the same function
send_notification(email, "Your order is confirmed.")
send_notification(sms, "Your order is confirmed.")
send_notification(push, "Your order is confirmed.")