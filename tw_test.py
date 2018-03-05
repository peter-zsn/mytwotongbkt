#coding=utf-8

"""
@varsion: ??
@author: 张帅男
@file: tw_test.py
@time: 2018/1/25 13:26
"""

import time
# from twisted.internet import epollreactor
# epollreactor.install()
from twisted.internet import protocol, reactor
from twisted.protocols.policies import TimeoutMixin

class Server(protocol.Protocol, TimeoutMixin):
    def __init__(self):
        self.name = '123'
        print 456

    def connectionMade(self):
        print '1111111111'

    def run_test(self):
        while 1:
            print self.name
            time.sleep(4)

    def run_test1(self):
        while 1:
            print 'haahhh'
            time.sleep(4)

def main():
    factory = protocol.Factory()
    factory.protocol = Server
    print "waiting for connection ..."
    # a = Server()
    # reactor.callLater(a.run_test1())
    reactor.suggestThreadPoolSize(10)
    reactor.listenTCP(8006, factory)
    reactor.run()

if __name__ == "__main__":
    main()