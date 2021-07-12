import psycopg2
import environ
import os
from dotenv import load_dotenv


# This demo shows connecting psycopg2 database adapter for Python to connect and run queries to PostgreSQL 
# Also the use of dotenv to hide passwords from VCS

load_dotenv()


# env = environ.Env()


# environ.Env.read_env()
# using psycopg2 as the db driver and the sqlalchemy for the orm

connection = psycopg2.connect(user="postgres",
                                password=os.getenv('DATABASE_PASS'),
                                host="localhost",
                                port="5432",
                                database="postgres")

cursor = connection.cursor()

cursor.execute('DROP TABLE IF EXISTS table2;')

cursor.execute('''
  CREATE TABLE table2 (
    id INTEGER PRIMARY KEY,
    completed BOOLEAN NOT NULL DEFAULT False
  );
''')

cursor.execute('INSERT INTO table2 (id, completed) VALUES (%s, %s);', (1, True))

SQL = 'INSERT INTO table2 (id, completed) VALUES (%(id)s, %(completed)s);'

data = {
  'id': 2,
  'completed': False
}
cursor.execute(SQL, data)

connection.commit()

connection.close()
cursor.close()