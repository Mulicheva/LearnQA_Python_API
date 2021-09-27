import requests
class TestLesson3Ex10:
    def test_check_cookie(self):
        url_api = "https://playground.learnqa.ru/api/homework_cookie"
        response = requests.get(url_api)
        print(response.cookies)
        assert "HomeWork" in response.cookies, "Cookie not the same"


