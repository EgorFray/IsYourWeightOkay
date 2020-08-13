import argparse
import logging


def create_logger():
    logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%H:%M:%S', level='INFO')
    logger = logging.getLogger()
    return logger


def createparser():
    parser = argparse.ArgumentParser(
        prog='weight_ratio',
        description='cool program'
    )
    parser.add_argument('-w', '--weight', type=int, metavar='')
    parser.add_argument('-hh', '--height', type=float, metavar='')
    return parser


def start_parcing():
    parser = createparser()
    return parser.parse_args()


def check_weight():
    parser = start_parcing()
    kef = parser.weight / (parser.height * parser.height)
    return kef


def comparator():
    answear = create_logger()
    answear.info('Start programm...')
    parser = start_parcing()
    kefi = check_weight()
    if kefi < 18.5:
        answear.info('Low weight')
    elif 18.5 < kefi < 24.9:
        answear.info('Everything is fine!')
    elif 25.0 < kefi < 29.9:
        answear.info('Dangerous!')
    elif 29.9 < kefi < 34.9:
        answear.info('How can you move?')
    elif 35.9 < kefi:
        answear.info('OMG')
    answear.info('Do you want some advice?')
    advice = input()
    if advice == 'yes':
        answear.info('okay')
    elif advice == 'no':
        answear.info('''that's all''')
    else:
        answear.warning('You can use only yes/no')


if __name__ == '__main__':
    comparator()
