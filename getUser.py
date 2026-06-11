import requests
import json

def prettyPrintJson(input): 
    """ #Json 파일 이쁘게 출력
    Args:
        input (json): HTTP POST로 받은 JSON
    """
    print(json.dumps(input, indent=3, ensure_ascii=False))
    return

def jsonToUserList(user_json): #Post로 받은 유저 데이터 파싱
    user_list = list()
    for user in user_json['results']:
        try:
            user_dict = dict()
            properties = user['properties']
            id = properties['ID']['title'][0]['text']['content']
            pw = properties['PW']['rich_text'][0]['text']['content']
            name = properties['이름']['rich_text'][0]['text']['content']
            age = properties['나이']['rich_text'][0]['text']['content']
            user_dict["ID"] = id; user_dict["PW"] = pw; user_dict["NAME"] = name; user_dict["AGE"] = age
            user_list.append(user_dict)
        except:
            continue
    return user_list

def postToNotion(url, payload, headers): #Notion에 Post
    response = requests.post(url, json=payload, headers=headers)
    user_json = response.json()
    return jsonToUserList(user_json)

def makeFilter(payload, attribute_name="", attribute_type="", want_to_filter=""): # 유저 쿼리를 위한 Filter 생성
    maked_filter = {
        "property": f"{attribute_name}",
        f"{attribute_type}": {
            "contains": f"{want_to_filter}"
        }
    }
    payload["filter"] = maked_filter
    return payload

def makeURL(database_id): # HTTP URL 만들기
    url = f"https://api.notion.com/v1/databases/{database_id}/query"# 내가 쿼리를 보낼 데이터베이스
    return url

def makeHeaders(token): # HTTP Header 만들기.
    headers = {
        "accept": "application/json",
        "Notion-Version": "2022-06-28",
        "content-type": "application/json",
        "authorization": f"Bearer {token}"
    }
    return headers

def makePayload(attribute_name="", attribute_type="", want_to_filter=""): #HTTP Payload 만들기
    payload = {
        "page_size": 100
    }
    if(attribute_name != ""):
        payload =  makeFilter(payload, attribute_name, attribute_type, want_to_filter)
    return payload


def queryAllUser(database_id, token): 
    """모든 User Notion DB에서 가져오기

    Args:
        database_id (str): 쿼리를 날릴 Notion DB id
        token (str): API Key

    Returns:
        list: 유저 데이터가 담긴 리스트
    """
    user_list = postToNotion(makeURL(database_id), makePayload(), makeHeaders(token))
    return user_list



def queryUser(database_id, token, attribute_name="", attribute_type="", want_to_filter=""): 
    """특정 User만 Notion DB에서 가져오기. Notion에서 직접 확인해보면 됨.

    Args:
        database_id (str): _description_
        token (str): _description_
        attribute_name (str, optional): Notion DB column 값. Defaults to "".
        attribute_type (str, optional): Notion DB column type. Defaults to "".
        want_to_filter (str, optional): Query하고자 하는 내용. Defaults to "".

    Returns:
        list: 유저 데이터가 담긴 리스트
    """
    user_list = postToNotion(makeURL(database_id), makePayload(attribute_name, attribute_type, want_to_filter), makeHeaders(token), )
    return user_list

def makeReponseDict(request_text="", reason_text="", user_info: dict = ""):
    """response 객체를 생성하는 Function

    Args:
        request_text (str, optional): 쿼리 요청 성공 or 실패 여부. Defaults to "".
        reason_text (str, optional): 요청이 실패한 경우, 실패 이유. Defaults to "".
        user_info (dict) : 요청이 성공한 경우, 유저의 정보를 전달
    """
    return {"Request": f"{request_text}", "Reason": f"{reason_text}", "user_info" : user_info}


def checkIdandPW(ID: str, PW:str, database_id, token):
    """특정 ID와, PW로 user가 존재하는지 체크하는 Function

    Args:
        ID (str): user가 입력한 ID
        PW (str): user가 입력한 PW
    """
    specific_user = queryUser(database_id, token, "ID", "title", ID)
    if not specific_user:
        return makeReponseDict("Failed", "No ID in Database")
    user_info = specific_user[0]
    user_pw_in_database = user_info["PW"]
    if(user_pw_in_database != PW):
        return makeReponseDict("Failed", "Wrong Password")
    return makeReponseDict("Success", user_info=user_info)