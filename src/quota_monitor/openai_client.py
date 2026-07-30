import json
from urllib.parse import urlencode
from urllib.request import Request, urlopen

BASE_URL = "https://api.openai.com/v1"


class OpenAIAdminClient:
    def __init__(self, admin_key: str, timeout: int = 45):
        if not admin_key.startswith("sk-admin-"):
            raise ValueError("Admin API Key must start with sk-admin-")
        self.admin_key = admin_key
        self.timeout = timeout

    def get(self, path: str, params: dict) -> dict:
        url = f"{BASE_URL}{path}?{urlencode(params, doseq=True)}"
        request = Request(url, headers={"Authorization": f"Bearer {self.admin_key}"})
        with urlopen(request, timeout=self.timeout) as response:
            return json.loads(response.read())
