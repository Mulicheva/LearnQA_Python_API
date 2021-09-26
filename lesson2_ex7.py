import requests

url_api = "https://playground.learnqa.ru/ajax/api/compare_query_type"

# question 1

response = requests.get(url_api)
print(response.text)
# answer Wrong method provided

# question 2
method = "HEAD"
response = requests.head(url_api, data={"method": method})
print(response.text)
# answer - it print nothing

# question 3
method = "POST"
response = requests.post(url_api, data={"method": method})
print(response.text)
# answer {"success":"!"}

# question 4

methods = ["GET", "POST", "PUT", "DELETE"]
for i in methods:
    response = requests.get(url_api, params={"method": i})
    print(f"Get Method {i} answer {response.text}")
print()
for i in methods:
    response = requests.post(url_api, data={"method": i})
    print(f"POST Method {i} answer {response.text}")

print()
for i in methods:
    response = requests.put(url_api, data={"method": i})
    print(f"PUT Method {i} answer {response.text}")

print()
for i in methods:
    response = requests.delete(url_api, data={"method": i})
    print(f"DELETE Method {i} answer {response.text}")
#answer Delete method success in 2 methods : get and delete