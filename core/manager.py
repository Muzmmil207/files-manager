from base import TextFile
import sys

class FileManager:
    files_types = {"text": TextFile}

    def __init__(self):
        self._files_data = []

    def search_files(self, format=None):
        self.run()

    def display_all_files(self):
        for file in self.files_data:
            print(file)
            self.run()

    def new_file(self):
        print("For save type SAVE() for close CLOSE()")
        print("================================================")
        content = []
        format = input("chose save format ({}) ".format(", ".join(self.files_types.keys())))
        while line := input("_ "):
            if line == "SAVE()":
                file_name = input("Enter a name or lave it empty for default: ")
                new = self.files_types[format](name=file_name, content=content)
                new.commit()
                new.read()
                self.files_data.append(new)
                input()
                break
            elif line == "CLOSE()":
                break

            content.append(line + "\n")
        self.run()

    def run(self):
        print(
            "for new file => n\nfor displaying all files => d\nfor search files => s\nfor exit => e"
        )
        print("================================================")
        option = input('> ').lower()
        if option == 'n':
            self.new_file()
        elif option == 'd':
            self.display_all_files()
        elif option == 's':
            self.search_files()
        elif option == 'e':
            sys.exit()
        else:
            self.run()


    @property
    def files_data(self):
        if not self._files_data.__len__() == 0:
            print("Retrieving The Data...")
            self._files_data = []
        return self._files_data

if __name__ == '__main__':
    FileManager().run()
