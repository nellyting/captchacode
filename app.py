from flask import Flask, request, jsonify
import json

from flask.json import dumps

app = Flask(__name__)

simple_database_of_points = {
    'Land Of Stories':5,
    'Workout Star':10
    }

simple_user_database = {
    'Master Moonlarkian':15,
    'yap30317' : 4,
    'faithyhuong' : 0,
    'Siti Jazmina Abd Rashid' : 0,
    'Tester' : 0,
    'nellytingshisiu' : 0,
    'ernernmooi' : 0,
    'bor' : 0
}

def getPointsWithCategory(category):
    if category in simple_database_of_points:
        #if the category does exist, return the point
        return simple_database_of_points[category]
    else:
        #if the category doesn't exist, throw an Error
        raise ValueError("Category doesn't exist")

def addPoints(user,points):
    #add points to existing points
    if user in simple_user_database:
        simple_user_database[user] += points
    else:
        simple_user_database[user] = points
    return simple_user_database[user]
    

@app.route('/points')
def pointsjson():
  user_points = (simple_user_database)
  json_dumps = json.dumps(user_points)
  return json_dumps


@app.route('/category')
def categoryjson():
  category = (simple_database_of_points)
  json_dumps = json.dumps(category)
  return json_dumps
  

@app.route('/points', methods=['POST'])
def points():
   body = json.loads(request.data)
   cat = getPointsWithCategory(body["category"])
   result = addPoints(body["user"], cat)
   #print("point", result)
   #result += cat
   #result1 = [result,cat]
   #total=sum(result1)
   #print("category", cat)
   #print("point", result)
   return jsonify(result) 


@app.route('/category', methods=['POST'])
def category():
   body = json.loads(request.data)
   result =  getPointsWithCategory (body["category"])
   return jsonify (result) 



app.debug = True
app.run ()
app.run(debug = True)
