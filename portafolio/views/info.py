import reflex as rx

from portafolio.components.info_detail import info_detail
from portafolio.components.heading import heading
from portafolio.data import Info
from portafolio.styles.styles import Size


def info(title: str, infos: list[Info]) -> rx.Component:
    return rx.vstack(
        heading(title),
        rx.vstack(
            *[info_detail(info) for info in infos],
            spacing=Size.DEFAULT.value,
            width="100%",
        ),
        spacing=Size.DEFAULT.value,
        width="100%",
    )
