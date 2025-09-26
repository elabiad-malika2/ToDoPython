from sqlalchemy import Column, Table, Integer, VARCHAR, MetaData, Enum, text
from Package.connection import get_connection

engine = get_connection()
meta = MetaData()
print(engine)

taches = Table(
    'taches', meta,
    Column('id', Integer, primary_key=True),
    Column('contenu', VARCHAR, nullable=False),
    Column('status', Enum('En cours', 'Terminée', name='status_enum')),
    Column('priorite', Enum('High', 'Low', 'Medium', name='priorite_enum'))
)
meta.create_all(engine)
