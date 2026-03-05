import mysql.connector

class DatabaseClient:

    def __init__(self, host, user, password, db):
        self.__conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=db
        )
        self.__cursor = self.__conn.cursor(dictionary=True)

    def execute_select(self, query):
        self.__cursor.execute(query)
        return self.__cursor.fetchall()

    def execute_modify(self, query):
        try:
            self.__cursor.execute(query)
            self.__conn.commit()
        except Exception as e:
            self.__conn.rollback()
            raise e

    def close(self):
        self.__cursor.close()
        self.__conn.close()
