import random
import string
import sys
from datetime import datetime
from pathlib import Path

# BASE_DIR = Path(__file__).resolve().parent.parent
# print(BASE_DIR)
# sys.path.append('/Users/MyPc/Desktop/master/oop/files manager')
# sys.path.append('../')
from models import FileModel


class File:
    def __init__(self, name=None, content=[]):
        self.name = name or default_name()
        self.content = content

    def commit(self):
        with open(self.path, "w") as file:
            now = datetime.now()
            self.content.append("\n\n\n{0:%Y-%m-%d %I:%M%p}".format(now))
            content = "".join(self.content)
            file.write(content)
            file.close()
            FileModel.objects.bulk_insert(
                [
                    {'name':self.name ,'format':self.format ,'timestamp':now}
                ]
            )

    def read(self):
        with open(self.path, "r") as file:
            print(file.read())
            file.close()

    def uniq_together(self):
        pass

    @property
    def path(self):
        return "files/{0}/{1}.{0}".format(self.format, self.name)


class TextFile(File):
    format = "txt"

    def __init__(self, name, content):
        super().__init__(name, content)


def default_name(length=8):
    name = [
        *list(string.ascii_lowercase),
        *list(string.ascii_uppercase),
        *list(string.digits)
    ]
    random.shuffle(name)
    return ''.join(name[:length])
    
