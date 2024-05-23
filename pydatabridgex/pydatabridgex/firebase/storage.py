from pydatabridge.pydatabridge import *
import requests


class Storage(FirebaseBase):
    def __init__(self, config: Configuration):
        super().__init__(config)

    def upload_byte8_array(self, path, image_base64):
        data = {"path": path, "imageBase64": image_base64}
        return self._send_request("POST", "uploadByte8Array", data=data)

    def upload_file(self, file_path, path):
        files = {"file": open(file_path, "rb")}
        data = {"path": path}
        return self._send_request("POST", "uploadFile", data=data, files=files)

    def get_download_url(self, path):
        data = {"path": path}
        return self._send_request("POST", "getDownloadURL", data=data)

    def delete_file(self, path):
        data = {"path": path}
        return self._send_request("DELETE", "deleteFile", data=data)
