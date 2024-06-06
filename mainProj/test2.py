import json
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

conversation_text = "Hello, how are you?"
url = 'http://localhost:5000/conversation'
data = json.dumps({'text': conversation_text}).encode('utf-8')

req = Request(url, data=data, headers={'Content-Type': 'application/json'})

try:
    with urlopen(req) as response:
        response_body = response.read().decode('utf-8')
        print('Response code:', response.getcode())
        print('Response body:', response_body)
except HTTPError as e:
    print('HTTP error:', e.code, e.reason)
except URLError as e:
    print('URL error:', e.reason)
