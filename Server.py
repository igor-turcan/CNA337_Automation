# Pinging AWS EC2 public IPv4.
import os

class Server:
    """ Server class for representing and manipulating servers. """

    def __init__(self, server_ip):
        # TODO -
        self.server_ip = server_ip

    def ping(self):
        # TODO - Use os module to ping the server
        return os.system("ping -n 4 %s" % self.server_ip)
