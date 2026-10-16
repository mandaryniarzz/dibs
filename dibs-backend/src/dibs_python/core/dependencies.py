from typing import Annotated

from dibs_python.core.settings import Settings, get_settings
from fastapi import Depends

SettingsDep = Annotated[Settings, Depends(get_settings)]