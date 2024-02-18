from src.singleton import BaseClass
from src.singleton import DerivedClass

if __name__ == '__main__':
    base1 = BaseClass('base')
    base2 = BaseClass('another_base')  # will not update the value in base1.  It's already instantiated.

    derived = DerivedClass('derived')
    derived2 = DerivedClass('derived2')  # will update the value in derived

    base1.show()
    base2.show()
    derived.show()
    derived2.show()