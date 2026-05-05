from dataclasses import dataclass


@dataclass
class Settings:
    theme: str = "light"
    language: str = "en"
    window_width: int = 1024
    window_height: int = 768
    password: str = ""

    def to_dict(self) -> dict:
        return {
            "theme": self.theme,
            "language": self.language,
            "window_width": self.window_width,
            "window_height": self.window_height,
            "password": self.password,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Settings":
        return cls(
            theme=data.get("theme", "light"),
            language=data.get("language", "en"),
            window_width=int(data.get("window_width", 1024)),
            window_height=int(data.get("window_height", 768)),
            password=data.get("password", ""),
        )
