class File:
    def __init__(self, name, content=[]):
        self.name = name
        self.content = content

    def commit(self):
        with open(f'files/text/{self.name}.txt', 'w') as file:
            content = ''.join(self.content)
            file.write(content)
        pass

    def read(self):
        pass

    def uniq_together(self):
        pass


class TextFile(File):
    def __init__(self, name, content):
        self._format = ".txt"
        super().__init__(name, content)
