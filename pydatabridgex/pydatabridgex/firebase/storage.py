from pydatabridge.pydatabridge import Configuration
from typing import Dict, Any
import requests


class Storage(FirebaseBase):
    """
    Represents a Storage instance for performing file operations.

    Args:
        config (Configuration): The Firebase configuration.

    Attributes:
        config (Configuration): The Firebase configuration.

    Methods:
        upload_byte8_array(path, image_base64): Uploads a base64-encoded image.
        upload_file(file_path, path): Uploads a file.
        get_download_url(path): Retrieves the download URL of a file.
        delete_file(path): Deletes a file.
    """

    def __init__(self, config: Configuration) -> None:
        """
        Initializes the Storage instance.

        Args:
            config (Configuration): The Firebase configuration.
        """
        super().__init__(config)

    def __repr__(self) -> str:
        """
        Return a string representation of the object.
        """
        return f"Storage(config={self.config})"

    def __str__(self) -> str:
        """
        Return a string representation of the object.
        """
        return f"Storage: Config={self.config}"

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

    def upload_byte8_array(self, path: str, image_base64: str) -> Dict[str, Any]:
        """
        Uploads a base64-encoded image to Firebase Storage.

        Args:
            path (str): The path to store the image.
            image_base64 (str): The base64-encoded image data.

        Returns:
            dict: The response data from the server.
        """
        data = {"path": path, "imageBase64": image_base64}
        return self._send_request("POST", "uploadByte8Array", data=data)

    def upload_file(self, file_path: str, path: str) -> Dict[str, Any]:
        """
        Uploads a file to Firebase Storage.

        Args:
            file_path (str): The path of the file to upload.
            path (str): The path to store the file.

        Returns:
            dict: The response data from the server.
        """
        files = {"file": open(file_path, "rb")}
        data = {"path": path}
        return self._send_request("POST", "uploadFile", data=data, files=files)

    def get_download_url(self, path: str) -> Dict[str, Any]:
        """
        Retrieves the download URL of a file from Firebase Storage.

        Args:
            path (str): The path of the file.

        Returns:
            dict: The response data from the server.
        """
        data = {"path": path}
        return self._send_request("POST", "getDownloadURL", data=data)

    def delete_file(self, path: str) -> Dict[str, Any]:
        """
        Deletes a file from Firebase Storage.

        Args:
            path (str): The path of the file to delete.

        Returns:
            dict: The response data from the server.
        """
        data = {"path": path}
        return self._send_request("DELETE", "deleteFile", data=data)
