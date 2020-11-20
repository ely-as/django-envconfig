from typing import Any, Union
import json
from json.decoder import JSONDecodeError

NoneType: type = type(None)


class EnvParser:
    # case insensitive
    bool_true_vals = ('1', 'on', 'true', 'yes')
    bool_false_vals = ('0', 'off', 'false', 'no')
    none_vals = ('none', 'null')

    @classmethod
    def parse(cls, val: str, *expected_types: type) -> Any:
        # Evaluate NoneType first if it's an expected type
        types_ = list(expected_types)
        if NoneType in types_ and types_[0] != NoneType:
            types_.insert(0, types_.pop(types_.index(NoneType)))
        # Attempt to parse val as each type. If all fails raise last ValueError
        for i, type_ in enumerate(types_, start=1):
            try:
                return getattr(cls, f'_{type_.__name__}')(val)
            except ValueError:
                if i < len(types_):
                    pass
                raise

    @classmethod
    def _bool(cls, val: str) -> bool:
        if val.lower() in cls.bool_true_vals:
            return True
        elif val.lower() in cls.bool_false_vals:
            return False
        raise ValueError

    @classmethod
    def _dict(cls, val: str) -> dict:
        dict_ = cls._json(val)
        if not isinstance(dict_, dict):
            raise ValueError(f"Expected dict but received {type(dict_)}")
        return dict_

    @classmethod
    def _float(cls, val: str) -> float:
        return float(val)

    @classmethod
    def _int(cls, val: str) -> int:
        return int(val)

    @classmethod
    def _json(cls, val: str) -> Union[dict, list]:
        try:
            return json.loads(val)
        except JSONDecodeError:
            raise ValueError("Invalid JSON")

    @classmethod
    def _list(cls, val: str) -> list:
        if val.startswith('['):
            return cls._json(val)  # type: ignore  # noqa
        return val.split(',')

    @classmethod
    def _NoneType(cls, val: str) -> None:
        if val.lower() in cls.none_vals:
            return
        raise ValueError  # don't need a message

    @classmethod
    def _str(cls, val: str) -> str:
        return val

    @classmethod
    def _tuple(cls, val: str) -> tuple:
        return tuple(cls._list(val))
