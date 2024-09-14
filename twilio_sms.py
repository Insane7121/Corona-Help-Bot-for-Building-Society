from twilio.rest import Client


# Function to send an SMS using Twilio
def sendSMS(body, recipient_number):
    account_sid = 'your_account_sid'
    auth_token = 'your_auth_token'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=body,
        from_='+1234567890',  # Your Twilio number
        to=recipient_number
    )

    print(f"SMS sent to {recipient_number}")

if __name__ == "__main__":
    body = "Stay safe! Wear a mask and maintain social distancing."
    recipient_number = '+919876543210'  # Replace with the recipient's phone number
    sendSMS(body, recipient_number)
