import psycopg2
from psycopg2 import Error


# try:
connection = psycopg2.connect  (user="postgres",
                                password="fuckit420",
                                host="localhost",
                                port="5432",
                                database="postgres")
            
cursor = connection.cursor()

print("PostgreSQL server information")
print(connection.get_dsn_parameters(), "\n")




cursor.execute(
    '''
    insert into products1 (product_id)
    values (2)
    '''
)




# except (Exception, Error) as error:
#     print("Error while connecting to PostgreSQL", error)
# finally:
#     if (connection):
#         cursor.close()
#         connection.close()
#         print("PostgreSQL connection is closed")

connection.commit()

connection.close()
connection.close()
