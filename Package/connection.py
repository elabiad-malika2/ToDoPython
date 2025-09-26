from sqlalchemy import create_engine

def get_connection():
    user = 'postgres'
    password = 'malika123'
    host = '127.0.0.1'
    port = 5432
    database = 'todolist_db'

    return create_engine(
        url="postgresql://{0}:{1}@{2}:{3}/{4}".format(
            user, password, host, port, database
        )
    )



try:
        engine = get_connection()
        print(
            f"Connection to the  for user created successfully.")
except Exception as ex:
        print("Connection could not be made due to the following error: \n", ex)