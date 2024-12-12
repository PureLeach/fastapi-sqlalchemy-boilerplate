from sqlalchemy import (
    ARRAY,
    Boolean,
    Column,
    DateTime,
    Enum,
    ForeignKey,
    Index,
    Integer,
    String,
    Table,
    func,
    literal_column,
)

from project.core.helpers.db import exported_field
from project.core.db_connection import metadata


users = Table(
    'users',
    metadata,
    Column('id', Integer, primary_key=True, info=exported_field()),
    Column('name', String(256), nullable=False),
    Column('created_at', DateTime(timezone=True), index=False, nullable=False, server_default=func.now()),
    Column(
        'updated_at',
        DateTime(timezone=True),
        index=True,
        nullable=False,
        server_default=func.now(),
        onupdate=func.now(),
    ),
    Column('deleted', Boolean, nullable=False, server_default='false', index=True),
)
