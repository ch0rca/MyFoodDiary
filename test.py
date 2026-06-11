import getUser
import showCalendar
import loadHistory
from datetime import datetime
"""파일 설명
    구현된 Notion DB 쿼리 함수들 테스팅 및 리턴 내용 이해를 위한 파일
"""

# database_id = " "
# calandar_database_id = " "
# token = " "
# calandar_address =" "

print(getUser.checkIdandPW("nno_on", "tjdwo", database_id, token))      # Correct ID, PW -> 유저의 info 전달
print(getUser.checkIdandPW("nno_on", "tjdwo96", database_id, token))    # PW error 
print(getUser.checkIdandPW("munal", "tjdwo", database_id, token))       # ID 존재 X


#Calendar에 먹은 기록 추가

history_info = loadHistory.HistoryFormat(food_name="떡볶이", user_name="조성원", restaurant_name="신전떡볶이", star_count=3)
print(loadHistory.addHistory(databaseID=calandar_database_id, token=token, history_info=history_info))

# showCalendar.openWeb(calandar_address)
