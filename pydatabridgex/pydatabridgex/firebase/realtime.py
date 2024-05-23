import requests
from pydatabridge.pydatabridge import Configuration


class RealTime(FirebaseBase):
    def __init__(self, config: Configuration):
        super().__init__(config)

    def create_item(self, data):
        return self._send_request("POST", "create", data={"data": data})

    def read_items(self, req):
        return self._send_request("GET", "read", params=req)

    def update_item(self, id, new_data):
        return self._send_request("PUT", "update", data={"id": id, "newData": new_data})

    def delete_item(self, id):
        return self._send_request("DELETE", "delete", data={"id": id})
