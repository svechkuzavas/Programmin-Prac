import os
import shutil


class FileManager:
    def __init__(self, root_path, root_name):
        self.__root_path = root_path
        self.__root_name = root_name
        self._initialize_dir()

    def _initialize_dir(self):
        os.chdir(self.__root_path)
        try:
            os.mkdir(self.__root_name)
        except FileExistsError as e:
            print(f"{os.getcwd()+self.__root_name} already exists")
        finally:
            os.chdir(self.__root_name)

    def _get_absolute_path(self, child):
        return os.path.join(os.getcwd(), child)

    def make_dir(self, dir_name):
        dir_path = self._get_absolute_path(dir_name)
        if not os.path.exists(dir_name):
            os.mkdir(dir_path)
        else:
            print(f"Directory already exists: {dir_path}")

    def remove_dir(self, dir_name):
        dir_path = self._get_absolute_path(dir_name)
        try:
            if len(os.listdir(dir_path)) == 0 and os.path.isdir(dir_path):
                os.rmdir(dir_path)
                print(f"Empty directory removed: {dir_path}")
        except FileNotFoundError as e:
            print(f"Not found directory: {dir_path}")

    def change_dir(self, dir_name=None, parent=False):
        if parent and dir_name is None:
            os.chdir(os.path.split(os.getcwd())[0])
        elif not parent:
            try:
                os.chdir(self._get_absolute_path(dir_name))
            except FileNotFoundError as e:
                print(f"Not found directory: {self._get_absolute_path(dir_name)}")

    def create_empty_file(self, file_name):
        if not os.path.exists(self._get_absolute_path(file_name)):
            f = open(file_name, 'w')
            f.close()
            print(f"File created: {self._get_absolute_path(file_name)}")
        else:
            print(f"File already exists: {self._get_absolute_path(file_name)}")

    def echo_to_file(self, file_name, context):
        if os.path.exists(self._get_absolute_path(file_name)):
            with open(file_name, "w") as f:
                f.write(context)
        else:
            print(f"File not exists: {self._get_absolute_path(file_name)}")

    def show_file(self, file_name):
        file_path = self._get_absolute_path(file_name)
        if os.path.exists(file_path) and os.path.isfile(file_path):
            with open(file_name, "r") as f:
                for line in f.readlines():
                    print(line, end='')
        else:
            print(f"File not exists: {file_path}")

    def remove_file(self, file_name):
        file_path = self._get_absolute_path(file_name)
        if os.path.exists(file_path) and os.path.isfile(file_path):
            os.remove(file_path)
        else:
            print(f"File not exists: {file_path}")

    def rename_file(self, file_name, new_name):
        file_path = self._get_absolute_path(file_name)
        if os.path.exists(file_path) and os.path.isfile(file_path):
            os.rename(file_path, self._get_absolute_path(new_name))
        else:
            print(f"File not exists: {file_path}")

    def copy_file(self, file_path, dest_path):
        if os.path.exists(file_path) and os.path.exists(dest_path):
            shutil.copy(file_path, dest_path)
        elif not os.path.exists(file_path):
            print(f"File not exists: {file_path}")
        elif not os.path.exists(dest_path):
            print(f"File not exists: {dest_path}")

    def move_file(self, file_path, dest_path):
        if os.path.exists(file_path) and os.path.exists(dest_path):
            shutil.move(file_path, dest_path)
        elif not os.path.exists(file_path):
            print(f"File not exists: {file_path}")
        elif not os.path.exists(dest_path):
            print(f"File not exists: {dest_path}")

    def __str__(self):
        return f"Current directory: {os.getcwd()}\nRoot directory: {self.__root_path}/{self.__root_name}"


