from orm import BaseModel,BaseManager

class File(BaseModel):
    manager_class = BaseManager
    table_name = "files"
