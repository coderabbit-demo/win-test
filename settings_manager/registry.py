import winreg
from settings_manager.settings import Settings

REGISTRY_HIVE = winreg.HKEY_LOCAL_MACHINE
REGISTRY_KEY_PATH = r"SOFTWARE\AppSettingsManager"

_STR_FIELDS = ("theme", "language", "password")
_INT_FIELDS = ("window_width", "window_height")


def save_settings(settings: Settings) -> None:
    """Persist settings to the registry."""
    key = winreg.CreateKey(REGISTRY_HIVE, REGISTRY_KEY_PATH)
    data = settings.to_dict()
    for field in _STR_FIELDS:
        winreg.SetValueEx(key, field, 0, winreg.REG_SZ, data[field])
    for field in _INT_FIELDS:
        winreg.SetValueEx(key, field, 0, winreg.REG_DWORD, data[field])


def load_settings() -> Settings:
    """Load settings from the registry."""
    key = winreg.OpenKey(REGISTRY_HIVE, REGISTRY_KEY_PATH)
    data = {}
    for field in _STR_FIELDS:
        value, _ = winreg.QueryValueEx(key, field)
        data[field] = value
    for field in _INT_FIELDS:
        value, _ = winreg.QueryValueEx(key, field)
        data[field] = value
    return Settings.from_dict(data)


def delete_settings() -> None:
    """Delete all settings by removing the registry key."""
    winreg.DeleteKey(REGISTRY_HIVE, REGISTRY_KEY_PATH)
