from datetime import datetime
from sqlalchemy import MetaData, Integer, String, TIMESTAMP, ForeignKey, Table, Column

metadata = MetaData()

users = Table(
    'users',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('phone', String, nullable=False),
    Column('name', String, nullable=False),
    Column('surname', String, nullable=False),
    Column('password', String, nullable=False),
    Column('image', String, nullable=False),
    Column('created_at', TIMESTAMP, default=datetime.utcnow)

)