import requests
from pydatabridge.pydatabridge import Configuration


class Firestore(FirebaseBase):
    def __init__(self, config: Configuration):
        super().__init__(config)

    def create_document(self, data):
        return self._send_request("POST", "", data={"data": data})

    def read_document(self, req):
        return self._send_request("GET", "", params=req)

    def update_document(self, data):
        return self._send_request("PUT", "", data={"data": data})

    def delete_document(self, req):
        return self._send_request("DELETE", "", params=req)

    def read_paths(self, req):
        return self._send_request("GET", "paths", params=req)

    def read_all_documents(self, req):
        return self._send_request("GET", "all", params=req)
