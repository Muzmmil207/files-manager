from base import TextFile


class FileManager:
    files_types = {"text": TextFile}
    
    def __init__(self) -> None:
        self._files_data = []

    def search_files(self, format=None):
        pass

    def display_all_files(self):
        for file in self.files_data:
            print(file)

    def new_file(self):
        print("For save type SAVE() for close CLOSE()")
        print("================")
        content = []
        format = input("chose save format ({}) ".format(", ".join(self.files_types.keys())))
        while line := input():
            if line == "SAVE()":
                file_name = input('Enter a name or lave it empty for default\n:')
                self.files_data.append(self.files_types[format](name=file_name,content=content))
                print(self.files_data[0].name)
                break
            elif line == "CLOSE()":
                self.run()
                break
            content.append(line + "\n")

    def save_file():
        return

    @property
    def files_data(self):
        if not self._files_data:
            print("Retrieving The Data...")
            self._files_data = []
        return self._files_data

FileManager().new_file()
