import time
class TrafficLight:
    __color = ['красный', 'желтый', 'зеленый']

    def running(self):
        times = 0
        while 0 <= times < 3:
            print(TrafficLight.__color[times])
            if times == 0:
                time.sleep(7)
            elif times == 1:
                time.sleep(2)
            else:
                time.sleep(7)
            times += 1

times_traffic = TrafficLight()
times_traffic.running()

