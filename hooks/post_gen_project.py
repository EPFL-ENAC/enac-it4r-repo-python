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


value_create_doc = '{{cookiecutter.create_documentation}}'

if value_create_doc == 'no':
    # remove top-level file inside the generated folder
    remove('docs')
    remove('_config.yml')
    remove('readthedocs.yml')
elif value_create_doc == 'yes, with readthedocs':
    remove('_config.yml')
elif value_create_doc == 'yes, with GitHub Pages site with Jekyll':
    remove('docs')
    remove('readthedocs.yml')

create_jupyter_notebook = '{{cookiecutter.create_jupyter_notebook}}' ==  'yes'

if not create_jupyter_notebook:
    # remove top-level file inside the generated folder
    path_folder = os.path.join(os.getcwd(),'{{cookiecutter.project_slug}}','notebooks')
    remove(path_folder)
