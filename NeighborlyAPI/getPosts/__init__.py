import logging
import azure.functions as func
import pymongo
import json
from bson.json_util import dumps


def main(req: func.HttpRequest) -> func.HttpResponse:

    logging.info('Python getPosts trigger function processed a request.')

    try:
        url = "mongodb://duongnq9-project2-cosmosdb-acc:gjKNOD7FD6SaBYJM2mt8gCOjDUEXdBmEUXMswMI4T8zkLobfEhfPI29q4AVp2ae05hofX6pEM5H38oEzZ69iyA==@duongnq9-project2-cosmosdb-acc.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@duongnq9-project2-cosmosdb-acc@"  # TODO: Update with appropriate MongoDB connection information
        client = pymongo.MongoClient(url)
        database = client['duongnq9-project2-mongodb']
        collection = database['posts']

        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8', status_code=200)
    except:
        return func.HttpResponse("Bad request.", status_code=400)