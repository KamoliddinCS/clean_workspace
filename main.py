try:
    import os
    import shutil
    import locale
except ModuleNotFoundError:
    print("\033[1;31;40m Some requirements are missing!\n\nRun \"pip install -r requirements.txt\"")

os_lang, n = locale.getdefaultlocale()
source = f"C:/Users/{os.environ.get('USERNAME')}/Desktop/"
if os_lang[:2] == "en":
    source = f"C:/Users/{os.environ.get('USERNAME')}/Desktop/"
elif os_lang[:2] == "ru":
    source = f"C:/Пользователи/{os.environ.get('USERNAME')}/Рабочий стол/"

items = os.listdir(source)

def create_dir(path, ext):
    """ Creates a directory in a given path with an extension name """
    try:
        os.mkdir(f"{path}/{ext.title()} Files")
    except FileExistsError:
        pass
    return f"{ext.title()} Files"

# print(items)

for i in items:
    elem, extension = os.path.splitext(f"C:/Users/User/Desktop/{i}")
    if not os.path.isdir(f"C:/Users/User/Desktop/{i}"):
        shutil.move(source + i, f"{source}/{create_dir(source, extension)}")

