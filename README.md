# dmo-test
A math problem, a solution in python


## Setup

Clone the repository:

`git clone git@github.com:pynchia/dmo-test.git`

Descend into the main directory of the application:

`cd dmo-test/`

Create the python virtual environment:

`python3 -m venv .venv`

Activate the virtual environment:

`. .venv/bin/activate`

Upgrade pip:

`pip install -U pip`

Install the requirements:

the external packages first

`pip install -r requirements.txt`

and then the internal modules

`pip install .`

## Execute the tests

`pytest`

## Launch the application

The command

`runme --help`

shows the available options.

For example, the command

`runme --size 100`

calculates the steps it takes the `cm` sequence to converge to one for `m` in the range of 1 to 10

The application can also generate a diagram on file.

For example, the command

`runme --size 100 --diagram`

generates the file `steps-100.png` in the same directory

## Notes

The application covers points b) and d) of the assignment, i.e.

    b) Adapt the implementation to calculate the number of steps for each m ∈ [1, 10000].
    d) Print the number of steps for each m ∈ [1, 10000] as diagram.`

Point a) is covered by specific tests and by the code that relies on it.

    a) Implement a program to calculate the number of steps to reach 1 the first time for any given m ∈ N .

Point c), i.e.

        c) Try to improve the implementation to calculate the steps as fast as possbile.

is covered implicitly by the use of [memoization](https://en.wikipedia.org/wiki/Memoization)

Of course the set of values for m could in principle be split into chunks and assigned to several processes.

For that purpose python's `multiprocessing` module would be a good candidate.

Nota Bene: threads are not useful when applied to  computation intensive applications like this one, at least when using the standard CPython interpreter (due to the GIL).

Of course there may be a mathematical way to reduce the `cm(n)` sequence to a one-step calculation instead of having to iterate/recurse.

Unfortunately I am not Gauss and I hadn't much time to devote to that kind of solution, so I haven't even attempted to find a formula.

I hope my deliverables show the way I work as a software engineer.

I am available for any clarification.

Best regards,
  Mauro Bertolotto Bianc
