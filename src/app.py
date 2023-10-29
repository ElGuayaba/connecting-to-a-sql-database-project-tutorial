import os
from sqlalchemy import create_engine, text
import pandas as pd
from dotenv import load_dotenv

# load the .env file variables
load_dotenv()

# 1) Connect to the database here using the SQLAlchemy's create_engine function

global engine # This allows us to use a global variable called engine
connection_string = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
print("Starting the connection...")
engine = create_engine(connection_string)

# 2) Execute the SQL sentences to create your tables using the SQLAlchemy's execute function
with engine.connect() as con:

    with open("./sql/drop.sql") as file:
        query = text(file.read())
        con.execute(query)

    with open("./sql/create.sql") as file:
        query = text(file.read())
        con.execute(query)

# 3) Execute the SQL sentences to insert your data using the SQLAlchemy's execute function
    with open("./sql/insert.sql") as file:
        query = text(file.read())
        con.execute(query)


# 4) Use pandas to print one of the tables as dataframes using read_sql function
    query = '''SELECT * FROM publishers'''
    result = pd.read_sql_query(query, con)
    print(result)