from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#change url here for production
#dialect://username:password@host:port/database
engine = create_engine('mysql://root:@localhost/androwing')
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db(): 
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    import androwing.models
    #drop all just for debug mode
    #prefere migration to init in production
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)