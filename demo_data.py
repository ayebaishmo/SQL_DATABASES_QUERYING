import sqlite3 as sq
import Queries as q

# conn = sq.connect('demo_data.sqlite3')
def connect_tosq_db(db_name = 'demo_data.sqlite3'):
    return sq.connect(db_name)

# cursor = conn.cursor()
# result = cursor.execute(q.CREATING_A_TABLE).fetchall()
def execute_q(conn, query):
    curs = conn.cursor()
    curs.execute(query)
    return  curs.fetchall()


if __name__ == "__main__":
    conn = connect_tosq_db()
    # execute_q(conn, q.INSERT_DATA)
    # row_count: How many rows are in the table?
    result1 = execute_q(conn, q.row_count)
    conn.commit()
    print(result1)

    # xy_at_least_5: How many rows are there where both x and y are at least 5?
    result2 = execute_q(conn, q.xy_at_least_5)
    conn.commit()
    print(result2)

    # unique_y: How many unique values of y are there (hint - COUNT() can accept a keyword DISTINCT)?
    result3 = execute_q(conn, q.unique_y)
    conn.commit()
    print(result3)
