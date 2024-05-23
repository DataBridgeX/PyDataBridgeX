import requests
from typing import Dict, Any
from pydatabridge.pydatabridge import Configuration


class RealTime(FirebaseBase):
    """
    Represents a RealTime instance for performing CRUD operations.

    Args:
        config (Configuration): The Firebase configuration.

    Attributes:
        config (Configuration): The Firebase configuration.

    Methods:
        create_item(data): Creates a new item.
        read_items(req): Reads items.
        update_item(id, new_data): Updates an item.
        delete_item(id): Deletes an item.
    """

    def __init__(self, config: Configuration) -> None:
        """
        Initializes the RealTime instance.

        Args:
            config (Configuration): The Firebase configuration.
        """
        super().__init__(config)

    def __repr__(self) -> str:
        """
        Return a string representation of the object.
        """
        return f"RealTime(config={self.config})"

    def __str__(self) -> str:
        """
        Return a string representation of the object.
        """
        return f"RealTime: Config={self.config}"

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

    def create_item(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Creates a new item.

        Args:
            data (Dict[str, Any]): The data to be stored.

        Returns:
            Dict[str, Any]: The response data from the server.
        """
        return self._send_request("POST", "create", data={"data": data})

    def read_items(self, req: Dict[str, Any]) -> Dict[str, Any]:
        """
        Reads items.

        Args:
            req (Dict[str, Any]): The request parameters.

        Returns:
            Dict[str, Any]: The response data from the server.
        """
        return self._send_request("GET", "read", params=req)

    def update_item(self, id: str, new_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Updates an item.

        Args:
            id (str): The ID of the item to update.
            new_data (Dict[str, Any]): The updated data.

        Returns:
            Dict[str, Any]: The response data from the server.
        """
        return self._send_request("PUT", "update", data={"id": id, "newData": new_data})

    def delete_item(self, id: str) -> Dict[str, Any]:
        """
        Deletes an item.

        Args:
            id (str): The ID of the item to delete.

        Returns:
            Dict[str, Any]: The response data from the server.
        """
        return self._send_request("DELETE", "delete", data={"id": id})
