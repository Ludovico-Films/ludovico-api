import strawberry
from datetime import datetime
from lib.db import db


@strawberry.type
class User:
    username: str
    firstName: str
    lastName: str
    dob: datetime
    email: str
    phoneNumber: str


@strawberry.type
class Query:
    @strawberry.field
    def user(self, username: str) -> User:
        user = db.user.find_one({"username": username})
        print(user)
        return User(username=user.username,
                    firstName=user.firstName,
                    lastName=user.lastName,
                    dob=user.dob,
                    email=user.email,
                    phoneNumber=user.phoneNumber)


@strawberry.type
class Mutation:
    @strawberry.mutation
    def add_user(self,
                 username: str,
                 firstName: str,
                 lastName: str,
                 dob: datetime,
                 email: str,
                 phoneNumber: str) -> User:
        print(f"Adding user:\nu: {username} name: {firstName} {lastName}")
        newUser = User(username=username,
                       firstName=firstName,
                       lastName=lastName,
                       dob=dob,
                       email=email,
                       phoneNumber=phoneNumber)
        print(vars(newUser))
        db.user.insert_one(vars(newUser))
        return newUser


schema = strawberry.Schema(query=Query, mutation=Mutation)
