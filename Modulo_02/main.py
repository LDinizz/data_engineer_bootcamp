from sqlalchemy import create_engine
import pandas as pd

engine = create_engine('postgresql+psycopg2://root:root@localhost:5435/test_db')


sql = '''
    select * from "Billboard" 
    limit 10
'''

df = pd.read_sql_query(sql,engine)


sql2 = '''
CREATE TABLE tb_artist AS (
    SELECT
        T1."date"
    ,   T1."rank"
    ,   T1.artist
    ,   T1.song
    FROM "Billboard" AS T1
    WHERE T1.artist = ''
    ORDER BY T1.artist , T1.song , T1."date"
);
'''
#CREATE TABLE
engine.execute(sql2)


