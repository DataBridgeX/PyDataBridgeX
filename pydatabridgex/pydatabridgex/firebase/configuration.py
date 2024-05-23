import json
from typing import Union


class Configuration:
    """
    Represents the configuration for Firebase.

    Args:
        firebase_config (dict): The Firebase configuration.
        service_account (Union[str, dict]): The service account credentials.
        database_url (str): The URL of the Firebase database.
        storage_bucket (str): The name of the Firebase storage bucket.
        base_url (str, optional): The base URL for requests. Defaults to "https://fir-connect-ea9c9.uc.r.appspot.com".

    Attributes:
        firebase_config (dict): The Firebase configuration.
        service_account (dict): The service account credentials.
        database_url (str): The URL of the Firebase database.
        storage_bucket (str): The name of the Firebase storage bucket.
        base_url (str): The base URL for requests.

    Methods:
        produce_headers(): Generates the headers for requests.
    """

    def __init__(
        self,
        firebase_config: dict,
        service_account: Union[str, dict],
        database_url: str,
        storage_bucket: str,
        base_url: str = "https://fir-connect-ea9c9.uc.r.appspot.com",
    ):
        """
        Initializes the Configuration object.

        Args:
            firebase_config (dict): The Firebase configuration.
            service_account (Union[str, dict]): The service account credentials.
            database_url (str): The URL of the Firebase database.
            storage_bucket (str): The name of the Firebase storage bucket.
            base_url (str, optional): The base URL for requests. Defaults to "https://fir-connect-ea9c9.uc.r.appspot.com".
        """
        self.firebase_config = firebase_config
        self.service_account = (
            json.load(open(service_account))
            if isinstance(service_account, str)
            else service_account
        )
        self.database_url = database_url
        self.storage_bucket = storage_bucket
        self.base_url = base_url

    def produce_headers(self):
        """
        Generates headers for requests.

        Returns:
            dict: The headers for requests.
        """
        return {
            "firebaseconfig": json.dumps(self.firebase_config),
            "serviceaccount": json.dumps(self.service_account),
            "databaseurl": self.database_url,
            "storagebucket": self.storage_bucket,
        }

    def __repr__(self):
        return (
            f"Configuration(firebase_config={self.firebase_config}, "
            f"service_account={self.service_account}, "
            f"database_url={self.database_url}, "
            f"storage_bucket={self.storage_bucket})"
        )

    def __str__(self):
        return json.dumps(self.produce_headers(), indent=4)

    def __eq__(self, other):
        if isinstance(other, Configuration):
            return (
                self.firebase_config == other.firebase_config
                and self.service_account == other.service_account
                and self.database_url == other.database_url
                and self.storage_bucket == other.storage_bucket
            )
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(
            (
                json.dumps(self.firebase_config),
                json.dumps(self.service_account),
                self.database_url,
                self.storage_bucket,
            )
        )

    def __len__(self):
        return 4

    def __getitem__(self, key):
        if key == "firebase_config":
            return self.firebase_config
        elif key == "service_account":
            return self.service_account
        elif key == "database_url":
            return self.database_url
        elif key == "storage_bucket":
            return self.storage_bucket
        else:
            raise KeyError(key)

    def __setitem__(self, key, value):
        if key == "firebase_config":
            self.firebase_config = value
        elif key == "service_account":
            self.service_account = value
        elif key == "database_url":
            self.database_url = value
        elif key == "storage_bucket":
            self.storage_bucket = value
        else:
            raise KeyError(key)

    def __call__(self):
        return self.produce_headers()

    def __iter__(self):
        yield "firebase_config", self.firebase_config
        yield "service_account", self.service_account
        yield "database_url", self.database_url
        yield "storage_bucket", self.storage_bucket
