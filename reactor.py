# noinspection PyUnresolvedReferences
from client2server import client2server

class tracker:
    def run(tracklog):
        c2s=client2server()
        while True:
            status=c2s.getStatus()
            dx=int(status)&0x0fff
            x=int(status)&0x000f

            if(dx>2048):
                dx=dx-4096
            tracklog.write("Received %d \n" % (dx))
            if(abs(int(dx))<500):
                if(abs(int(dx))<30):
                    speed=int(abs(dx)/6)
                    if(int(dx)>0):
                        c2s.moveLeft(speed)
                    else:
                        c2s.moveRight(speed)
                else:
                    speed=int(abs(dx)/1.3)
                    if(int(dx)>0):
                        c2s.moveLeft(speed)
                    else:
                        c2s.moveRight(speed)
        c2s.__finit__
