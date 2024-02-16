class RouteSelection:

    def __init__(self, transport):
        """self._transport references the objects of other transport classes. It's called composition."""
        self._transport = transport

    def time_estimation(self, distance):
        """Call the operation's function from referenced instance variable."""
        return self._transport.operation(distance)
