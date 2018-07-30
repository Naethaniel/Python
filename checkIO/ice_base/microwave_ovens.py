class MicrowaveBase:
    def __init__(self):
        self.seconds = 0
        self.minutes = 0

    def set_time(self, time):
        minutes, seconds = time.split(':')
        self.minutes = int(minutes)
        self.seconds = int(seconds)

    def add_time(self, time):
        if 's' in time:
            time = time[:-1]
            time = int(time)
            while self.seconds + time >= 60:
                self.minutes += 1
                time -= 60
            self.seconds += time
        else:
            time = time[:-1]
            time = int(time)
            self.minutes += time
        if self.minutes > 90:
            self.minutes = 90
            self.seconds = 0
        if self.seconds < 0:
            self.seconds = 0

    def del_time(self, time):
        if 's' in time:
            time = time[:-1]
            time = int(time)
            while self.seconds + time < 60:
                if time == 0:
                    break
                self.minutes -= 1
                time -= 60
            self.seconds -= time
        else:
            time = time[:-1]
            time = int(time)
            self.minutes -= time

        if self.minutes < 0:
            self.minutes = 0
            self.seconds = 0
        if self.seconds < 0:
            self.seconds = 0
        if self.seconds == 60:
            self.minutes += 1
            self.seconds = 0

    def show_time(self):
        raise NotImplemented()


class Microwave1(MicrowaveBase):
    def __init__(self):
        MicrowaveBase.__init__(self)

    def show_time(self):
        if self.seconds < 10:
            seconds = '0{}'.format(self.seconds)
        else:
            seconds = str(self.seconds)
        if self.minutes < 10:
            minutes = str(self.minutes)
        else:
            minutes = str(self.minutes)[1]
        return '_{}:{}'.format(minutes, seconds)


class Microwave2(MicrowaveBase):
    def __init__(self):
        MicrowaveBase.__init__(self)

    def show_time(self):
        if self.minutes < 10:
            minutes = '0{}'.format(self.minutes)
        else:
            minutes = str(self.minutes)

        if self.seconds < 10:
            seconds = str(self.seconds)
        else:
            seconds = str(self.seconds)[0]
        return '{}:{}_'.format(minutes, seconds)


class Microwave3(MicrowaveBase):
    def __init__(self):
        MicrowaveBase.__init__(self)

    def show_time(self):
        if self.minutes < 10:
            minutes = '0{}'.format(self.minutes)
        else:
            minutes = str(self.minutes)
        if self.seconds < 10:
            seconds = '0{}'.format(self.seconds)
        else:
            seconds = str(self.seconds)
        return '{}:{}'.format(minutes, seconds)


class RemoteControl:
    def __init__(self, microwave):
        self.set_time = microwave.set_time
        self.add_time = microwave.add_time
        self.del_time = microwave.del_time
        self.show_time = microwave.show_time


if __name__ == '__main__':
    microwave_3 = Microwave3()
    rc_8 = RemoteControl(microwave_3)
    rc_8.add_time("10s")
    rc_8.add_time("15s")
    rc_8.add_time("12m")
    rc_8.show_time()



