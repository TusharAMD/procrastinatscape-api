from flask import Flask
from flask_cors import CORS, cross_origin
import pymongo
import os

app = Flask(__name__)
cors = CORS(app)

@cross_origin()
@app.route('/addtask')
def addtask():
    return {"status":200}

@cross_origin()
@app.route('/getCards',methods=['GET'])
def getCards():
    
    client = pymongo.MongoClient("mongodb+srv://admin:admin@cluster0.wonbr.mongodb.net/?retryWrites=true&w=majority")
    db = client.MentalHacks
    col = db["cards"]
    retDict = {"res":[]}
    for x in col.find():
        x.pop("_id")
        retDict["res"].append(x)
        print(x)


    return retDict

if __name__ == '__main__':
    app.run(port=int(os.environ.get("PORT", 5001)))