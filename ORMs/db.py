from sqlalchemy import create_engine, MetaData, engine

DB_URI='postgresql+psycopg2://postgres:qwert12345@localhost:5432/postgres'
engine=create_engine(DB_URI, echo=True)

try:
    connection=engine.connect()
    print("connection successful!")
    connection.close()
except Exception as e:
    print("connection failed:", e)

metadata_obj=MetaData()
