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
    "X"
    "Y",
COUNT(*)
FROM 
    demo
GROUP BY 
    "X", "Y"
HAVING COUNT(*)=5
'''

unique_y = '''
SELECT 
COUNT(DISTINCT y) AS unique_y_count
FROM 
    demo
'''