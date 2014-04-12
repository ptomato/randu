randu
=====

Python implementation of the flawed random number generator
[RANDU](http://en.wikipedia.org/wiki/RANDU) as a
[`random.Random`](https://docs.python.org/2/library/random.html) subclass.

I entered Kaggle's April Fool's
[Random Number Grand Challenge](http://www.kaggle.com/c/random-number-grand-challenge)
with this program.
Dubious competitions call for dubious solutions.

### Usage ###

Initialize an instance:
```py
from randu import Randu
randu = Randu(seed)
```
All the methods from
[`random.Random`](https://docs.python.org/2/library/random.html) should work on
this as well.
Unit test to make sure the algorithm is correct:
```py
Randu.check()
```
To generate a submission for the Kaggle challenge, run `python randu.py` from
the command line, and a `randu.csv` file will appear.
