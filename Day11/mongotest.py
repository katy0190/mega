from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import Movie

uri = "mongodb+srv://xodus0118:비밀번호@xodus0118.nr0cb6s.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
db = client['test']
collection = db['CGV']


name = input('등록할 영화 이름을 넣어주세요:')
location = input('위치를 넣어주세요:')
time = int(input('상영 시간을 넣어주세요:'))
rank = input('영화 등급을 넣어주세요:')


newMovie = Movie.Movie(name, location, time, rank)

collection.insert_one(newMovie.__dict__)


# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)