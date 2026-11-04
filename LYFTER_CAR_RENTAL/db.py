import psycopg2

class PgManager:
    def __init__(self, db_name, user, password, host, port=5432):
        self.db_name=db_name
        self.user=user
        self.password=password
        self.host=host
        self.port=port

        self.connection=self.created_connection()
        if self.connection:
            print("1- connected to database")
            self.cursor=self.connection.cursor()

    def created_connection(self):
        try:
            connection=psycopg2.connect(
                dbname=self.db_name,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            return connection
        except Exception as e:
            print(f"Error connecting to data base: {e}")
            return None

    def close_connection(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
            print("Connection closed")

    def execute_query(self, query, args):
        self.cursor.execute(query, args)
        self.connection.commit()
        result=None
        if self.cursor.description:
            result=self.cursor.fetchall()
            return result