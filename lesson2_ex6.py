import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect", allow_redirects=True)
last_response = response.history[-1]
print(f"Итоговый URl {last_response.url}")
count_of_redirects =0
for resp in response.history:
    print(resp.status_code, resp.url)
    count_of_redirects = count_of_redirects + 1
print(f"Количество редиректов {count_of_redirects}")