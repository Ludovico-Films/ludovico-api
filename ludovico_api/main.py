from user.app import schema
from strawberry.asgi import GraphQL
from lib.config import Config

global config
config = Config()

app = GraphQL(schema)
