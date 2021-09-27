import json

import pytest
import requests
class TestLesson3Ex13:
    user_agent_params=[
        ("Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"),
        ("Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1"),
        ("Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"),
        ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0"),
        ("Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"),
    ]
    @pytest.mark.parametrize('uaparam',user_agent_params)
    def test_check_cookie(self, uaparam):
        response=requests.get( "https://playground.learnqa.ru/ajax/api/user_agent_check", headers={"User-Agent": uaparam}  )
        obj = json.loads(response.text)
        device =obj["device"]
        browser =obj["browser"]
        platform =obj["platform"]
        print(device, browser, platform)
        if uaparam == "Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30":
           assert platform =='Mobile', "wrong platform in user agent 1"
           assert browser == 'No', "wrong browser in user agent 1"
           assert device == 'Android', "wrong device in user agent 1"
        elif uaparam == "Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1":
           assert platform == 'Mobile', "wrong platform in user agent 2"
           assert browser == 'Chrome', "wrong browser in user agent 2"
           assert device == 'iOS', "wrong device in user agent 2"
        elif uaparam == "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)":
           assert platform == 'Googlebot', "wrong platform in user agent 3"
           assert browser == 'Unknown', "wrong browser in user agent 3"
           assert device == 'Unknown', "wrong device in user agent 3"
        elif uaparam == "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0":
           assert platform == 'Web', "wrong platform in user agent 4"
           assert browser == 'Chrome', "wrong browser in user agent 4"
           assert device == 'No', "wrong device in user agent 4"
        elif uaparam == "Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1":
           assert platform == 'Mobile', "wrong platform in user agent 5"
           assert browser == 'No', "wrong browser in user agent 5"
           assert device == 'iOS', "wrong device in user agent 5"