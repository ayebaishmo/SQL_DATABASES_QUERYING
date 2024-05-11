import sqlite3 as sq

# conn = sq.connect('northwind_small-1.sqlite3')
# curs = conn.cursor()
# result = curs.execute('SELECT * FROM Category').fetchall()


def connect_tosq_db(db_name = 'northwind_small.sqlite3'):
    return sq.connect(db_name)

# cursor = conn.cursor()
# result = cursor.execute(q.CREATING_A_TABLE).fetchall()
def execute_q(conn, query):
    curs = conn.cursor()
    curs.execute(query)
    return  curs.fetchall()

# expensive_items: What are the ten most expensive items (per unit price) in the database? Please return all columns in the table, not just
expensive_items = '''
SELECT *
FROM Product
ORDER BY UnitPrice DESC
LIMIT 10
'''

# avg_hire_age: What is the average age of an employee at the time of their hiring? (Hint: a lot of arithmetic works with dates.)
avg_hire_age = '''
SELECT
AVG(strftime('%Y', HireDate) - strftime('%Y', BirthDate)) AS avg_hire_age
FROM employee
'''

# ten_most_expensive: What are the ten most expensive items (per unit price) in the database and their suppliers? 
ten_most_expensive = '''
SELECT Product.ProductName, Product.UnitPrice, Supplier.CompanyName
FROM Product
JOIN Supplier ON Product.SupplierId = Supplier.Id
ORDER BY Product.UnitPrice DESC
LIMIT 10
'''

# largest_category: What is the largest category (by number of unique products in it)?
largest_category = '''
SELECT CategoryName, ProductCount
FROM Category
JOIN (
    SELECT CategoryId, COUNT(*) AS ProductCount
    FROM Product
    GROUP BY CategoryId
    ORDER BY ProductCount DESC
    LIMIT 1
) AS LargestCategory ON Category.Id = LargestCategory.CategoryId
''' 

conn  = connect_tosq_db()
result = execute_q(conn, expensive_items)
conn.commit()
print(result)
result1 = execute_q(conn, avg_hire_age)
conn.commit()
print(result1)
result2 =execute_q(conn, ten_most_expensive)
conn.commit()
print(result2)
result3 = execute_q(conn, largest_category)
conn.commit()
print(result3)