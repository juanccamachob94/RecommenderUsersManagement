import csv

class UserCreatorService:
    @classmethod
    def perform(cls, user, csvManager):
        csvManager.read()
        