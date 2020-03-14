from client2server import client2server
from io import StringIO
import sys
from math import cos, pi

class tracker:
    def run(tracklog: StringIO):
        path = tracklog.name
        tracklog.close()
        tracklog = open(path, 'rb')
        c2s=client2server()
        cur_code = -1
        wmax = 0.5585
        angle = -40 * 2 * pi / 360
        while True:
            try:
                status=c2s.getStatus()
                dx=int(status)&0x0fff
                code = int(status) & 0xff00000000000 // 16 ** 11
                time = int(status) & 0xffffff00000 // 16 ** 5
    
                if(dx>2048):
                    dx=dx-4096
                # tracklog.write("Received %d \n" % (dx))
                # tracklog.write('Code %s \n' % bin(code))
                # tracklog.write('Time %d \n' % (time))

                if code != cur_code:
                    # tracklog.write(chr(time // 256 ** 2))
                    # tracklog.write(chr((time // 256) % 256))
                    # tracklog.write(chr(time % 256 ** 2))
                    # tracklog.write(chr(time))

                    tracklog.write(time.to_bytes(3, 'big'))
                    tracklog.write(.to_bytes(1, 'big'))

                    cur_code = code

                if(abs(int(dx))<500):
                 if(abs(int(dx))<10):
                    c2s.moveStop()
                 else:
                     speed = int(100*0.7*abs(dx)/(cos(angle)*wmax))
                    if(int(dx)>0):
                        c2s.moveLeft(speed)
                        angle -= wmax * speed / 100
                    else:
                        c2s.moveRight(speed)
                        angle += wmax * speed / 100
            except Exception as e:
                tracklog.write('!!!')
                tracklog.write(str(e))
                tracklog.write('!!!')
        c2s.__finit__
