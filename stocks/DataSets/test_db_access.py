from sqlalchemy import create_engine
from sqlalchemy import Table, MetaData
engine = create_engine('sqlite:///tick_data.db', echo=True)

#print(engine.execute("SELECT * FROM tick_data WHERE `symbol` == 'A'").fetchall()[:10])

meta = MetaData()

tick_data_db = Table('tick_data', meta, autoload=True, autoload_with=engine)

print([c.name for c in tick_data_db.columns])
print([c.type for c in tick_data_db.columns])


'''
from sqlalchemy.orm import sessionmaker
session = sessionmaker()
session.configure(bind=engine)
Base.metadata.create_all(engine)4'''