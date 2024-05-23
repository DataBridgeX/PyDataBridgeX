import requests
from pydatabridge.pydatabridge import Configuration


class Authentication(FirebaseBase):
    def __init__(self, config: Configuration):
        super().__init__(config)

    def create_user(self, user_data):
        return self._send_request("POST", "", data={"userData": user_data})

    def send_verification_email(self, email):
        return self._send_request("GET", "verification/email", params={"email": email})

    def login_user(self, email, password):
        return self._send_request(
            "GET", "login", params={"email": email, "password": password}
        )

    def update_user(self, uid, user_data):
        return self._send_request("PUT", "", data={"uid": uid, "userData": user_data})

    def get_user(self, uid):
        return self._send_request("GET", "", params={"uid": uid})

    def delete_user(self, uid):
        return self._send_request("DELETE", "", data={"uid": uid})

    def create_phone_verification(self, phone_number):
        return self._send_request("POST", "phone", data={"phoneNumber": phone_number})

    def verify_phone_verification(self, verification_id, otp):
        return self._send_request(
            "GET", "phone", params={"verificationId": verification_id, "otp": otp}
        )

    def reset_password(self, email):
        return self._send_request("GET", "reset/password", params={"email": email})
