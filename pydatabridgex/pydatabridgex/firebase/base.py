from typing import Dict, Any
from pydatabridge.pydatabridge import Configuration
import requests


class FirebaseBase:
    """
    Base class for Firebase operations.

    Args:
        config (Configuration): The Firebase configuration.
    """

    def __init__(self, config: Configuration) -> None:
        """
        Initializes the FirebaseBase class with the provided configuration.

        Args:
            config (Configuration): The Firebase configuration.
        """
        self.config = config
        self.headers = self.config.produce_headers()
        self.base_url = self.config.base_url

    def __repr__(self) -> str:
        """
        Return a string representation of the object.
        """
        return f"FirebaseBase(config={self.config})"

    def __str__(self) -> str:
        """
        Return a string representation of the object.
        """
        return f"FirebaseBase: Config={self.config}"

    def __len__(self) -> int:
        """
        Return the length of the object.
        """
        return len(self.config)

    def __getitem__(self, key: str) -> Any:
        """
        Get an item from the object.
        """
        return self.config[key]

    def _send_request(
        self,
        method: str,
        endpoint: str,
        data: Dict[str, Any] = None,
        params: Dict[str, Any] = None,
        files: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        """
        Sends a request to the Firebase API.

        Args:
            method (str): The HTTP method (GET, POST, PUT, DELETE).
            endpoint (str): The API endpoint.
            data (dict): The request body data (for POST, PUT, DELETE methods).
            params (dict): The request URL parameters.
            files (dict): The files to upload (for POST method).

        Returns:
            dict: The JSON response from the API.
        """
        url = f"{self.base_url}/{endpoint}"
        try:
            if method == "GET":
                response = requests.get(url, headers=self.headers, params=params)
            elif method == "POST":
                response = requests.post(
                    url, headers=self.headers, json=data, files=files
                )
            elif method == "PUT":
                response = requests.put(url, headers=self.headers, json=data)
            elif method == "DELETE":
                response = requests.delete(url, headers=self.headers, json=data)
            else:
                raise ValueError(f"Unsupported method: {method}")

            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}
