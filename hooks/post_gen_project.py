import os
import shutil

print(os.getcwd())  # prints /absolute/path/to/{{cookiecutter.project_slug}}

def remove(filepath):
    if os.path.isfile(filepath):
        os.remove(filepath)
    elif os.path.isdir(filepath):
        shutil.rmtree(filepath)

create_docker_file = '{{cookiecutter.create_docker_file}}' ==  'yes'


if not create_docker_file:
    # remove top-level file inside the generated folder
    remove('Dockerfile')
