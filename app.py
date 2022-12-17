from flask import Flask, request, jsonify

app= Flask(__name__)

datas=[
    {
        "id":1,
        "Name":"Raju",
        "Contact":"9987644456",
        "done":False,
    },
    {
        "id":2,
        "Name":"Rahul",
        "Contact":"9876543222",
        "done":False
    }
]

@app.route("/add-data",methods=["POST"])

def add_task():
    if not request.json:
        return jsonify({
           "status":"error",
           "message":"please enter valid data" 
        },400)
    data={
        "id":datas[-1]["id"],
        "Name":request.json["Name"],
        "Contact":request.json.get("Contact",""),
        "done":False
    }
    datas.append(data)
    return jsonify({
        "status":"success",
        "message":"data added successfully"
    })

@app.route("/")

def get_task():
    return jsonify({
        "data":datas
    })

if (__name__=="__main__"):
    app.run(debug=True)