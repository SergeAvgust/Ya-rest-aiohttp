from sqlalchemy import MetaData

convention = {
    'all_column_names': lambda constraint, table: '_'.join([
        column.name for column in constraint.columns.values()
    ]),
    # index
    "ix": "ix_%(table_name)s_%(all_column_names)s",
    # unique index
    "uq": "uq_%(table_name)s_%(all_column_names)s",
    # CHECK-constraint
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    # foreign key
    "fk": "fk_%(table_name)s_%(all_column_names)s_%(referred_table_name)s",
    # primary key
    "pk": "pk_%(table_name)s"
}
metadata = MetaData(naming_convention=convention)

from enum import Enum, unique

@unique
class Gender(Enum):
    male = 'male'
    female = 'female'

from sqlalchemy import (
    Column, Date, Enum as PgEnum, ForeignKey, ForeignKeyConstraint, Integer,
    String, Table
)

imports_table = Table(
    'imports',
    metadata,
    Column('import_id', Integer, primary_key=True)
)
citizens_table = Table(
    'citizens',
    metadata,
    Column('import_id', Integer, ForeignKey('imports.import_id'), primary_key=True),
    Column('citizen_id', Integer, primary_key=True),
    Column('town', String, nullable=False),
    Column('street', String, nullable=False),
    Column('building', String, nullable=False),
    Column('apartment', Integer, nullable=False),
    Column('name', String, nullable=False),
    Column('birth_datr', Date, nullable=False),
    Column('gender', PgEnum(Gender, name='gender'), nullable=False),
)
relations_table = Table(
    'relations',
    metadata,
    Column('import_id', Integer, primary_key=True),
    Column('citizen_id', Integer, primary_key=True),
    Column('relative_id', Integer, primary_key=True),
    ForeignKeyConstraint(
        ('import_id', 'citizen_id'),
        ('citizens.import_id', 'citizens.citizen_id')
    ),
    ForeignKeyConstraint(
        ('import_id', 'relative_id'),
        ('citizens.import_id', 'citizens.citizen_id')
    ),
)