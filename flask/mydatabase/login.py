from pymongo import MongoClient
from PIL import Image
import pprint
client = MongoClient(host = "localhost", port = 27017)
db = client

for i in db.USER.find():
     pprint.pprint(i)




