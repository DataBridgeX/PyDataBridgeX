import requests
from pydatabridge.pydatabridge import Configuration


class Firestore(FirebaseBase):
    """
    Represents a Firestore instance for performing CRUD operations.

    Args:
        config (Configuration): The Firebase configuration.

    Attributes:
        config (Configuration): The Firebase configuration.

    Methods:
        create_document(data): Creates a new document.
        read_document(req): Reads a document.
        update_document(data): Updates a document.
        delete_document(req): Deletes a document.
        read_paths(req): Reads paths.
        read_all_documents(req): Reads all documents.
    """

    def __init__(self, config: Configuration):
        """
        Initializes the Firestore instance.

        Args:
            config (Configuration): The Firebase configuration.
        """
        super().__init__(config)

    def create_document(self, data):
        """
        Creates a new document.

        Args:
            data (dict): The data to be stored.

        Returns:
            dict: The response data from the server.
        """
        return self._send_request("POST", "", data={"data": data})

    def read_document(self, req):
        """
        Reads a document.

        Args:
            req (dict): The request parameters.

        Returns:
            dict: The response data from the server.
        """
        return self._send_request("GET", "", params=req)

    def update_document(self, data):
        """
        Updates a document.

        Args:
            data (dict): The updated data.

        Returns:
            dict: The response data from the server.
        """
        return self._send_request("PUT", "", data={"data": data})

    def delete_document(self, req):
        """
        Deletes a document.

        Args:
            req (dict): The request parameters.

        Returns:
            dict: The response data from the server.
        """
        return self._send_request("DELETE", "", params=req)

    def read_paths(self, req):
        """
        Reads paths.

        Args:
            req (dict): The request parameters.

        Returns:
            dict: The response data from the server.
        """
        return self._send_request("GET", "paths", params=req)

    def read_all_documents(self, req):
        """
        Reads all documents.

        Args:
            req (dict): The request parameters.

        Returns:
            dict: The response data from the server.
        """
        return self._send_request("GET", "all", params=req)
