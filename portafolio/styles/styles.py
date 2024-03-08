from enum import Enum
import reflex as rx

MAX_WIDTH = "900px"
IMAGE_HEIGHT = "200px"


class EmSize(Enum):
    DEFAULT = "1em"  # 16 px
    MEDIUM = "2em"
    BIG = "4em"


class Size(Enum):
    ZERO = "0"
    SMALL = "2"
    DEFAULT = "4"  # 16px
    MEDIUM = "6"
    BIG = "8"


STYLESHEETS = ["https://cdn.jsdelivr.net/gh/devicons/devicon@latest/devicon.min.css"]

BASE_STYLES = {
    rx.button: {
        "--cursor-button": "pointer",
    }
}
