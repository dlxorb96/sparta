from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

movie = db.movies.find_one({'title':'굿 윌 헌팅'})
print(movie['score'])

findscore = movie['score']

movies = list(db.movies.find({'score': findscore},{'_id':False}))
print(movies)

for name in movies:
    print(name['title'])

