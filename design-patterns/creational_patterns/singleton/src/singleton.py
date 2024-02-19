from .utils import SingletonMeta


class BaseClass(metaclass=SingletonMeta):
    base_value = "Base Value"

    def __init__(self, value, *args, **kwargs):
        print(f"Initializing {type(self).__name__} with value {value}")
        self.value = value

    def show(self):
        print(f"BaseClass: value = {self.value}, base_value = {self.base_value}")


class DerivedClass(BaseClass):
    base_value = "Derived Value"

    def __init__(self, value,  *args, **kwargs):
        print(f"Initializing {type(self).__name__} with value {value}")
        self.value = value

    def show(self):
        print(f"DerivedClass: value = {self.value}, base_value = {self.base_value}")


class SecondDerivedClass(BaseClass):
    base_value = "Second Derived Value"

    def __init__(self, value,  *args, **kwargs):
        print(f"Initializing {type(self).__name__} with value {value}")
        self.value = value

    def show(self):
        print(f"SecondDerivedClass: value = {self.value}, base_value = {self.base_value}")