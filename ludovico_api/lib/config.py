from dotenv import load_dotenv
import os

load_dotenv()


class Config:
    def __init__(self):
        self.MONGO_USERNAME = os.getenv("MONGO_USERNAME", default="username")
        self.MONGO_PASSWORD = os.getenv("MONGO_PASSWORD", default="password")
        self.MONGO_DB = os.getenv("MONGO_DB", default="1337DB")
        self.MONGO_URI = f"mongodb+srv://{self.MONGO_USERNAME}:{self.MONGO_PASSWORD}@{self.MONGO_DB}.mongodb.net/?retryWrites=true&w=majority"
        print(self.MONGO_URI)
        self.SCHEMA_NAME = os.getenv('SCHEMA_NAME', default='user')
        self.SERVER_PORT = os.getenv('SERVER_PORT', default='3000')
