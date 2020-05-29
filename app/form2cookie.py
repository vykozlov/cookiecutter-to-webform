from cookiecutter.main import cookiecutter
import os
import shutil
import json

def read_json():
    f = open('app/files/cookiecutter.json', "r")
    # Reading from file
    data = json.loads(f.read())
    data_vals = []
    for key, value in data.items():
        data_vals.append([key,value])
    return data_vals


def call_cookiecutter(form):
    with open('app/files/cookiecutter.json', 'r') as file:
        json_data = json.load(file)
        for key, value in form.items():
            if value!= "" and key != "submit":
                if key == "repo_name":
                    name_rep = json_data["project_name"].lower().replace(' ', '_').replace('-','_')
                    json_data[key] = name_rep
                else:
                    json_data[key] = value

    # create a temp directory
    owd_parent = os.getcwd()
    os.mkdir('Deep_Project')
    # switch to that temp directory
    os.chdir('Deep_Project')
    owd_child = os.getcwd()
    # call cookiecutter
    print(json_data)
    cookiecutter('https://github.com/indigo-dc/cookiecutter-data-science', no_input=True, extra_context=json_data)
    os.chdir(owd_parent)
    zip_name = 'deep_project'
    shutil.make_archive('deep_project', 'zip', 'Deep_Project')
    shutil.rmtree(owd_child)



