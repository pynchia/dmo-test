"""
The main module of the application
"""
import logging
import matplotlib as mpl
import matplotlib.pyplot as plt

from cmn.converge import count_steps_for_many_m


log = logging.getLogger()


def main(size, diagram):
    counts = count_steps_for_many_m(size)
    if diagram:
        mpl.use('Agg')

        fig, ax = plt.subplots(1,1)
        ax.set_title("Steps it takes Cm to reach 1")
        ax.set_xlabel("m")
        ax.set_ylabel("steps")

        ax.plot(list(counts))
        fig.savefig(f"steps-{size}.png", dpi=300)
    else:
        for m, steps in enumerate(counts, start=1):
            print(f"c{m} reaches 1 in {steps=}")
