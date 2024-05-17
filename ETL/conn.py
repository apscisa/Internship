from sqlalchemy import create_engine


def conn(URL):
    engine = create_engine(URL)
    return engine.connect()