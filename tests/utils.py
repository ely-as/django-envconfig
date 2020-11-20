from typing import List, Tuple

from django.conf import global_settings


def get_global_settings_types() -> List[Tuple[str, type]]:
    setting_names = [s for s in dir(global_settings) if s.isupper()]
    return [(s, type(getattr(global_settings, s))) for s in setting_names]
