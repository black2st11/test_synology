import requests
import json
import sys
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-chat_api_url', help='enter your chat api url')
parser.add_argument('-repository', help='enter your git respository')
parser.add_argument('-status', help='return status')
parser.add_argument('-message_id', help='enter your git message id')
parser.add_argument('-message', help='enter your git message')
parser.add_argument('-git_url', help='enter your git url')
parser.add_argument('-timestamp', help='enter your push timestamp')

args = parser.parse_args()

def send_synology_chat(args):

    json_data = json.dumps({"text": f"Github \n *REPOSITORY* : {args.repository}\n *STATUS* : {args.status}\n *MESSAGE_ID* : {args.message_id}\n *MESSAGE* : {args.message}\n *GIT_URL* : {args.git_url}\n *TIMESTAMP* : {args.timestamp}"})
    print(json_data)
    res = requests.post(
        args.chat_api_url,
        {'payload': json_data},
        headers={'Content-Type': 'application/json'}
    )

if __name__ == '__main__':
    send_synology_chat(args)