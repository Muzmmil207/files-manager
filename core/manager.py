import sys

from base import TextFile
from models import FileModel


class FileManager:
    files_types = {"txt": TextFile}
    file_model = FileModel

    def __init__(self):
        self._files_data = []

    def search(self, filter):        
        return [file for file in self.files_data if filter in file.name]

    def display_files(self):
        return self.files_data

    def new_file(self):
        print("For save type SAVE() for close CLOSE()")
        print("================================================")
        content = []
        format = input("chose save format ({}) ".format(", ".join(self.files_types.keys()))).lower()
        new = self.files_types.get(format)
        if new:
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
        else:
            print('This format dose note  exist')

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
            self._files_data = self.file_model.objects.select(
                [
                    "name",
                    "timestamp",
                    "format",
                ]
            )
        return self._files_data


class Menu:
    '''Display a menu and respond to choices when run.'''
    
    def __init__(self):
        self.manager = FileManager()
        self.choices = {
        "1": self.show_files,
        "2": self.search_files,
        "3": self.add_file,
        "4": self.modify_file,
        "5": self.quit
        }
    
    def display_menu(self):
        print("""
        File Manager Menu
        1. Show all files
        2. Search files
        3. Add file
        4. Modify file
        5. Quit
        """)
    
    def run(self):
        '''Display the menu and respond to choices.'''
        while True:
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))
    
    def show_files(self, files=None):
        if not files:
            files = self.manager.display_files()

        for index, file in enumerate(files):
            print("{}: {}.{}".format(index + 1, file.name, file.format))
        input()
    
    def search_files(self):
        filter = input("Search for: ")
        files = self.manager.search(filter)
        self.show_files(files)

    def add_file(self):
        self.manager.new_file()
        print("Your file has been added.")
    
    
    def quit(self):
        print("Thank you for using your File Manager today.")
        sys.exit(0)



if __name__ == "__main__":
    Menu().run()

