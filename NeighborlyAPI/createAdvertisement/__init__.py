import azure.functions as func
import pymongo

def main(req: func.HttpRequest) -> func.HttpResponse:

    request = req.get_json()

    if request:
        try:
            url = "mongodb://duongnq9-project2-cosmosdb-acc:gjKNOD7FD6SaBYJM2mt8gCOjDUEXdBmEUXMswMI4T8zkLobfEhfPI29q4AVp2ae05hofX6pEM5H38oEzZ69iyA==@duongnq9-project2-cosmosdb-acc.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@duongnq9-project2-cosmosdb-acc@"  # TODO: Update with appropriate MongoDB connection information
            client = pymongo.MongoClient(url)
            database = client['duongnq9-project2-mongodb']
            collection = database['advertisements']

            rec_id1 = collection.insert_one(eval(request))

            return func.HttpResponse(req.get_body())

        except ValueError:
            print("could not connect to mongodb")
            return func.HttpResponse('Could not connect to mongodb', status_code=500)

    else:
        return func.HttpResponse(
            "Please pass name in the body",
            status_code=400
        )