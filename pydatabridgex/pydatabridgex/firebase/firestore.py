import requests
from typing import Dict, Any
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

    def __init__(self, config: Configuration) -> None:
        """
        Initializes the Firestore instance.

        Args:
            config (Configuration): The Firebase configuration.
        """
        super().__init__(config)

    def __repr__(self) -> str:
        """
        Return a string representation of the object.
        """
        return f"Firestore(config={self.config})"

    def __str__(self) -> str:
        """
        Return a string representation of the object.
        """
        return f"Firestore: Config={self.config}"

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

    def create_document(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Creates a new document.

        Args:
            data (Dict[str, Any]): The data to be stored.

        Returns:
            Dict[str, Any]: The response data from the server.
        """
        return self._send_request("POST", "", data={"data": data})

    def read_document(self, req: Dict[str, Any]) -> Dict[str, Any]:
        """
        Reads a document.

        Args:
            req (Dict[str, Any]): The request parameters.

        Returns:
            Dict[str, Any]: The response data from the server.
        """
        return self._send_request("GET", "", params=req)

    def update_document(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Updates a document.

        Args:
            data (Dict[str, Any]): The updated data.

        Returns:
            Dict[str, Any]: The response data from the server.
        """
        return self._send_request("PUT", "", data={"data": data})

    def delete_document(self, req: Dict[str, Any]) -> Dict[str, Any]:
        """
        Deletes a document.

        Args:
            req (Dict[str, Any]): The request parameters.

        Returns:
            Dict[str, Any]: The response data from the server.
        """
        return self._send_request("DELETE", "", params=req)

    def read_paths(self, req: Dict[str, Any]) -> Dict[str, Any]:
        """
        Reads paths.

        Args:
            req (Dict[str, Any]): The request parameters.

        Returns:
            Dict[str, Any]: The response data from the server.
        """
        return self._send_request("GET", "paths", params=req)

    def read_all_documents(self, req: Dict[str, Any]) -> Dict[str, Any]:
        """
        Reads all documents.

        Args:
            req (Dict[str, Any]): The request parameters.

        Returns:
            Dict[str, Any]: The response data from the server.
        """
        return self._send_request("GET", "all", params=req)
