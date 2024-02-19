from src.singleton import BaseClass
from src.singleton import DerivedClass
from src.singleton import SecondDerivedClass

if __name__ == '__main__':
    base1 = BaseClass('base')
    base2 = BaseClass('another_base')  # will not update the value in base1.  It's already instantiated.

    derived = DerivedClass('derived')
    derived2 = DerivedClass('derived2')

    second_derived = SecondDerivedClass('second_derived')
    second_derived2 = SecondDerivedClass('second_derived2')

    base1.show()
    base2.show()
    derived.show()
    derived2.show()
    second_derived.show()
    second_derived2.show()
