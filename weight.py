# coding=utf-8

import argparse


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


def comparator():
    kefi = check_weight() # what does kefi men ?
    if kefi < 18.5:
        print('Low weight')
    elif 18.5 < kefi < 24.9:
        print('Everything is fine!')
    elif 25.0 < kefi < 29.9:
        print('Dangerous!')
    elif 29.9 < kefi < 34.9:
        print('How can you move?')
    elif 35.9 < kefi:
        print('OMG')


if __name__ == '__main__':
    comparator()
