import argparse


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
    parser = start_parcing()
    kefi = check_weight()
    if kefi < 18.5:
        print('Low weight')
    elif 18.5 < kefi < 24.9:
        print('Eveything is fine!')
    elif 25.0 < kefi < 29.9:
        print('Dangerous!')
    elif 29.9 < kefi < 34.9:
        print('How can you move?')
    elif 35.9 < kefi:
        print('OMG')


if __name__ == '__main__':
    comparator()
