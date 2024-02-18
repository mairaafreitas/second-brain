from .utils import SingletonMeta


class BaseClass(metaclass=SingletonMeta):
    base_value = "Base Value"

    def __init__(self, value, *args, **kwargs):
        print(f"Initializing {type(self).__name__} with value {value}")
        self.value = value

    def show(self):
        print(f"BaseClass: value = {self.value}, base_value = {self.base_value}")


class DerivedClass(BaseClass):
    __allow_reinitialization = True
    base_value = "Derived Value"

    def __init__(self, value,  *args, **kwargs):
        print(f"Initializing {type(self).__name__} with value {value}")
        self.value = value

    def show(self):
        print(f"DerivedClass: value = {self.value}, base_value = {self.base_value}")


base1 = BaseClass('base')
base2 = BaseClass('another_base')  # will not update the value in base1.  It's already instantiated.

derived = DerivedClass('derived')
derived2 = DerivedClass('derived2')  # will update the value in derived

base1.show()
base2.show()
derived.show()
derived2.show()