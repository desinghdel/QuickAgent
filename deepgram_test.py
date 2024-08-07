import requests

api_key = 'bd8762f77777a1829ded6c077fa8abdfa38f31ed'
url = 'https://api.deepgram.com/v1/listen'

headers = {
    'Authorization': f'Token {api_key}',
    'Content-Type': 'application/json'
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    print("API key is valid")
else:
    print(f"API key is invalid: {response.status_code} - {response.text}")