import sqlalchemy as alch
import os
from dotenv import load_dotenv

load_dotenv()

dbName = "rickandmorty"
password=os.getenv("sql_password")


connectionData = f"mysql+pymysql://root:{password}@localhost/{dbName}"
engine = alch.create_engine(connectionData)