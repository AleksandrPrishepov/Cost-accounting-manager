import psycopg2 as ps
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


connection = ps.connect(
    host='127.0.0.1',
    user='postgres',
    password='my_password',
    database='notebooks',
    port=5432
)
#     1. создаем базу данныхnotebooks
# cursor = connection.cursor()
# connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
# cursor.execute("CREATE DATABASE notebooks")
# connection.commit()
# cursor.close()
# connection.close()
# cursor = connection.cursor()

cursor = connection.cursor()
# cursor.execute("""CREATE TABLE brand(
#                 brand_id integer PRIMARY KEY,
#                 name_brand varchar(120) NOT NULL)
# """)
# cursor.execute("""CREATE TABLE notebook(
#                 notebook_id integer PRIMARY KEY,
#                 name_notebook varchar(120) NOT NULL,
#                 diagonal decimal NOT NULL,
#                 depth decimal NOT NULL,
#                 width decimal NOT NULL,
#                 height decimal NOT NULL,
#                 fk_brand_id integer REFERENCES brand(brand_id))
# """)
# cursor.execute("INSERT INTO brand VALUES(1, 'Asus')")
# cursor.execute("INSERT INTO brand VALUES(2, 'HP')")
# cursor.execute("INSERT INTO brand VALUES (3, 'Lenova')")
# cursor.execute("INSERT INTO brand VALUES (4, 'DELL')")
#
# cursor.execute("INSERT INTO notebook VALUES(1, 'G15 5511-378284', 15.6, 272.11, 357.2, 23.3, 4)")
# cursor.execute("INSERT INTO notebook VALUES(2, 'G15 5511-378283', 15.6, 272.11, 357.2, 23.4, 4)")
# cursor.execute("INSERT INTO notebook VALUES(3, 'IdeaPad 5 Pro 16IHU6 82L9004JR', 17, 251, 356, 16.9, 3)")
# cursor.execute("INSERT INTO notebook VALUES(4, 'IdeaPad 3 15ITL6 82H8009WRE', 15.6, 236.5, 359.2, 19.9, 3)")
# cursor.execute("INSERT INTO notebook VALUES(5, 'ThinkPad P1 Gen 3 20TJS60C00', 15.6, 245.7, 361.8, 18.7, 3)")
# cursor.execute("INSERT INTO notebook VALUES(6, 'ENVY 13-ba1204nw ((4H316EA))', 13.3, 195, 307, 16.9, 2)")
# cursor.execute("INSERT INTO notebook VALUES(7, 'GGaming Pavilion 15-dk2325nw', 15.6, 256, 360, 23.4, 2)")
# cursor.execute("INSERT INTO notebook VALUES(8, 'Pavilion 15-eh1154nw ((4H3T9EA))', 15.6, 234, 360.2, 17.9, 2)")
# cursor.execute("INSERT INTO notebook VALUES(9, '15s-eq2304nw', 15.6, 242, 358.5, 17.9, 2)")
# cursor.execute("INSERT INTO notebook VALUES(10, 'TUF Gaming A15 FA506ICB', 15.6, 256, 359.8, 24.9, 1)")
# cursor.execute("INSERT INTO notebook VALUES(11, 'Vivobook 15 OLED K513EA-L12974', 15.6, 235, 359, 17.9, 1)")
# cursor.execute("INSERT INTO notebook VALUES(12, 'X415MA-EB521', 14.0, 216, 325.4, 19.9, 1)")
# cursor.execute("INSERT INTO notebook VALUES(13, 'TUF Gaming F15 FX506LHB', 15.6, 256, 359, 24.9, 1)")
# cursor.execute("INSERT INTO notebook VALUES(14, ' IdeaPad 3 15IGL05 81WQ0023RE', 15.6, 253.4, 362.2, 19.9, 3)")


cursor.execute("""SELECT fk_brand_id, count(name_notebook) as count
                FROM notebook
                GROUP BY fk_brand_id ORDER BY count DESC
""")
cursor.execute("""SELECT round(diagonal), count(fk_brand_id) as count
                FROM notebook
                GROUP BY diagonal ORDER BY diagonal
""")

connection.commit()
cursor.close()
connection.close()


