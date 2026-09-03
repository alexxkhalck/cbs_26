import requests

class APIClient:

    def __init__(self, base_url):
        self.base_url = base_url

    def get_post(self):
        url = f"{self.base_url}/posts"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return response.text


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com"
    client = APIClient(base_url)
    posts = client.get_post()
    print(posts[:5])
