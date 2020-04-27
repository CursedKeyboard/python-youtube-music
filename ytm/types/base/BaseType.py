import builtins
import re
from ... import classes

class BaseType(str, metaclass=classes.BuiltinMeta):
    _patterns = ()

    def __new__(cls, value):
        if not cls._validate(value):
            raise TypeError \
            (
                'Invalid {class_name}: {value}'.format \
                (
                    class_name = cls.__name__,
                    value = repr(str(value)),
                )
            )

        value = cls._clean(value)

        return str.__new__(cls, value)

    def __repr__(self):
        return '<{class_name}({value})>'.format \
        (
            class_name = self.__class__.__name__,
            value = super().__repr__(),
        )

    @classmethod
    def _validate(cls, value: str):
        if not cls._patterns:
            return True

        if not builtins.isinstance(value, str):
            return False

        for pattern in cls._patterns:
            match = re.match \
            (
                pattern = pattern,
                string  = value,
                flags   = re.DOTALL,
            )

            if match is not None:
                break
        else:
            return False

        return True

    @classmethod
    def _clean(cls, value: str):
        return value