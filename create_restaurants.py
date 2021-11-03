from database.engine import SessionMaker
from join_model.models import Restaurant

menus_in_hyo = ['치킨', '김밥', '피자', '짜장면']
menus_in_seocho = ['샐러드', '비빔밥']
menus_in_bau = ['김치찌개']

session = SessionMaker()

for menu in menus_in_hyo:
    for i in range(1, 201):
        r = Restaurant(name=f'{menu}#{i}')
        session.add(r)
        session.flush()
        session.execute(
            f"INSERT INTO restaurant_deliverable_locations(restaurant_id, location_id)"
            f"SELECT {r.id}, l.id FROM locations l WHERE memo IN ('강남대로', '효령로')"
        )

for menu in menus_in_seocho:
    for i in range(1, 201):
        r = Restaurant(name=f'{menu}#{i}')
        session.add(r)
        session.flush()
        session.execute(
            f"INSERT INTO restaurant_deliverable_locations(restaurant_id, location_id)"
            f"SELECT {r.id}, l.id FROM locations l WHERE memo IN ('강남대로', '서초대로')"
        )

for menu in menus_in_bau:
    for i in range(1, 201):
        r = Restaurant(name=f'{menu}#{i}')
        session.add(r)
        session.flush()
        session.execute(
            f"INSERT INTO restaurant_deliverable_locations(restaurant_id, location_id)"
            f"SELECT {r.id}, l.id FROM locations l WHERE memo IN ('강남대로', '바우뫼로')"
        )


session.commit()
session.close()




