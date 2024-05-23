from pydatabridge.pydatabridge import Configuration


class FirebaseBase:
    def __init__(self, config: Configuration):
        self.config = config
        self.headers = self.config.produce_headers()
        self.base_url = self.config.base_url

    def _send_request(self, method, endpoint, data=None, params=None, files=None):
        url = f"{self.base_url}/{endpoint}"
        try:
            if method == "GET":
                response = requests.get(url, headers=self.headers, params=params)
            elif method == "POST":
                response = requests.post(
                    url, headers=self.headers, json=data, files=files
                )
            elif method == "PUT":
                response = requests.put(url, headers=self.headers, json=data)
            elif method == "DELETE":
                response = requests.delete(url, headers=self.headers, json=data)
            else:
                raise ValueError(f"Unsupported method: {method}")

            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}
