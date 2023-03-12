from orm import BaseManager, BaseModel


class FileModel(BaseModel):
    manager_class = BaseManager
    table_name = "files"
