from __init__ import app
from models import *
from flask import abort, flash, render_template, request, redirect, session, jsonify
from flask_jwt_extended import JWTManager, create_access_token

jwt = JWTManager(app)


@app.route('/auth/', methods=['POST'])
def login():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400

    username = request.json.get("username", "")
    password = request.json.get("password", "")

    user = db.session.query(Participant).filter(Participant.email == username)
    check_pass = user.password_valid(password)

    if not user or not check_pass:
        return jsonify({"msg": "Bad username or password"}), 400
    else:
        return jsonify(email=user.email, name=user.name, about=user.about, picture=user.picture)


@app.route("/locations/", methods=["GET"])
def get_locations_list():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400

    locs = db.session.query(Location).all()
    locs_dict = []
    for loc in locs:
        locs_dict.append(dict(id=loc.l_id, title=loc.title, code=loc.code))
    return jsonify(locs_dict)


@app.route("/events/", methods=["GET"])
def get_events_list():
    events = db.session.query(Event).all()
    event_type = request.args.get('eventtype')
    location = request.args.get('location')
    events_typed = db.session.query(Event).filter(Event.type == event_type).all()
    events_locs = db.session.query(Event).filter(Event.loc_id == location).all()
    events_dict = []
    if event_type and not location:
        if events_typed:
            events = events_typed
        else:
            return jsonify(), 500
    elif location and not event_type:
        if events_locs:
            events = events_locs
        else:
            return jsonify(), 500
    elif location and event_type:
        if events_locs and events_typed:
            events = db.session.query(Event).filter(db.and_(Event.loc_id == location,
                                                            Event.type == event_type))
        else:
            return jsonify(), 500
    for e in events:
        events_dict.append(dict(id=e.e_id,
                                title=e.title,
                                description=e.description,
                                date=str(e.datetime).split(' ')[0],
                                time=str(e.datetime).split(' ')[1],
                                type=e.type,
                                category=e.category,
                                address=e.address,
                                seats=e.seats,
                                location=db.session.query(Location).get(e.loc_id).title
                                ))
    return jsonify(events_dict)


@app.route("/enrollments/<int:event_id>", methods=["POST", "DELETE"])
def enrollments(event_id):
    if request.method == 'POST':
        enroll = db.session.query(Enrollment).filter(Enrollment.event_id == event_id).all()
        event = db.session.query(Event).get(event_id)
        if not enroll or len(enroll) > event.seats:
            return jsonify(status='success'), 200
        else:
            return jsonify(erorr="Not enough seats"), 400
    elif request.method == 'DELETE':
        if not request.is_json:
            return jsonify({"msg": "Missing JSON in request"}), 400
        user_id = request.args.get('user_id')
        enrolls = db.session.query(Enrollment).filter(db.and_(Enrollment.event_id == event_id,
                                                              Enrollment.part_id == user_id)).all()
        for enroll in enrolls:
            db.session.delete(enroll)
        db.session.commit()
        return jsonify(status='success')


@app.route('/register/', methods=['POST'])
def register():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400
    name = request.args.get('name')
    email = request.args.get('email')
    about = request.args.get('about')
    password = request.args.get('password')
    search_user = db.session.query(Participant).filter(Participant.email == email).first()
    if search_user:
        return jsonify(erorr='Already exist'), 400
    user = Participant(name=name,
                       email=email,
                       about=about,
                       password=password)
    db.session.add(user)
    db.session.commit()
    return jsonify(email=user.email, name=user.name, about=user.about, picture=user.picture)


@app.route("/profile/<int:u_id>", methods=["GET"])
def get_profile(u_id):
    user = db.session.query(Participant).get(u_id)
    if user:
        return jsonify(id=user.p_id,
                       name=user.name,
                       email=user.email,
                       picture=user.picture,
                       location=user.location,
                       event_id=user.event_id,
                       about=user.about
                       )
    return jsonify(), 404
