"""Represents an object pool pattern."""

from typing import List

# Things to keep in mind with object pools
#   When an object is released, you have to make sure it is reset to a fresh state.
# If you don't reset objects properly, you may end up leaking information.
#   If an authentication token wasn't cleared, it may give undesirable access to the next
#   user of that instance.
# Multi-threading is still an issue with object pool as multiple threads could potentially
#   use the same object in the pool.


class PoolManager:
    """Context manager for an object pool."""

    def __init__(self, pool):
        self.pool = pool
        self.obj = None

    def __enter__(self):
        """Store the object in the config manager so that we can release it later."""
        self.obj = self.pool.acquire()
        return self.obj

    def __exit__(self, type, value, traceback):
        """Releases the stored object."""
        self.pool.release(self.obj)


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
        obj = self.free[0]
        # remove from free list
        self.free.remove(obj)
        # add to in_use list
        self.in_use.append(obj)
        return obj

    def release(self, obj: Reusable):
        """Releases an instance of Reusable back into the pool for others to use."""
        self.in_use.remove(obj)
        self.free.append(obj)


# pool = ReusablePool(2)
# r = pool.acquire()
# r2 = pool.acquire()
# # r3 = pool.acquire() # causes an exception because pool only has 2 objects
# pool.release(r2)

# r.test()
# r2.test()

# r3 = pool.acquire()
# r3.test()


pool = ReusablePool(2)
with PoolManager(pool) as r_pool:
    r_pool.test()
with PoolManager(pool) as r_pool:
    r_pool.test()
with PoolManager(pool) as r_pool:
    r_pool.test()
