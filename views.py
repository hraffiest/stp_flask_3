from __init__ import app
from models import *
from flask import abort, flash, render_template, request, redirect, session, jsonify
from flask_jwt_extended import JWTManager, create_access_token

jwt = JWTManager(app)


@app.route('/auth/', methods=['POST'])
def login():
    pass
    # if not request.is_json:
    #     return jsonify({"msg": "Missing JSON in request"}), 400
    #
    # username = request.json.get("username", "")
    # password = request.json.get("password", "")
    #
    # if username != "test" or password != "test":
    #     return jsonify({"msg": "Bad username or password"}), 401
    #
    # access_token = create_access_token(identity=username)
    # return jsonify(access_token=access_token)


@app.route("/locations/", methods=["GET"])
def get_locations_list():
    pass


@app.route("/events/", methods=["GET"])
def get_locations_list():
    pass


@app.route("/enrollments/<int:eventid>", methods=["POST", "DELETE"])
def enrollments(eventid):
    if request.method == 'POST':
        pass
    pass


@app.route('/register/', methods=['POST'])
def register():
    pass


@app.route("/profile/", methods=["GET"])
def get_profile():
    pass