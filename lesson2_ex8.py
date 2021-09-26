import requests
import json
import time
url_api = "https://playground.learnqa.ru/ajax/api/longtime_job"
#response = requests.get(url_api, params={"method": i})
 #   print(f"Get Method {i} answer {response.text}")
response = requests.get(url_api)
obj = json.loads(response.text)
token_value= obj["token"]
time_value =obj["seconds"]
#print(token_value)
#print(time_value)

response2 = requests.get(url_api,params={"token":token_value})
obj2 = json.loads(response2.text)
status_is = obj2["status"]
if status_is == "Job is NOT ready":
    print("Job is NOT ready - it is ok")
    print (f"We will wait {time_value} sec")
    time.sleep(time_value)
    response3 = requests.get(url_api, params={"token": token_value})
    obj3 = json.loads(response3.text)
    status_is = obj3["status"]
    key="result"
    if key in obj3:
        if status_is == "Job is ready":
            print(f"Job is ready and result is : {obj3['result']} it is ok")
        else:
            print("Job is NOT ready - it is not ok")
    else:
        print("No result it is not ok")
else:
    print("Job is ready- it is not ok")



