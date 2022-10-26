import os

def create_dir(app_name):
  try:
    os.mkdir(app_name)
  except FileExistsError:
    print('Directory already exists: ' + app_name)

# create app.py in directory 'app_name'
def create_app(app_name):
    app_py_file = open(app_name + "/app.py", "w+")
    app_py = """
import npyscreen

def myFunction(*args):
    pass

if __name__ == '__main__':
    npyscreen.wrapper_basic(myFunction)
    print("This is your first application!")

"""
    app_py_file.writelines([app_py])
    app_py_file.close()

a=input("アプリケーション名を入力してください。:")
create_dir(a)
create_app(a)
