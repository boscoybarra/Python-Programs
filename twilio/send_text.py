from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ENTER-YOUR-ACCOUNT-SID"
# Your Auth Token from twilio.com/console
auth_token  = "ENTER-YOUR-AUTH-TOKEN"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="ENTER-PHONE",
    from_="ENTER-PHONE-REGISTERED-ON-TWILIO",
    body="Hello, simply type in here the code you want to send out!. Twilio does not allow emojis. Too bad!")

print(message.sid)
