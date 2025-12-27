import requests

class ApiHelper:

    url = "127.0.0.1:8000"

    @staticmethod
    def get(endpoint: str, query_params: dict = None):
        full_url = f"http://{ApiHelper.url}/{endpoint}"
        response = requests.get(full_url, params=query_params)
        return response
    
    @staticmethod
    def post(endpoint: str, data: dict = None, query_params: dict = None):
        full_url = f"http://{ApiHelper.url}/{endpoint}"
        response = requests.post(full_url, json=data, params=query_params)
        return response
        