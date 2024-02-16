import datetime

from . import Transport


class Public(Transport):
    speed = 50

    def operation(self, distance):
        estimated_hours = distance / self.speed
        return str(datetime.timedelta(hours=estimated_hours))