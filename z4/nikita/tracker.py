from client2server import client2server

class tracker:
    def run(tracklog):
        c2s=client2server()
        i=0
        wmax = 0.5585
        angle = -40 * 2 * pi / 360
        while i==0:
            status=c2s.getStatus()
            dx=int(status)&0x0fff

            if(dx>2048):
                dx=dx-4096
            tracklog.write("Received %d \n" % (dx))
            if(abs(int(dx))<500):
             if(abs(int(dx))<20):
                c2s.moveStop()
             else:
                speed = int(100 * 0.07 * abs(dx) / (cos(angle) * wmax))
                if(int(dx)>0):
                    c2s.moveLeft(speed)
                    angle -= wmax * speed / 100
                else:
                    c2s.moveRight(speed)
                    angle += wmax * speed / 100
        c2s.__finit__
