import requests
import json

# url = " "

payload = {
    "page_size": 100,
    # "filter": {
    #     "property": "이름",
    #     "rich_text": {
    #         "contains": "조성원"
    #     }
    # }
}
headers = {
    "accept": "application/json",
    "Notion-Version": "2022-06-28",
    "content-type": "application/json",
    # "authorization": " "
}

response = requests.post(url, json=payload, headers=headers)
data = response.json()
for result in data['results']:
            try:
                properties = result['properties']
                col1 = properties['ID']['title'][0]['text']['content']
                col2 = properties['PW']['rich_text'][0]['text']['content']
                col3 = properties['이름']['rich_text'][0]['text']['content']
                col4 = properties['나이']['rich_text'][0]['text']['content']
                print(f'ID: {col1}, PW: {col2}, 이름: {col3}, 나이: {col4}')
            except:
                continue

#print(json.dumps(data, ensure_ascii=False, indent=3))