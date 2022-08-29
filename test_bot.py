import requests
import json
import sys


json_data = json.dumps({"text": f"{sys.argv[1]}"})
res = requests.post(
    
'https://odn.i234.me:5001/webapi/entry.cgi?api=SYNO.Chat.External&method=incoming&version=2&token=%22ja5RT3U26Z0vKr3wzRoFVv9Ewft7dm1WUTu8N6X3yZTIgc6bhj8uWOT4Vb4RYrrY%22',
    {'payload': json_data},
    headers={'Content-Type': 'application/json'}
)

print(res.text)
