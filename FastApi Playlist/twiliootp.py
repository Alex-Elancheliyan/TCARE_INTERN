
import os
from twilio.rest import Client

account_sid = "AC48b4e4618e9a1566e20564f3ae96ba5f"
auth_token = "c0a5ecc8278b623ab91220efd28cd4b5"
verify_sid = "VAb0b0346703060ebbb0f6a0210bcf3ce2"
verified_number = "+919043372484"

client = Client(account_sid, auth_token)

verification = client.verify.v2.services(verify_sid) \
  .verifications \
  .create(to=verified_number, channel="sms")
print(verification.status)

otp_code = input("Please enter the OTP:")

verification_check = client.verify.v2.services(verify_sid) \
  .verification_checks \
  .create(to=verified_number, code=otp_code)
print(verification_check.status)


