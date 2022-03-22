"""Represents a singleton pattern in python."""

# Anti-pattern:
# Singletons break object-oriented programming desgin principles.
#   If you inherit from it, this allows you to create multiple instances
#   of that singleton by creating multiple subclasses which shouldn't be allowed.
# You don't have control over creation.
#   When you access the instance you never know whether it's an existing instance
#   or a newly created one.
# Testing code that has singetons is really hard because you can't easily create a
#   fresh instance for each test you want to run.
# Singletons don't work well in multi-threaded applications due to a race conditions
#   where if multiple threads try to access a not yet instantiated singleton at the
#   same time, you end up creating multiple instances.


class Singleton(type):
    """
    Represents a singleton.
    inheriting from type makes this a metaclass.
    """
    # for every class that is a singleton, you maintain an
    # instace of that in this dictionary
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(
                Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Logger(metaclass=Singleton):
    """A logger class that is made into a singleton."""

    def log(self, msg):
        """Writes out a message."""
        print(msg)


# both loggers refer to the same instance of logger
logger = Logger()
logger2 = Logger()
print(logger)
print(logger2)

logger.log("Hello")
logger2.log("World")
