# Windows App Settings Manager

This project is a Windows app settings manager built in Python. It lets you save user preferences — like theme, language, and window size — directly to the Windows Registry, so they persist between sessions. You run simple CLI commands to save, load, or reset settings. It's a clean, zero-dependency example of how to work with the Windows Registry from Python using the built-in `winreg` module.

## Usage

```bash
# Save settings
python -m settings_manager save --theme dark --language fr --width 1280 --height 720

# Load current settings
python -m settings_manager load

# Reset to defaults
python -m settings_manager reset
```
