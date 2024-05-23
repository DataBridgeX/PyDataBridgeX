import requests
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

    def __init__(self, config: Configuration):
        """
        Initializes the RealTime instance.

        Args:
            config (Configuration): The Firebase configuration.
        """
        super().__init__(config)

    def create_item(self, data):
        """
        Creates a new item.

        Args:
            data (dict): The data to be stored.

        Returns:
            dict: The response data from the server.
        """
        return self._send_request("POST", "create", data={"data": data})

    def read_items(self, req):
        """
        Reads items.

        Args:
            req (dict): The request parameters.

        Returns:
            dict: The response data from the server.
        """
        return self._send_request("GET", "read", params=req)

    def update_item(self, id, new_data):
        """
        Updates an item.

        Args:
            id (str): The ID of the item to update.
            new_data (dict): The updated data.

        Returns:
            dict: The response data from the server.
        """
        return self._send_request("PUT", "update", data={"id": id, "newData": new_data})

    def delete_item(self, id):
        """
        Deletes an item.

        Args:
            id (str): The ID of the item to delete.

        Returns:
            dict: The response data from the server.
        """
        return self._send_request("DELETE", "delete", data={"id": id})
