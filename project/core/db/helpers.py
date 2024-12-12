import json
from typing import Any
from sqlalchemy import MetaData


metadata = MetaData(
    naming_convention={
        'ix': 'ix_%(column_0_label)s',
        'uq': 'uq_%(table_name)s_%(column_0_name)s',
        'ck': 'ck_%(table_name)s_%(constraint_name)s',
        'fk': 'fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s',
        'pk': 'pk_%(table_name)s',
    }
)


async def connection_init(connection: Any) -> None:
    # Enable JSON -> dict conversion:
    # https://github.com/encode/databases/issues/138
    # https://magicstack.github.io/asyncpg/current/usage.html#example-automatic-json-conversion
    # https://github.com/encode/databases/issues/143
    await connection.set_type_codec(
        'json',
        encoder=lambda x: x,  # dict -> JSON conversion is done by SQLAlchemy
        decoder=json.loads,
        schema='pg_catalog',
    )


def external_field(ref: str) -> dict[str, str]:
    return {'external': ref}


def exported_field() -> dict[str, bool]:
    return {'exported': True}