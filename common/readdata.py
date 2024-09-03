import yaml
import configparser
import csv

def readYaml(yaml_file):
    with open(yaml_file, 'r', encoding='utf-8') as f:
        yaml_data = yaml.safe_load(f)
        return yaml_data

def readIni(ini_file):
    # 创建一个ConfigParser对象
    config = configparser.ConfigParser()
    # 读取INI文件
    ini_data = config.read(ini_file)
    return ini_data



def readCsv(csv_file):
    csv_data = []
    with open(csv_file, mode='r', encoding='utf-8') as file:
        # 创建CSV字典读取器
        csv_reader = csv.DictReader(file)

        # 逐行读取数据
        for row in csv_reader:
            # 每一行数据作为一个字典
            csv_data.append(row)
    return csv_data