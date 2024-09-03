import os.path

def get_yaml_path(file):
    base_path = os.path.dirname(__file__)
    file_path = os.path.join(base_path, "../data/{}".format(file))
    return file_path