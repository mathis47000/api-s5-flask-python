from flask import Blueprint, request, abort
from androwing.database import db_session
from androwing.models import Training, User


bp = Blueprint('training', __name__, url_prefix='/training')

#get all training
@bp.route('/all',methods=['GET'])
def get_all_training():
    list = Training.query.all()
    return [t.to_dict() for t in list]


#return json training with id parameter
#if id don't exist raise error 404
@bp.route('/<int:id>',methods=['GET'])
def get_by_id_training(id):
    t = Training.query.get(id)
    #to_dict = get json from object
    return t.to_dict() if t else abort(404)
    
@bp.route('/add/<int:user_id>',methods=['POST','GET'])
def add_training(user_id):
    try:
        title = request.form['title']
        distance = request.form['distance']
        duration = request.form['duration']
        feeling = request.form['feeling']
        t = Training(title, distance, duration, feeling)
        u = User.query.get(user_id)
        '' if u else abort(404)
        u.trainings.append(t)
    except:
        abort(400)
    try:
        db_session.add(t)
        db_session.commit()
    except:
        abort(500)
    return t.to_dict(), 201


@bp.route('/update/<int:id>',methods=['PUT','GET'])
def update_training(id):
    t = Training.query.get(id)
    '' if t else abort(404)
    try:
        title = request.form['title']
        distance = request.form['distance']
        duration = request.form['duration']
        feeling = request.form['feeling']
        t.title = title
        t.distance = distance
        t.duration = duration
        t.feeling = feeling
    except:
        abort(400)
    try:
        db_session.commit()
    except:
        abort(500)
   
    return t.to_dict()

@bp.route('/delete/<int:id>',methods=['DELETE','GET'])
def delete_training(id):
    t = Training.query.get(id)
    '' if t else abort(404)
    try:
        db_session.delete(t)
        db_session.commit()
    except:
        abort(500)
    return t.to_dict()

