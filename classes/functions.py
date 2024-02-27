import json, os


def get_json_file():
    """Get json list format"""
    path_for_file = os.path.join('source', 'operations.json')
    with open(path_for_file, mode='r', encoding='utf-8') as f:
        file = json.load(f)
    return file
