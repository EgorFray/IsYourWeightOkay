# coding=utf-8

import argparse
import logging


def create_logger():
    logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%H:%M:%S', level='INFO')
    logger = logging.getLogger()
    return logger


def create_parser():
    parser = argparse.ArgumentParser(
        prog='weight_ratio',
        description='This program checks your weight'
    )
    parser.add_argument('-w', '--weight', type=int, metavar='')
    parser.add_argument('-hh', '--height', type=float, metavar='')
    return parser


def start_parsing():
    return create_parser().parse_args()


def check_weight():
    parser = start_parsing()
    return parser.weight / parser.height ** 2


def advice():
    answear = create_logger()
    answear.info('Do you want some advice?')
    advice = input()
    if advice == 'yes':
        explit_advice()
    elif advice == 'no':
        answear.info('''that's all''')
    else:
        answear.warning('You can use only yes/no')


def explit_advice():
    pass
    

def comparator():
    answear = create_logger()
    answear.info('Start programm...')
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
    advice()


if __name__ == '__main__':
    comparator()
