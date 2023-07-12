from user.app import schema
from strawberry.asgi import GraphQL
from lib.config import config

app = GraphQL(schema)
