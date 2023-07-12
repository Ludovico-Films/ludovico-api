import strawberry
from datetime import date
from lib.db import DB

db = DB(config)


@strawberry.type
class User:
    username: str
    firstName: str
    lastName: str
    dob: date
    email: str
    phoneNumber: str


@strawberry.type
class Query:
    @strawberry.field
    def user(self) -> User:
        username = "Todd"
        firstName = "Todd"
        lastName = "Selwitz"
        dob = "2020-02-02"
        email = "todd@todd.com"
        phoneNumber = "+12344152365"
        return User(username=username,
                    firstName=firstName,
                    lastName=lastName,
                    dob=dob,
                    email=email,
                    phoneNumber=phoneNumber)


@strawberry.type
class Mutation:
    @strawberry.mutation
    def add_user(self,
                 username: str,
                 firstName: str,
                 lastName: str,
                 dob: date,
                 email: str,
                 phoneNumber: str) -> User:
        print(f"Adding user:\nu: {username} name: {firstName} {lastName}")
        newUser = User(username=username,
                       firstName=firstName,
                       lastName=lastName,
                       dob=dob,
                       email=email,
                       phoneNumber=phoneNumber)
        try:
            db.client.admin.command("Ping")
        except Exception as e:
            print(e)
        finally:
            return newUser


schema = strawberry.Schema(query=Query, mutation=Mutation)
