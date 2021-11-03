import requests

from database.engine import SessionMaker
from join_model.models import Location

URI = 'https://www.juso.go.kr/addrlink/addrLinkApi.do'
KEY = 'devU01TX0FVVEgyMDIxMTEwMTE0NTYxMDExMTgyNzI='

MAIN_LOCATION = '강남대로'
OPTIONAL_LOCATIONS = {
    'seocho': '서초대로',  # 1419 건
    'bau': '바우뫼로',  # 490 건
    'hyo': '효령로',  # 1830 건
}

# 2021-11-03 실행 성공


def get_locations(keyword: str, page: int) -> list:
    response = requests.get(
        URI,
        params={
            'confmKey': KEY,
            'keyword': keyword,
            'resultType': 'json',
            'addInfoYn': 'Y',
            'countPerPage': 100,
            'currentPage': page,
        },
    )
    return response.json().get('results').get('juso')


session = SessionMaker()

#  강남대로는 모든 레스토랑 배달 가능!

for page in range(1, 30):
    session.bulk_insert_mappings(
        Location,
        [
            {
                'name': doc.get('roadAddr'),
                'memo': MAIN_LOCATION,
            } for doc in get_locations(MAIN_LOCATION, page)
        ],
    )

session.commit()


for key, location in OPTIONAL_LOCATIONS.items():
    for page in range(1, 30):
        session.bulk_insert_mappings(
            Location,
            [
                {
                    'name': doc.get('roadAddr'),
                    'memo': location,
                } for doc in get_locations(location, page)
            ],
        )

session.commit()
session.close()



