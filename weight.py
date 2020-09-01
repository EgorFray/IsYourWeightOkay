# coding=utf-8

import argparse
import logging


class WeightRatio():
    def create_logger(self):
        logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%H:%M:%S', level='INFO')
        logger = logging.getLogger()
        return logger

    def create_parser(self):
        parser = argparse.ArgumentParser(
            prog='weight_ratio',
            description='This program checks your weight'
        )
        parser.add_argument('-w', '--weight', type=int, metavar='')
        parser.add_argument('-hh', '--height', type=float, metavar='')
        return parser

    def start_parsing(self):
        return self.create_parser().parse_args()

    def check_weight(self):
        parser = self.start_parsing()
        return parser.weight / parser.height ** 2

    def advice(self, answer):
        answear = self.create_logger()
        answear.info('Do you want some advice?')
        advice = input()
        if advice == 'yes':
            self.explit_advice(answer)
        elif advice == 'no':
            answear.info('''that's all''')
        else:
            answear.warning('You can use only yes/no')

    def explit_advice(self, answer):
        if answer == 'Low weight':
            print('You just need to eat more!')
        elif answer == 'Everything is fine!':
            print('You are in fine condition! Eat healthy food and do workouts to keep yourself feet!')
        elif answer == 'Dangerous!':
            print('You should do more exercises and try not to eat bad food')
        elif answer == 'How can you move?':
            print('Stop eating! DO EXERCISES!')
        elif answer == 'OMG':
            print('If you do not stop eating bad food you will die. You must do some workout and avoid fast and bad food.')

    def comparator(self):
        answear = self.create_logger()
        answear.info('Start programm...')
        kefi = self.check_weight()
        if kefi < 18.5:
            answer = 'Low weight'
        elif 18.5 < kefi < 24.9:
            answer = 'Everything is fine!'
        elif 25.0 < kefi < 29.9:
            answer = 'Dangerous!'
        elif 29.9 < kefi < 34.9:
            answer = 'How can you move?'
        elif 35.9 < kefi:
            answer = 'OMG'
        print(answer)
        self.advice(answer)

if __name__ == '__main__':
    start_programme = WeightRatio()
    start_programme.comparator()
