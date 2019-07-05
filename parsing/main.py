import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-n", "--name", default='noname', type=str)
parser.add_argument("-l", "--lang", default='en', choices=['en', 'ru'])
parser.add_argument("-t", "--times", default=1, type=int)
args = parser.parse_args()


def main(name, lang, times):
    for _ in range(times):
        if lang == 'en':
            print('Hello, {}!'.format(name))
        else:
            print('Привет, {}!'.format(name))


main(**args.__dict__)
