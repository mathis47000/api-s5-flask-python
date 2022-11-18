from flask import Blueprint, request, abort
from androwing.database import db_session
from androwing.models import User

bp = Blueprint('user', __name__, url_prefix='/user')

#get all training
@bp.route('/all',methods=['GET'])
def get_all_user():
    list = User.query.all()
    return [u.to_dict() for u in list]

@bp.route('/delete/<int:id>',methods=['DELETE','GET'])
def delete_user(id):
    u = User.query.get(id)
    '' if u else abort(404)
    try:
        db_session.delete(u)
        db_session.commit()
    except:
        abort(500)
    return u.to_dict()