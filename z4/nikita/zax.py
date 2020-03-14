# noinspection PyUnresolvedReferences
from client2server import client2server

class tracker:
    def run(tracklog):
        c2s=client2server()
        x = int(status) & 0xf0000 // 16 ** 4
        while x!=0:
            status=c2s.getStatus()
            dx=int(status)&0x0fff
            time = int(status) & 0xffffff00000 // 16 ** 5
            x = int(status) & 0xf0000 // 16 ** 4
            tracklog.write("Received %d \n" % (x))
            tracklog.write("time %d \n" % (time))
            speed = 100
            c2s.moveRight(speed)

        c2s.__finit__
