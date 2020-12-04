from sensor import AtlasProb
from util import Request
import os
import time


class Socket:
    def __init__(self):
        url = os.getenv('SERVER_URI')
        self.request = Request(url)

    def emit(self, data):
        self.request.post('/prob-data', {"prob": data})


class Program:
    def __init__(self):
        self.prob = AtlasProb()
        self.socket = Socket()

    def data_stream(self, data):
        print(data)
        self.socket.emit(data)

    def main(self):
        self.prob.start(self.data_stream)
        time.sleep(4)
        self.prob.stop()


Program().main()
