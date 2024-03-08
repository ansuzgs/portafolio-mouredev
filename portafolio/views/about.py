import reflex as rx

from portafolio.components.heading import heading


def about() -> rx.Component:
    return rx.vstack(
        heading("Sobre mi"),
        rx.text("Descripcion"),
    )
