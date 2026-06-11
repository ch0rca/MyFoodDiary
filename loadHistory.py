import requests, json
from datetime import datetime

class HistoryFormat:
    def __init__(self, food_name, user_name, restaurant_name, star_count):
        self.food_name= food_name
        self.user_name = user_name
        self.restaurant_name = restaurant_name
        self.star_rank = self.make_star_rank(star_count)
        self.date = str(datetime.now().date())
        
    def make_star_rank(self, star_count):
        star_rank = str()
        for i in range(star_count):
            star_rank += "⭐️"
        return star_rank

def addHistory(databaseID : str, token : str, history_info : HistoryFormat):
    """Calendar에 특정 유저가 먹은 기록 추가

    Args:
        databaseID (str): database ID
        token (str): API Token
        history_info(HistoryFormat): 유저가 먹은 정보가 담긴 info
    """
    
    return postToCalendar(databaseID, makeHeaders(token), history_info)

def postToCalendar(databaseId : str, headers: dict, history_info : HistoryFormat):
    """유저가 먹은 기록을 Calendar에 저장

    Args:
        databaseID (str): database ID
        token (str): API Token
        history_info(HistoryFormat): 유저가 먹은 정보가 담긴 info
    """
    createdUrl = "https://api.notion.com/v1/pages"
    newPageData = {
        "parent": {"database_id": databaseId},
        "properties": {
            "음식이름": makeProperties("title", history_info.food_name),
            "이름": makeProperties("rich_text", history_info.user_name),
            "가게이름": makeProperties("rich_text", history_info.restaurant_name),
            "별점" : makeProperties("rich_text", history_info.star_rank),
            "날짜" : makeDateProperties(history_info.date)
        }
    }
    res = requests.post(createdUrl, headers=headers, data=json.dumps(newPageData))
    if(res.status_code != 200):
        return makeReponseDict("Failed")
    return makeReponseDict("Success")

def makeProperties(property_type : str, property_body : str):
    """추가할 속성 값을을 만들어주기

    Args:
        property_type (str): Notion내 특정 데이터의 타입
        property_body (str): 들어갈 데이터 

    Returns:
        dict: Property dictionary
    """
    property = {
        f"{property_type}": [
            {
                "text":{
                    "content" : property_body
                }
            }
        ]
    }
    return property

def makeDateProperties(property_body : str):
    property = {
        "date": {
            "start": property_body
        }
    }
    return property

def makeReponseDict(request_text):
    return {"Request": f"{request_text}"}

def makeHeaders(token : str):
    """ Make header for Notion Post

    Args:
        token (str): API Token

    Returns:
        dict : headers for HTTP Post
    """
    headers = {
        "Authorization": "Bearer " + token,
        "Content-Type": "application/json",
        "Notion-Version": "2022-02-22"
    }
    return headers