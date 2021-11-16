from flask import Flask, render_template, request
import pymongo

connection = pymongo.MongoClient('mongodb://localhost:27017/')
db = connection.get_database("testDB")

app = Flask(__name__)


@app.route("/", methods=["GET","POST"])
def intro():
    if request.method == "GET":
        return render_template("sign_up.html")
    else:
        id = request.form.get("user_id")
        pw = request.form.get("password")
        collection = db.get_collection("TESTCOL")
        collection.insert_one({"component":id,"path":pw})
        return print(list(collection.find()))
        
        


if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)
