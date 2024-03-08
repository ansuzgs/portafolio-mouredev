import reflex as rx

from portafolio.components.icon_button import icon_button
from portafolio.data import Media
from portafolio.styles.styles import Size


def media(data: Media) -> rx.Component:
    return rx.hstack(
        icon_button(
            "mail",
            f"mailto:{data.email}",
            data.email,
            True,
        ),
        icon_button(
            "file-text",
            data.cv,
        ),
        icon_button(
            "github",
            data.github,
        ),
        icon_button(
            "linkedin",
            data.linkedin,
        ),
        spacing=Size.SMALL.value,
    )
