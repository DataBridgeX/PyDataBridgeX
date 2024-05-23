import requests
from pydatabridge.pydatabridge import Configuration


class Authentication(FirebaseBase):
    """
    Class for Firebase Authentication operations.

    Args:
        config (Configuration): The Firebase configuration.
    """

    def __init__(self, config: Configuration):
        """
        Initializes the Authentication class with the provided configuration.

        Args:
            config (Configuration): The Firebase configuration.
        """
        super().__init__(config)

    def create_user(self, user_data):
        """
        Creates a new user.

        Args:
            user_data (dict): The user data.

        Returns:
            dict: The response data.
        """
        return self._send_request("POST", "", data={"userData": user_data})

    def send_verification_email(self, email):
        """
        Sends a verification email to the specified email address.

        Args:
            email (str): The email address.

        Returns:
            dict: The response data.
        """
        return self._send_request("GET", "verification/email", params={"email": email})

    def login_user(self, email, password):
        """
        Logs in a user with the provided email and password.

        Args:
            email (str): The email address of the user.
            password (str): The password of the user.

        Returns:
            dict: The response data.
        """
        return self._send_request(
            "GET", "login", params={"email": email, "password": password}
        )

    def update_user(self, uid, user_data):
        """
        Updates a user's information.

        Args:
            uid (str): The user ID.
            user_data (dict): The updated user data.

        Returns:
            dict: The response data.
        """
        return self._send_request("PUT", "", data={"uid": uid, "userData": user_data})

    def get_user(self, uid):
        """
        Retrieves user information by ID.

        Args:
            uid (str): The user ID.

        Returns:
            dict: The response data.
        """
        return self._send_request("GET", "", params={"uid": uid})

    def delete_user(self, uid):
        """
        Deletes a user by ID.

        Args:
            uid (str): The user ID.

        Returns:
            dict: The response data.
        """
        return self._send_request("DELETE", "", data={"uid": uid})

    def create_phone_verification(self, phone_number):
        """
        Creates a phone verification request.

        Args:
            phone_number (str): The phone number.

        Returns:
            dict: The response data.
        """
        return self._send_request("POST", "phone", data={"phoneNumber": phone_number})

    def verify_phone_verification(self, verification_id, otp):
        """
        Verifies a phone verification request.

        Args:
            verification_id (str): The verification ID.
            otp (str): The one-time password.

        Returns:
            dict: The response data.
        """
        return self._send_request(
            "GET", "phone", params={"verificationId": verification_id, "otp": otp}
        )

    def reset_password(self, email):
        """
        Resets the password for a user.

        Args:
            email (str): The email address.

        Returns:
            dict: The response data.
        """
        return self._send_request("GET", "reset/password", params={"email": email})
