import requests

url="https://jsonplaceholder.typicode.com/posts"
data={
    "title":"Devikas session","body":"hello","userId":1
}

response=requests.post(url,json=data)
print(response.json())
print(response.status_code)