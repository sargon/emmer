def lock(function):
    """A decorator to use to lock an instance of a class. The instance must
    have a `lock` instance variable already initialized.
    """
    def decorator(self, *args):
        self.lock.acquire()
        try:
            natural_return_value = function(self, *args)
            return natural_return_value
        finally:
            self.lock.release()

    return decorator
