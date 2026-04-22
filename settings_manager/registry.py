import winreg
from settings_manager.settings import Settings

REGISTRY_HIVE = winreg.HKEY_CURRENT_USER
REGISTRY_KEY_PATH = r"SOFTWARE\AppSettingsManager"

_STR_FIELDS = ("theme", "language")
_INT_FIELDS = ("window_width", "window_height")


def save_settings(settings: Settings) -> None:
    """Persist settings to the registry under HKCU."""
    with winreg.CreateKey(REGISTRY_HIVE, REGISTRY_KEY_PATH) as key:
        data = settings.to_dict()
        for field in _STR_FIELDS:
            winreg.SetValueEx(key, field, 0, winreg.REG_SZ, data[field])
        for field in _INT_FIELDS:
            winreg.SetValueEx(key, field, 0, winreg.REG_DWORD, data[field])


def load_settings() -> Settings:
    """Load settings from the registry. Returns defaults if key does not exist."""
    try:
        with winreg.OpenKey(REGISTRY_HIVE, REGISTRY_KEY_PATH) as key:
            data = {}
            for field in _STR_FIELDS:
                try:
                    value, _ = winreg.QueryValueEx(key, field)
                    data[field] = value
                except FileNotFoundError:
                    pass
            for field in _INT_FIELDS:
                try:
                    value, _ = winreg.QueryValueEx(key, field)
                    data[field] = value
                except FileNotFoundError:
                    pass
            return Settings.from_dict(data)
    except FileNotFoundError:
        return Settings()


def delete_settings() -> None:
    """Delete all settings by removing the registry key."""
    try:
        with winreg.OpenKey(
            REGISTRY_HIVE, REGISTRY_KEY_PATH, access=winreg.KEY_ALL_ACCESS
        ) as key:
            # Delete all values first before deleting the key itself
            while True:
                try:
                    value_name, _, _ = winreg.EnumValue(key, 0)
                    winreg.DeleteValue(key, value_name)
                except OSError:
                    break
        winreg.DeleteKey(REGISTRY_HIVE, REGISTRY_KEY_PATH)
    except FileNotFoundError:
        pass
