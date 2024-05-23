from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
from typing import List, Optional, Any
import warnings


class AzureStorage:
    """
    AzureStorage class for interacting with Azure Blob Storage.
    """

    def __init__(
        self,
        container_name: str,
        connection: str = "DefaultEndpointsProtocol=https;AccountName=[AccountNameAccountName];AccountKey=[AccountKey];EndpointSuffix=core.windows.net",
    ) -> None:
        """
        Initialize the AzureStorage object.

        Parameters:
            container_name (str): The name of the container in Azure Blob Storage.
            connection (str, optional): The connection string for the Azure Storage account. Defaults to the provided connection string.
        """
        self.connection_str = connection
        self.blob_service_client = BlobServiceClient.from_connection_string(
            conn_str=self.connection_str
        )
        self.container_name = str(container_name)
        try:
            self.container_client = self.blob_service_client.create_container(
                self.container_name
            )
        except:
            warnings.warn("Container already exists")

    def __repr__(self) -> str:
        """
        Return a string representation of the object.
        """
        return f"AzureStorage(container_name={self.container_name})"

    def __str__(self) -> str:
        """
        Return a string representation of the object.
        """
        return f"AzureStorage: Container '{self.container_name}'"

    def __len__(self) -> int:
        """
        Return the number of files in the container.
        """
        return len(self.find_file())

    def __getitem__(self, index: int) -> str:
        """
        Get the file name at the specified index in the container.
        """
        files = self.find_file()
        if 0 <= index < len(files):
            return files[index]
        else:
            raise IndexError("Index out of range")

    def __contains__(self, item: str) -> bool:
        """
        Check if a file with the given name exists in the container.
        """
        return item in self.find_file()

    def create_file(self, file_rb: Any, file_name_in_the_cloud: str) -> None:
        """
        Uploads a file to Azure Blob Storage.

        Parameters:
            file_rb (Any): The file to be uploaded.
            file_name_in_the_cloud (str): The name of the file in Azure Blob Storage.
        """
        blob_client = self.blob_service_client.get_blob_client(
            container=self.container_name, blob=file_name_in_the_cloud
        )
        blob_client.upload_blob(file_rb, overwrite=True)

    def find_file(self) -> List[str]:
        """
        Finds all files in the container.

        Returns:
            List[str]: A list of file names in the container.
        """
        blobs_list = self.container_client.list_blobs()
        files = []
        for blob in blobs_list:
            files.append(blob.name)
        return files

    def download_file(self, file_name_in_the_cloud: str) -> Optional[bytes]:
        """
        Downloads a file from Azure Blob Storage.

        Parameters:
            file_name_in_the_cloud (str): The name of the file in Azure Blob Storage.

        Returns:
            Optional[bytes]: The content of the downloaded file.
        """
        blob_client = self.blob_service_client.get_blob_client(
            container=self.container_name, blob=file_name_in_the_cloud
        )
        return blob_client.download_blob().readall()

    def delete_blob(self) -> None:
        """
        Deletes the container and all its contents.
        """
        self.container_client.delete_container()
