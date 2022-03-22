"""Represents an object pool pattern."""

from typing import List


class Reusable:
    """Represents a class that would be expensive to make so we
    want to use it repeatable instead of destroying it each time
    we stop using it."""

    def test(self):
        """Test the object by showing it's id."""
        print(f"Using object {id(self)}")


class ReusablePool:
    """Represents an object pool."""

    free: List = []
    in_use: List = []
    size: int = 0

    def __init__(self, size):
        self.size = size
        for _ in range(size):
            self.free.append(Reusable())

    def acquire(self) -> Reusable:
        """Gets an instance of a Reusable object from the pool."""
        if len(self.free) <= 0:
            raise Exception("No more objects are available.")

        # get a reference to the object
        reusable = self.free[0]
        # remove from free list
        self.free.remove(reusable)
        # add to in_use list
        self.in_use.append(reusable)
        return reusable

    def release(self, reusable: Reusable):
        """Releases an instance of Reusable back into the pool for others to use."""
        self.in_use.remove(reusable)
        self.free.append(reusable)


pool = ReusablePool(2)
r = pool.acquire()
r2 = pool.acquire()
# r3 = pool.acquire() # causes an exception because pool only has 2 objects
pool.release(r2)

r.test()
r2.test()

r3 = pool.acquire()
r3.test()
