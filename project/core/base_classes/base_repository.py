import math
import traceback
from contextlib import asynccontextmanager
from typing import AsyncGenerator, Callable, Optional, Type, TypeVar, Union

from databases import Database
from databases.core import Transaction
from sqlalchemy import Column, Table, case, func, select
from sqlalchemy.sql import Alias, CompoundSelect, Select
from sqlalchemy.sql.elements import BooleanClauseList, Label
from sqlalchemy.sql.selectable import FromClause
from project.core.base_classes.base_model import ProjectBaseModel
from project.core.db_connection import database
from project.config.base import settings

ResponseModelType = TypeVar('ResponseModelType', bound=ProjectBaseModel)


class BaseRepository:
    def __init__(self, db: Database = database) -> None:
        self.db: Database = db
        self.logger = settings.LOGGER.getChild(self.__class__.__name__)

    @asynccontextmanager
    async def transaction(self, isolation: Optional[str] = None) -> AsyncGenerator[Transaction, None]:
        if isolation:
            current_transaction = self.db.transaction(isolation=isolation)
        else:
            current_transaction = self.db.transaction()

        try:
            yield await current_transaction.start()
        except Exception as error:
            self.logger.error(f'Transaction failed: {error}')
            self.logger.error(traceback.print_exception(error))
            await current_transaction.rollback()
            raise error
        else:
            await current_transaction.commit()
