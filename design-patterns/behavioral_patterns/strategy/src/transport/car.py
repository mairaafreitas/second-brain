import datetime

from . import Transport


class Car(Transport):
    speed = 90

    def operation(self, distance):
        estimated_hours = distance / self.speed
        return str(datetime.timedelta(hours=estimated_hours))
