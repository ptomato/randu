import random
import csv


class Randu(random.Random):
    """
    Implementation of the flawed pseudorandom number generating algorithm RANDU.
    See, for more information: http://en.wikipedia.org/wiki/RANDU

    "...its very name RANDU is enough to bring dismay into the eyes and stomachs
    of many computer scientists!"
       -- Donald E. Knuth, The Art of Computer Programming
    """

    def __init__(self, seed=[]):
        try:
            self.seed(seed)
        except TypeError:  # not hashable
            self._state = 1

    def seed(self, x):
        self._state = hash(x) % 0x80000000

    def getstate(self):
        return self._state

    def setstate(self, state):
        self._state = state

    def random(self):
        self._state = (65539L * self._state) % 0x80000000
        return self._state / float(0x80000000)

    @staticmethod
    def check():
        """
        Check against Wikipedia's listed sequence of numbers (start and end of
        the sequence with initial seed 1):
        1, 65539, 393225, 1769499, 7077969, 26542323, ..., 2141591611,
        388843697, 238606867, 79531577, 477211307, 1
        """
        randu = Randu(2141591611)
        actual = []
        for x in range(11):
            actual.append(randu.getstate())
            randu.random()
        assert actual == [2141591611, 388843697, 238606867, 79531577, 477211307,
            1, 65539, 393225, 1769499, 7077969, 26542323]


# Output data for Kaggle competition
if __name__ == '__main__':
    Randu.check()

    # Gosh, I don't know what to seed it with
    randu = Randu(random.randint(1, 0x7FFFFFFF))

    # Gleaned from painstaking analysis of the test data
    upper_bound = 1000000000

    with open('randu.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Id', 'Predicted'])
        for count in range(10000):
            writer.writerow([count, int(randu.random() * upper_bound)])
