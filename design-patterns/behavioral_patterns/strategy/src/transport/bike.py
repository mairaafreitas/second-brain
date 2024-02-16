import datetime

from . import Transport


class Bike(Transport):
    speed = 75

    def operation(self, distance):
        estimated_hours = distance / self.speed
        return str(datetime.timedelta(hours=estimated_hours))
