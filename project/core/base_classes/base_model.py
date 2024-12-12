from pathlib import Path as FilePath
from typing import Annotated, Any

from fastapi import Form, HTTPException, Path, Query
from humps import camelize
from pydantic import (
    AnyUrl,
    BaseModel,
    BeforeValidator,
    ConfigDict,
    Field,
    SerializerFunctionWrapHandler,
    field_validator,
    model_serializer,
)
from pydantic import AwareDatetime as AwareDatetimeOriginal
import json
import logging
from datetime import datetime
from decimal import ROUND_FLOOR, ROUND_HALF_UP, Decimal
from typing import Generator, Optional, Sequence, TypeVar
from pydantic import BaseModel, Field
from typing import Annotated

from sqlalchemy.dialects import postgresql
from sqlalchemy.sql import Join, Select



class ProjectBaseModel(BaseModel):
    model_config = ConfigDict(
        alias_generator=camelize,
        populate_by_name=True,
        str_strip_whitespace=True,
        validate_assignment=True,
    )

def fix_postgres_datetime(v: str | datetime) -> str | datetime:
    """
    Workaround for https://github.com/pydantic/pydantic/issues/6576
    """
    if isinstance(v, str) and '+' in v:
        dt, tz = v.split('+')
        if len(tz) == 2:
            return f'{dt}+{tz}00'
    return v





PositiveInt32 = Annotated[int, Field(gt=0, le=2_147_483_647)]

ConstrainedName = Annotated[str, Field(max_length=256)]

AwareDatetime = Annotated[AwareDatetimeOriginal, BeforeValidator(fix_postgres_datetime)]