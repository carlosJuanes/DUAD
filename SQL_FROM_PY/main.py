import  psycopg2

#creando la coneccion de la database
connection=psycopg2.connect(
    host="localhost",
    port=5432,
    user="postgres",
    password="qwert12345",
    dbname="postgres",
)

request_body={
    "full_name": "jose antonio aguilar",
    "email":"jose@gmail.com",
    "password":"123456",
}

full_name=request_body.get("full_name")
email=request_body.get("email")
password=request_body.get("password")


def format_user(user_record):
    return{
        "id":user_record[0],
        "full_name":user_record[1],
        "email":user_record[2],
        "password":user_record[3],
    }

print("1- connected data base")

#creando el cursor para ejecutar queries en la base de datos.
cursor=connection.cursor()
cursor.execute(f"INSERT INTO lyfter_duad.users (full_name, email, password) values ('{full_name}', '{email}', '{password}');")
print("2- query executed")


connection.commit()
print("3- connection changes committed")
#results=cursor.fetchall()
#formatted_results=[format_user(result) for result in results]
#print("3- formatted results")
#print(formatted_results)