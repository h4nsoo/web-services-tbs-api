from flask import Flask, request, abort
from flask_smorest import Api, Blueprint
from uuid import uuid4
from db import specializations, course_items
from resources.course_item import blp as CourseItemBlueprint
from resources.specializations import blp as SpecializationBlueprint

app = Flask(__name__)

app.config["API_TITLE"] = "TBS Web Services API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist@4/"
api = Api(app)


api.register_blueprint(SpecializationBlueprint, description="Operations on specializations")
api.register_blueprint(CourseItemBlueprint, description="Operations on course_items")

"""@app.get("/specialization/<string:specialization_id>")
def get_specialization(specialization_id):
    try:
        return {"specialization": specializations[specialization_id]}
    except KeyError:
        return {"message": "Specialization not found"}, 404


@app.get('/specialization')
def get_specializations():
    return {"specialization": list(specializations.values())}

    
@app.post('/specialization')
def create_specialization():


    request_data = request.get_json()

    if "name" not in request_data:
        abort(400, message="Bad request, missing required fields")

    for spec in specializations.values():
        if spec["name"] == request_data["name"]:
            abort(400, description="Specialization already exists")

    specialization_id = uuid4().hex
    specialization = {**request_data, "id": specialization_id}
    specializations[specialization_id] = specialization
    return specialization, 201

print(specializations)
    
@app.post('/course_item')
def create_course_item():
    
    request_data = request.get_json()

    if ("type" not in request_data) or ("name" not in request_data) or ("specialization_id" not in request_data):
        abort(400, description="Bad request, missing required fields")

    for course_item in course_items.values():
        if (request_data["name"] == course_item["name"] and
            request_data["type"] == course_item["type"] and
            request_data["specialization_id"] == course_item["specialization_id"]):
            abort(400, description="Course item already exists")

    if request_data["specialization_id"] not in specializations:
        print(specializations)
        abort(404, description="Specialization not found")

    course_item_id = uuid4().hex
    course_item = {**request_data, "id": course_item_id}
    course_items[course_item_id] = course_item
    return course_item, 201


@app.get("/course_item")
def get_all_course_items():
    return {"course_items": list(course_items.values())}


@app.get("/course_item/by_specialization/<string:specialization_id>")
def get_course_items_by_specialization(specialization_id):
    current_course_items = [
        course_item for course_item in course_items.values()
        if course_item.get("specialization_id") == specialization_id
    ]

    if not current_course_items:
        abort(404, description="No course items found for this specialization")

    return {"course_items": current_course_items}, 200



@app.delete("/specialization/<string:specialization_id>")
def delete_specialization(specialization_id):
    try:
        del specializations[specialization_id]
        return {"message": "Specialization deleted"}, 200
    except KeyError:
        return {"message": "Specialization not found"}, 404
    

@app.put("/specialization/<string:specialization_id>")
def update_spececialization(specialization_id):
    request_data = request.get_json()

    if "name" not in request_data:
        abort(400, description="Bad request, missing required fields")
    
    try:
        specialization = specializations[specialization_id]
        specialization.update(request_data)
        return specialization

    except KeyError:
        return {"message": "Specialization not found"}, 404
    
    
@app.delete("/course_item/<string:course_item_id>")
def delete_course_item(course_item_id):
    try:
        del course_items[course_item_id]
        return {"message": "Course item deleted"}
    except KeyError:
        return {"message": "Course item not found"}, 404
    
@app.put("/course_item/<string:course_item_id>")
def update_course_item(course_item_id):
    request_data = request.get_json()

    if ("type" not in request_data) or ("name" not in request_data) or ("specialization_id" not in request_data):
        abort(400, description="Bad request, missing required fields")
    
    try:
        course_item = course_items[course_item_id]
        course_item.update(request_data)
        return course_item

    except KeyError:
        return {"message": "Course item not found"}, 404 """
    


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
