from src.transport.public import Public
from src.transport.car import Car
from src.transport.bike import Bike
from src.route_selection import RouteSelection


if __name__ == '__main__':

    public_transport = Public()
    route_selection = RouteSelection(public_transport)
    print('Estimated time to reach destination: ', route_selection.time_estimation(60))

    car = Car()
    route_selection = RouteSelection(car)
    print('Estimated time to reach destination: ', route_selection.time_estimation(60))

    bike = Bike()
    route_selection = RouteSelection(bike)
    print('Estimated time to reach destination: ', route_selection.time_estimation(60))
