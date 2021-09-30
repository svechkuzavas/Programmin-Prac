from FileManager import FileManager
from config import *

fm = FileManager(USER_STORAGE, 'kirill')
fm.make_dir('1')
fm.make_dir('2')
fm.make_dir('3')
fm.make_dir('4')
fm.change_dir('3')
fm.create_empty_file('note')
fm.move_file(os.path.join(os.getcwd(),'note'), '/home/kirill/PycharmProjects/FileManager/storage/kirill/4')
print(fm)