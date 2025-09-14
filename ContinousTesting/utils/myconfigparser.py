import configparser
from pathlib import Path

cfgFile = 'petsqa.ini'
cfgFileDir = 'config'

config = configparser.ConfigParser()
BASE_DIR = Path(__file__).resolve().parent.parent
print(BASE_DIR)
CONFIG_FILE = BASE_DIR.joinpath(cfgFileDir).joinpath(cfgFile)

config.read(CONFIG_FILE)


def getPetApiUrl():
    return config['pet']['url']


def getStoreApiUrl():
    return config['store']['url']


print(getPetApiUrl())
