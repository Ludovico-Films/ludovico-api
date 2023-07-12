from pymongo.mongo_client import MongoClient


class DB:
    def __init__(self, config):
        # get mongodb URI and database name from environment variale
        try:
            self.client = MongoClient(config.MONGO_URI)
        except Exception as e:
            print(e)
