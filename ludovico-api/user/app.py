import strawberry
from datetime import date


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
        return User(username=username,
                    firstName=firstName,
                    lastName=lastName,
                    dob=dob,
                    email=email,
                    phoneNumber=phoneNumber)


schema = strawberry.Schema(query=Query, mutation=Mutation)
