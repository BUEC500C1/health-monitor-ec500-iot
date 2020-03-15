import yaml

stream = open('config.yml', 'r')
config = yaml.load(stream, Loader=yaml.FullLoader)

if __name__ == '__main__':
    print(config)
