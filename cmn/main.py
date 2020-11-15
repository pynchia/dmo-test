"""
The main module of the application
"""
import logging

from cmn.converge import count_steps_for_many_m


log = logging.getLogger()


def main(size):
    for m, steps in enumerate(count_steps_for_many_m(size), start=1):
        print(f"c{m} reaches 1 in {steps=}")
