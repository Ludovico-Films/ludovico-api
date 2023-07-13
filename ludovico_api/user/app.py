import strawberry
from typing import Optional
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
    # TODO
    # @strawberry.field
    # def allUsers(self) -> User:
    #     users = db.user.find_many()
    #     Users = []
    #     for user in users:
    #         Users.append(username=user["username"],
    #                      firstName=user["firstName"],
    #                      lastName=user["lastName"],
    #                      dob=user["dob"],
    #                      email=user["email"],
    #                      phoneNumber=user["phoneNumber"])
    #     return Users

    @strawberry.field
    def user(self,
             username: Optional[str] = None,
             firstName: Optional[str] = None,
             lastName: Optional[str] = None,
             dob: Optional[str] = None,
             email: Optional[str] = None,
             phoneNumber: Optional[str] = None) -> User:
        find_one_dict_orig = {
            "username": username,
            "firstName": firstName,
            "lastName": lastName,
            "dob": dob,
            "email": email,
            "phoneNumber": phoneNumber
        }
        find_one_dict = {}
        for key in find_one_dict:
            if find_one_dict[key] is not None:
                find_one_dict[key] = find_one_dict_orig[key]
        user = db.user.find_one(find_one_dict)
        print(user)
        return User(username=user["username"],
                    firstName=user["firstName"],
                    lastName=user["lastName"],
                    dob=user["dob"],
                    email=user["email"],
                    phoneNumber=user["phoneNumber"])


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
