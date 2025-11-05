from flask import Flask, request
app = Flask(__name__)

specializations = [
    {
    "name": "IT",
    "course_items": [{
    "name": "Web Services",
    "type": "Mandatory",
    }],}
]

@app.get('/specialization')
def get_specializations():
    return {"specialization": specializations}

    
@app.post('/specialization')
def create_specialization():
    request_data = request.get_json()
    new_specialization = {
        "name": request_data['name'],
        "course_items": []
    }
    specializations.append(new_specialization)
    return new_specialization, 201


    
@app.post('/specialization/<string:name>/course_item')
def create_course_item(name):
    request_data = request.get_json()
    
    for spec in specializations:
        if spec['name'] == name:
            new_course_item = {
                "name": request_data['name'],
                "type": request_data['type']
            }
            spec['course_items'].append(new_course_item)
            return new_course_item, 201 
    
    return {"message": "Specialization not found"}, 404 



@app.get('/specialization/<string:name>')
def get_specialization(name):
    for spec in specializations:
        if spec['name'] == name:
            return {"specialization": spec}
    return {"message": "Specialization not found"}



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
