import configparser

config=configparser.ConfigParser()
config.read('config.ini')
print(config.get('section1','key1'))