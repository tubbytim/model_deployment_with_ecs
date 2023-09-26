import requests

test_data =             {
                "name": "Foo",
                "sex": "male",
                "age": 35,
                "fare": 302,
                "cabin": "C1",
                "embarked": "belfast",
                'pclass': 3,
                'sibsp':0,
                'parch':0
            }

response = requests.post("http://localhost:8000/predict", json={'input':test_data})
print(response.text)
response.raise_for_status()
print(response.json())
