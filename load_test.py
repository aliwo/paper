from database.engine import SessionMaker


session = SessionMaker()


for _ in range(10000):
    session.execute('''SELECT COUNT(restaurants.id) FROM restaurants WHERE ST_Contains(
        restaurants.delivery_zone,
        ST_GeomFromText(
            'POINT (37.486411 126.987975)',
            4326
        )
    );''')
    session.execute('''SELECT COUNT(restaurants.id) FROM restaurants
    INNER JOIN restaurant_deliverable_locations AS rdl on restaurants.id = rdl.restaurant_id
    INNER JOIN locations AS l ON rdl.location_id = l.id
    WHERE l.id = 2815;
    ''')

# session.commit()
session.close()
