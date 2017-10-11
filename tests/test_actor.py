from .context import Actor

import unittest
import asyncio
from threading import Thread
import time


class Foo(object):
    def bar(self):
        return 42

    def sleep(self, seconds):
        time.sleep(seconds)
        return 42

    def exception(self):
        raise Exception()


class AsyncFoo(object):
    async def bar(self):
        return 42

    async def sleep(self, seconds):
        await asyncio.sleep(seconds)
        return 42

    async def exception(self):
        raise Exception()


class ActorTestSuite(unittest.TestCase):
    def setUp(self):
        self.loop = asyncio.new_event_loop()

        def thread_func(loop=self.loop):
            asyncio.set_event_loop(loop)
            try:
                loop.run_forever()
            finally:
                loop.run_until_complete(loop.shutdown_asyncgens())
                loop.close()

        self.thread = Thread(target=thread_func)
        self.thread.start()

    def tearDown(self):
        self.loop.call_soon_threadsafe(self.loop.stop)
        self.thread.join()

    def test_call_1_nonasync_method(self):
        sut = Actor(Foo(), self.loop)

        self.assertEqual(42, sut.bar().result())

    def test_call_1_heavy_nonasync_method(self):
        sut = Actor(Foo(), self.loop)

        future = sut.sleep(0.1)

        self.assertFalse(future.done())
        time.sleep(0.1)
        self.assertEqual(42, future.result())

    def test_call_1_nonasync_method_when_raises_exception(self):
        sut = Actor(Foo(), self.loop)

        self.assertRaises(Exception, sut.exception().result)

    def test_call_1_async_method(self):
        sut = Actor(AsyncFoo(), self.loop)

        self.assertEqual(42, sut.bar().result())

    def test_call_1_heavy_async_method(self):
        sut = Actor(AsyncFoo(), self.loop)

        future = sut.sleep(0.1)

        self.assertFalse(future.done())
        time.sleep(0.1)
        self.assertEqual(42, future.result())

    def test_call_1_async_method_when_raises_exception(self):
        sut = Actor(AsyncFoo(), self.loop)

        self.assertRaises(Exception, sut.exception().result)
