import json
import reflex as rx


class UserMetadata(rx.Base):
    user: str
    groups: list[str]


class State(rx.State):
    count: int = 0
    user: UserMetadata | None = None

    def increment(self):
        self.count += 1

    def decrement(self):
        self.count -= 1

    def get_current_user(self) -> str | None:
        """
        Get the user metadata from the RStudio-Connect-Credentials header and then
        parse the data into a UserMetadata object.
        """
        rstudio_connect_credentials = self.router.headers.dict().get(
            "rstudio_connect_credentials"
        )
        if rstudio_connect_credentials is None:
            self.user = None
            return
        user_meta_data = json.loads(rstudio_connect_credentials)
        self.user = UserMetadata(**user_meta_data)

    @rx.var
    def greeting(self) -> str:
        if self.user is None:
            return "Howdy stranger!"
        return f"So nice to see you, {self.user.user}!"


def index():
    return rx.vstack(
        rx.text(State.greeting),
        rx.hstack(
            rx.button(
                "Decrement",
                color_scheme="ruby",
                on_click=State.decrement,
            ),
            rx.heading(State.count, font_size="2em"),
            rx.button(
                "Increment",
                color_scheme="grass",
                on_click=State.increment,
            ),
            spacing="4",
        ),
    )


app = rx.App()
app.add_page(index, on_load=State.get_current_user)
