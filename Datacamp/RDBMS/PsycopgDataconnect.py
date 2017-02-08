from psycopg2 import connect, DatabaseError

try:
    conn = connect(database='postgres', user='postgres', port=5433, password='1234')
    cur = conn.cursor()
    cur.execute('SELECT version()')
    version = cur.fetchone()
    cur.execute('CREATE DATABASE dvdrental')
    cur.close()
except (Exception, DatabaseError) as err:
    print(err)
finally:
    if conn: conn.close()

print(version)
