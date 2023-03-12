import sys

from base import TextFile
from models import FileModel


class FileManager:
    files_types = {"txt": TextFile}

    def __init__(self):
        self._files_data = []

    def search_files(self, format=None):
        search_query = input("Enter the file name")
        for file in self.files_data:
            if file.name == search_query:
                self.files_types[file.format](file.name, []).read()
        input("\n")
        self.run()

    def display_files(self):
        for index, file in enumerate(self.files_data):
            print("{}: {}.{}".format(index + 1, file.name, file.format))
        input("\n")
        self.run()

    def new_file(self):
        print("For save type SAVE() for close CLOSE()")
        print("================================================")
        content = []
        format = input("chose save format ({}) ".format(", ".join(self.files_types.keys()))).lower()
        while line := input("_ "):
            if line == "SAVE()":
                file_name = input("Enter a name or lave it empty for default: ")
                new = self.files_types[format](name=file_name, content=content)
                new.commit()
                self.files_data.append(new)
                new.read()
                input()
                break
            elif line == "CLOSE()":
                break

            content.append(line + "\n")
        self.run()

    def run(self):
        print(
            """
            ===== Files Manager =====
            for new file => n
            for displaying all files => d
            for search files => s
            for exit => e
        """
        )
        option = input("> ").lower()
        if option == "n":
            self.new_file()
        elif option == "d":
            self.display_files()
        elif option == "s":
            self.search_files()
        elif option == "e":
            sys.exit()
        else:
            self.run()

    @property
    def files_data(self):
        if self._files_data.__len__() == 0:
            print("Retrieving The Data...")
            self._files_data = FileModel.objects.select(
                [
                    "name",
                    "timestamp",
                    "format",
                ]
            )
        return self._files_data


if __name__ == "__main__":
    FileManager().run()
