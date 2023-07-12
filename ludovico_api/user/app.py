import strawberry
from datetime import datetime
from lib.db import db
from lib.objUtils import to_dict


@strawberry.type
class User:
    username: str
    firstName: str
    lastName: str
    dob: datetime
    email: str
    phoneNumber: str

    @property
    def __dict__(self):
        return {
            "username": self.username,
            "firstName": self.firstName,
            "lastName": self.lastName,
            "dob": self.dob.strftime("%m/%d/%Y, %H:%M:%S"),
            "email": self.email,
            "phoneNumber": self.phoneNumber,
        }


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
        info = db.user.insert_one(vars(newUser))
        print(info)
        return newUser


schema = strawberry.Schema(query=Query, mutation=Mutation)
