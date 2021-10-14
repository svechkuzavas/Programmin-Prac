import os
import shutil


class FileManager:
    def __init__(self, root_path, root_name):
        self.__root_path = root_path
        self.__root_name = root_name
        self._initialize_dir()
        self.current_dir = root_name

    def _initialize_dir(self):
        os.chdir(self.__root_path)
        try:
            os.mkdir(self.__root_name)
        except FileExistsError as e:
            print(f"[file manager] найдена ваша директория, переходим...")
        finally:
            os.chdir(self.__root_name)

    def _get_absolute_path(self, child):
        return os.path.join(os.getcwd(), child)

    def get_wd(self):
        return self.current_dir

    def make_dir(self, args):
        dir_name = args[0]
        dir_path = self._get_absolute_path(dir_name)
        if not os.path.exists(dir_name):
            os.mkdir(dir_path)
        else:
            print(f"Directory already exists: {dir_path}")

    def remove_dir(self, args):
        dir_name = args[0]
        dir_path = self._get_absolute_path(dir_name)
        try:
            if len(os.listdir(dir_path)) == 0 and os.path.isdir(dir_path):
                os.rmdir(dir_path)
                print(f"Empty directory removed: {dir_path}")
        except FileNotFoundError as e:
            print(f"Not found directory: {dir_path}")

    def change_dir(self, args):
        dir_name = None if args[0] == '..' else args[0]
        if dir_name is None and not self.current_dir == self.__root_name:
            os.chdir(os.path.split(os.getcwd())[0])
            self.current_dir = os.path.split(self.current_dir)[0]
        elif dir_name is None and self.current_dir == self.__root_name:
            print('Вы в своей корневой директории')
        else:
            try:
                os.chdir(self._get_absolute_path(dir_name))
                self.current_dir = os.path.join(self.current_dir, dir_name)
            except FileNotFoundError as e:
                print(f"Not found directory: {self._get_absolute_path(dir_name)}")

    def create_empty_file(self, args):
        file_name = args[0]
        if not os.path.exists(self._get_absolute_path(file_name)):
            f = open(file_name, 'w')
            f.close()
            print(f"File created: {self._get_absolute_path(file_name)}")
        else:
            print(f"File already exists: {self._get_absolute_path(file_name)}")

    def echo_to_file(self, args):
        file_name, context = args[0], args[1]
        if os.path.exists(self._get_absolute_path(file_name)):
            with open(file_name, "w") as f:
                f.write(context)
        else:
            print(f"File not exists: {self._get_absolute_path(file_name)}")

    def show_file(self, args):
        file_name = args[0]
        file_path = self._get_absolute_path(file_name)
        if os.path.exists(file_path) and os.path.isfile(file_path):
            print("Соедержимое файла: ")
            with open(file_name, "r") as f:
                for line in f.readlines():
                    print(line, end='')
            print('\n')
        else:
            print(f"File not exists: {file_path}")

    def remove_file(self, args):
        file_name = args[0]
        file_path = self._get_absolute_path(file_name)
        if os.path.exists(file_path) and os.path.isfile(file_path):
            os.remove(file_path)
            print(f"File removed")
        else:
            print(f"File not exists: {file_path}")

    def rename_file(self, args):
        file_name, new_name = args[0], args[1]
        file_path = self._get_absolute_path(file_name)
        if os.path.exists(file_path) and os.path.isfile(file_path):
            os.rename(file_path, self._get_absolute_path(new_name))
        else:
            print(f"File not exists: {file_path}")

    def copy_file(self, args):
        file_path, dest_path = args[0], args[1]
        file_path = os.path.join(self.__root_path, self.__root_name, file_path)
        dest_path = os.path.join(self.__root_path, self.__root_name, dest_path)
        if os.path.exists(file_path) and os.path.exists(dest_path):
            shutil.copy(file_path, dest_path)
        elif not os.path.exists(file_path):
            print(f"File not exists: {file_path}")
        elif not os.path.exists(dest_path):
            print(f"File not exists: {dest_path}")

    def move_file(self, args):
        file_path, dest_path = args[0], args[1]
        file_path = os.path.join(self.__root_path, self.__root_name, file_path)
        dest_path = os.path.join(self.__root_path, self.__root_name, dest_path)
        if os.path.exists(file_path) and os.path.exists(dest_path):
            shutil.move(file_path, dest_path)
        elif not os.path.exists(file_path):
            print(f"File not exists: {file_path}")
        elif not os.path.exists(dest_path):
            print(f"File not exists: {dest_path}")

    def execute_command(self, n):
        commands = {
            '0': (self.get_wd, ''),
            '1': (self.make_dir, 'Введите имя новой папки: '),
            '2': (self.remove_dir, 'Введите имя удаляемой папки: '),
            '3': (self.change_dir, 'Введите имя папки назначения: '),
            '4': (self.create_empty_file, 'Введите имя нового файла: '),
            '5': (self.echo_to_file, 'Введите имя файла и текст(через пробел): '),
            '6': (self.show_file, 'Введите имя файла: '),
            '7': (self.remove_file, 'Введите имя файла: '),
            '8': (self.copy_file, 'Введите имя файла и имя файла назначения: '),
            '9': (self.move_file, 'Введите имя файла и имя файла назначения: '),
            '10': (self.rename_file, 'Введите имя файла и новое имя файла: ')
        }
        if n in commands.keys():
            if n != '0':
                args = input(f"[file manager] {commands.get(n)[1]}").split(' ')
                commands.get(n)[0](args)
            else:
                print(f"[file manager] {commands.get(n)[0]()}")

    def __str__(self):
        return f"Current directory: {os.getcwd()}\nRoot directory: {self.__root_path}/{self.__root_name}"


