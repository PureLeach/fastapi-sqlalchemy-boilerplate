from project.core.base_classes.base_model import ProjectBaseModel
from project.core.base_classes.base_model import AwareDatetime

from project.core.base_classes.base_model import PositiveInt32, ConstrainedName


class UserCreateRequest(ProjectBaseModel):
    name: ConstrainedName


class UserResponse(ProjectBaseModel):
    id: int
    name: str
    created_at: AwareDatetime
    updated_at: AwareDatetime
    deleted: bool
