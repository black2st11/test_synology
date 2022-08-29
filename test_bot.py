import requests
import json
import sys

print(sys.argv)

chat_api_url = sys.argv[1]
git_repository = sys.argv[2]
git_message_id = sys.argv[3]
git_message = sys.argv[4]
git_url = sys.argv[5]
git_timestamp = sys.argv[6]
status = sys.argv[7]
json_data = json.dumps({"text": f"repository: {git_repository}\nstatus: {status} \nmessage_id: {git_message_id} \nmessage: {git_message} \ngit_url: {git_url} \ntimestamp: {git_timestamp}"})

res = requests.post(
    chat_api_url,
    {'payload': json_data},
    headers={'Content-Type': 'application/json'}
)

print(res.text)
