# noinspection PyUnresolvedReferences
from client2server import client2server
from io import StringIO
import sys


class tracker:
    def run(tracklog: StringIO):
        c2s = client2server()
        status = c2s.getStatus()
        path = tracklog.name
        tracklog = open(path, 'wb')
        while True:
            try:
                status = c2s.getStatus()
                dx = int(status) & 0x0fff
                code = int(status) & 0xff00000000000 // 16 ** 11
                time = int(status) & 0xffffff00000 // 16 ** 5

                if (dx > 2048):
                    dx = dx - 4096
                tracklog.write(time.to_bytes(3, 'big'))
                tracklog.write(code.to_bytes(1, 'big'))

                if (abs(int(dx)) < 500):
                    if (abs(int(dx)) < 10):
                        c2s.moveStop()
                    else:
                        speed = 50
                        if (int(dx) > 0):
                            c2s.moveLeft(speed)
                        else:
                            c2s.moveRight(speed)
            except Exception as e:
                tracklog.write(int(0).to_bytes(15, 'big'))
        c2s.__finit__
