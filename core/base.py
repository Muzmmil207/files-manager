from datetime import datetime


class File:
    def __init__(self, name=None, content=[]):
        self.name = name
        self.content = content

    def commit(self):
        with open(self.path, "w") as file:
            self.content.append("\n\n\n{0:%Y-%m-%d %I:%M%p}".format(datetime.now()))
            content = "".join(self.content)
            file.write(content)
            file.close()

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
