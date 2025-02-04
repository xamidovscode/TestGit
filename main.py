import requests

class WebScrapingStudy:

    def __init__(self, url, token, chat_id):
        self.token = token
        self.chat_id = chat_id
        self.url = url

    @staticmethod
    def send_telegram_message(token, chat_id, message: str):
        url = f"https://api.telegram.org/bot{token}/sendMessage"
        data = {"chat_id": chat_id, "text": message}
        requests.post(url=url, data=data)

    @staticmethod
    def get_json_data(url: str):
        response = requests.get(url)
        return response.json().get("data")

    def run_script(self):
        responses = self.get_json_data(self.url)
        for response in responses:
            name = response.get("name")
            self.send_telegram_message(token=self.token, chat_id=self.chat_id, message=name)
        return responses


