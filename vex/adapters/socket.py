import asyncio

class Socket(object):
    def __init__(self, bot=None, host='localhost', port=6000):
        self.host = host
        self.port = port
        self.connection = None
        self.reader = None
        self.writer = None
        self.is_activated = False
    
    @asyncio.coroutine
    def message(self, message):
        self.writer.write(message)
        line = yield from self.reader.readline()
        return line

    @asyncio.coroutine
    def activate(self):
        self.reader, self.writer = yield from asyncio.open_connection(self.host, self.port)
        print('socket activated!')
        self.is_activated = True
    
    @asyncio.coroutine
    def run(self):
        if not self.is_activated:
            return