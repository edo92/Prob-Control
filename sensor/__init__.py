#!/usr/bin/python

from sensor import AtlasI2C
import time
import threading       # used for sleep delay and timestamps
import string     # helps parse strings


class AtlasProb:
    def __init__(self):
        # Initialize altlas i2c
        self.device = AtlasI2C()
        # must be greater than AtlasI2C.long_timeout
        self.delaytime = AtlasI2C.long_timeout
        # polling status
        self.status = False

    def set_status(self, status):
        self.status = status

    # read connected addresses
    def get_all_address(self):
        return self.device.list_i2c_devices()

    # passed array of address/map->set
    def set_all_addresses(self, addrs):
        for addr in addrs:
            self.set_address(addr)

    # set unique address
    def set_address(self, addr):
        self.device.set_i2c_address(addr)

    # Read sensor data
    def read_data(self):
        self.set_status(True)
        while self.status:
            self.stream(self.device.query("R"))
            time.sleep(self.delaytime - AtlasI2C.long_timeout)

    def stop(self):
        self.set_status(False)

    def start(self, stream):
        self.stream = stream
        # list i2c addresses
        addrs = self.get_all_address()
        # sets list of addresses
        self.set_all_addresses(addrs)
        # read data/create thread independent polling
        r_thread = threading.Thread(target=self.read_data)
        # start thread thats runign read method
        r_thread.start()
