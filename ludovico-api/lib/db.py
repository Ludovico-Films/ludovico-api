from os import getenv

from dotenv import load_dotenv

load_dotenv()

from pymongo.mongo_client import MongoClient


# get mongodb URI and database name from environment variale
MONGO_URI = "mongodb+srv://{}:{}@{}.mongodb.net/?retryWrites=true&w=majority".format(
    getenv("MONGO_USERNAME", default="username"),
    getenv("MONGO_PASSWORD", default="password"),
    getenv("MONGO_DB", default="1337DB")
)

client = MongoClient(MONGO_URI)

try:
  client.admin.command('ping')
  print("Pinged")
except Exception as e:
  print(e)