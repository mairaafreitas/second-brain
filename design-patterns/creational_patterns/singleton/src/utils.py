from typing import Any
from typing import Dict


class SingletonMeta(type):
    _instances: Dict[object, Any] = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            print(f"Singleton __call__ {cls.__name__} id {id(cls)}")
            # if we do not have built an instance before, build one
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        else:
            instance = cls._instances[cls]

        return cls._instances[cls]
