import requests
class TestLesson3Ex12:
    def test_check_cookie(self):
        url_api = "https://playground.learnqa.ru/api/homework_header"
        response = requests.get(url_api)
        print(response.headers)
        assert "x-secret-homework-header" in response.headers, "Header is not the same"


