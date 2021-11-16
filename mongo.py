import pymongo

connection = pymongo.MongoClient('mongodb://localhost:27017/')
db = connection.get_database("tes")

def create_collection(coll_name):
    db.create_collection(coll_name, validator={
        '$jsonSchema': {
            'bsonType': 'object',
            'additionalProperties': True,
            'required': ['component', 'path'],
            'properties': {
                'component': {
                    'bsonType': 'string'
                },
                'path': {
                    'bsonType': 'string',
                    'description': 'Set to default value'
                }
            }
        }
    })
create_collection("TESTCOL")
collection = db.get_collection("TESTCOL")

collection.insert_many([{"component":1},{"path":2}])

print(list(collection.find()))