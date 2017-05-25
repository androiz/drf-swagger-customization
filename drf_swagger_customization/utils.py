import os
from coreapi.compat import force_bytes
from os.path import join
from django.conf import settings
import simplejson as json


def get_item_from_path(path, json):
    res = json
    for p in path:
        if p in res:
            res = res[p]
        else:
            if '=' in p:
                oper = p.split('=')
                for i, x in enumerate(res):
                    if x[oper[0]] == oper[1]:
                        res = res[i]
            else:
                raise Exception
    return res


def add_documentation(operation, swagger_doc):
    for key, value in operation.items():
        path_elements = key.split("|")
        last_element = path_elements.pop()

        path = get_item_from_path(path_elements, swagger_doc)

        if isinstance(value, list):
            if last_element not in path:
                path[last_element] = []

            for x in value:
                path[last_element].append(x)

        if isinstance(value, dict):
            path[last_element] = value


def update_documentation(operation, swagger_doc):
    for key, value in operation.items():
        path_elements = key.split("|")
        last_element = path_elements.pop()

        path = get_item_from_path(path_elements, swagger_doc)

        if '=' in last_element:
            oper = last_element.split('=')
            for i, x in enumerate(path):
                if x[oper[0]] == oper[1]:
                    path[i] = value
                    break
        else:
            path[last_element] = value


def remove_documentation(operation, swagger_doc):
    for key in operation:
        path_elements = key.split("|")
        last_element = path_elements.pop()

        path = get_item_from_path(path_elements, swagger_doc)
        if '=' in last_element:
            oper = last_element.split('=')
            for i, x in enumerate(path):
                if x[oper[0]] == oper[1]:
                    del path[i]
                    break
        else:
            del path[last_element]


def execute_action(data, swagger_doc):
    if data['action'] == 'create':
        add_documentation(data['operation'], swagger_doc)
    elif data['action'] == 'update':
        update_documentation(data['operation'], swagger_doc)
    elif data['action'] == 'delete':
        remove_documentation(data['operation'], swagger_doc)
    else:
        raise Exception


def build(path_to_file, swagger_doc):
    with open(path_to_file, 'r') as f:
        json_data = json.loads(f.read())

    for data in json_data:
        try:
            execute_action(data, swagger_doc)
        except Exception:
            pass


def append_schemas(swagger_doc):
    folder = settings.EXTERNAL_DOC_FOLDER
    files = [join(folder, f) for f in os.listdir(folder) if os.path.isfile(join(folder, f))]

    for file in files:
        with open(file, 'r') as f:
            data = json.loads(f.read())
            swagger_doc['paths'].update(data['paths'])

    build(settings.EXTENSION_PATH, swagger_doc)

    return force_bytes(json.dumps(swagger_doc))
