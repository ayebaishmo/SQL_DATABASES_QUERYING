import sqlite3 as sq

# conn = sq.connect('demo_data.sqlite3')
def connect_tosq_db(db_name = 'demo_data.sqlite3'):
    return sq.connect(db_name)

# cursor = conn.cursor()
# result = cursor.execute(q.CREATING_A_TABLE).fetchall()
def execute_q(conn, query):
    curs = conn.cursor()
    curs.execute(query)
    return  curs.fetchall()

CREATING_A_TABLE = '''
CREATE
TABLE
    demo (
    S VARCHAR(100),
    X INT(100),
    Y INT(100)
    )
'''

INSERT_DATA = '''
INSERT INTO 
    demo
    (S, X, Y)
VALUES
    ('g', 3, 9),
    ('v', 5, 7),
    ('f', 8, 7)
    '''

row_count = '''
SELECT 
COUNT(*)
FROM 
    demo
'''

xy_at_least_5 = '''
SELECT
COUNT(*)
FROM 
    demo
WHERE "X" >=5 AND "Y" >= 5
'''

unique_y = '''
SELECT 
COUNT(DISTINCT y) AS unique_y_count
FROM 
    demo
'''

conn = connect_tosq_db()
# execute_q(conn, q.INSERT_DATA)
# row_count: How many rows are in the table?
result1 = execute_q(conn, row_count)
conn.commit()
print(result1)
# xy_at_least_5: How many rows are there where both x and y are at least 5?
result2 = execute_q(conn, xy_at_least_5)
conn.commit()
print(result2)
# unique_y: How many unique values of y are there (hint - COUNT() can accept a keyword DISTINCT)?
result3 = execute_q(conn, unique_y)
conn.commit()
print(result3)
