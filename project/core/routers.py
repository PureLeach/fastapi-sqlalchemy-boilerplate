import os
import importlib.util
from fastapi import FastAPI, APIRouter
from importlib.machinery import ModuleSpec
from typing import Optional
import pathlib
from project.config.base import settings


logger = settings.LOGGER.getChild('register_routers')


def register_routers(app: FastAPI):
    """Основная функция для обхода модулей и регистрации роутеров."""
    
    logger.debug('Регистрация роутеров')
    modules_directory = str(pathlib.Path(__file__).parent.parent / 'modules')
    for root, dirs, files in os.walk(modules_directory):
        for file in files:
            if file.endswith(".py"):
                module_path = os.path.join(root, file)
                module_name = os.path.splitext(file)[0]

                # Получаем спецификацию модуля
                spec = get_module_spec(module_path, module_name)
                if spec is not None:
                    # Загружаем и выполняем модуль
                    module = load_module(spec)
                    if module is not None:
                        # Регистрируем роутеры модуля
                        register_module_routers(app, module)
                    else:
                        logger.error(f"Не удалось загрузить модуль {module_name} из {module_path}")
                else:
                    logger.error(f"Не удалось найти спецификацию для модуля {module_name} из {module_path}")


def get_module_spec(module_path: str, module_name: str) -> Optional[ModuleSpec]:
    """Получение спецификации модуля по пути и имени."""
    return importlib.util.spec_from_file_location(module_name, module_path)


def load_module(spec: ModuleSpec) -> Optional[object]:
    """Загрузка и выполнение модуля."""
    if spec.loader is not None:
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module
    return None


def register_module_routers(app: FastAPI, module: object):
    """Регистрация роутеров, найденных в модуле."""
    for item_name in dir(module):
        item = getattr(module, item_name)
        if isinstance(item, APIRouter):
            app.include_router(item)


