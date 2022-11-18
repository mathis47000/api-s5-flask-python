
from androwing.database import db_session
from androwing.models import Training, Feeling, User

u = User.query.get(1)

t = Training("title2", 1234, 1234, Feeling.BAD)

u.trainings.append(t)
db_session.add(u)
db_session.add(t)

db_session.commit()