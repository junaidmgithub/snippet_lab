from datetime import datetime


def measure_runtime(method):
    def measure(*args, **kwargs):
        s = datetime.now()
        r = method(*args, **kwargs)
        f = datetime.now()
        print('Execution of <{}> finished (runtime): {}'.format(method.__name__, str(f - s)))
        return r
    return measure

