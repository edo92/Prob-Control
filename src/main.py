from sensor import AtlasProb
from util import Request

import time


class Socket:
    def __init__(self):
        url = 'https://c2f82d141074ff41254776558b262db7.balena-devices.com'
        self.request = Request(url)  # os.getenv('SERVER_URI')

    def emit(self, data):
        self.request.post('/prob-data', {"prob": data})


class Program:
    def __init__(self):
        self.prob = AtlasProb()
        self.socket = Socket()

    def data_stream(self, data):
        print('data--->')
        print(data)
        self.socket.emit(data)

    def main(self):
        self.prob.start(self.data_stream)
        time.sleep(4)
        self.prob.stop()


Program().main()
