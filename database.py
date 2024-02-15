from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.user_login_system
user_login_credentials = db.user_login_credentials
