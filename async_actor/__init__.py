import asyncio
from concurrent.futures import Future
from functools import partial


__version__ = '0.1'


class Actor(object):
    def __init__(self, obj, loop):
        self._obj = obj
        self._loop = loop

    def __getattr__(self, name):
        attr = self._obj.__getattribute__(name)
        if not callable(attr):
            return attr
        else:
            if asyncio.iscoroutinefunction(attr):
                def wrap(f=attr, loop=self._loop):
                    def func(*args, **kwargs):
                        co = attr(*args, **kwargs)
                        return asyncio.run_coroutine_threadsafe(co, loop)
                    return func
            else:
                def wrap(f=attr, loop=self._loop):
                    def task(future, *args, **kwargs):
                        try:
                            r = f(*args, **kwargs)
                            future.set_result(r)
                        except Exception as e:
                            future.set_exception(e)
                        return future

                    def func(*args, **kwargs):
                        future = Future()
                        loop.call_soon_threadsafe(
                            partial(task, future, *args, **kwargs))
                        return future
                    return func
            return wrap()
