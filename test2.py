import psycopg2
import environ

env = environ.Env()

environ.Env.read_env()

connection = psycopg2.connect(user="postgres",
                                password=env('DATABASE_PASS'),
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