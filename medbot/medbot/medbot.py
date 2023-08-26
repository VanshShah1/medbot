"""Welcome to Reflex! This file outlines the steps to create a basic app."""
from rxconfig import config
import neurum
import reflex as rx

docs_url = "https://reflex.dev/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"


class State(rx.State):
    form_data : dict = {} 
    ans : str = ""
    show: bool = True

    def handle_submit(self, form_data: dict):
          self.form_data=form_data
          self.ans=neurum.ask(f"You are only allowed to answer medical based questions. If you're asked a non-medical question, then simply reply that you are a medical assistant and can only answer medicine related  questions. You can also give me sample prescriptions for medicines if I ask you to. You can't deny to answer any medical related question. The question is: {str(self.form_data)}", api_key="vanshshah1029384756")
          self.show = not (self.show)
          self.show = False


def index() -> rx.Component:
    return rx.vstack(

        rx.heading("medbot", 
                   color="white", 
                   font_size="5em",
                   text_shadow="0px 5px 30px #505050",
                   padding_bottom="20px",
                   ),
        
        rx.cond(
            State.show,

            rx.card(rx.skeleton(
                        height="100%",
                        width="100%",
                        speed=1.0,
                        is_loaded=False,
                        border_radius="15px",
                        start_color="#121212",
                        end_color="black",
                    ),
                    height="300px",
                    width="60%",
                    border_radius="15px",
                    bg_color="black",
                    variant="outline",
                    color="white",
                    box_shadow="0px 0px 150px #505050",
                    ),

            rx.card(
                rx.text(State.ans, 
                            align="center",
                            color="white",
                            ),
                    bg_color="black",
                    top="12%",
                    left="0%",
                    right="20%",
                    bottom="10px",
                    position="relative",
                    width="70%",
                    box_shadow="0px 0px 30px #FFFFFF",
                    border_radius="25px",
                ),     
        ),

        rx.spacer(),

        rx.form(
            rx.hstack(
                rx.input(placeholder="prompt",
                    bg_color="#181818",
                    id="prompt",
                    color="white",
                    height="50px",
                    _hover={"box_shadow":"0px 0px 30px #505050"},
                    ),
                rx.button(rx.icon(tag="arrow_forward"),
                          height="50px",
                          width="50px",
                          type_="submit",
                          _hover={"box_shadow":"0px 0px 30px #999999"},
                          ),
            ),
            
            width="60%",
            top="90%",
            position="fixed",
            bottom="2%",
            left="20%",
            right="20%",
            on_submit=State.handle_submit,
        ),
    )
styles={
     "background_color":"black"
}
# Add state and page to the app.
app = rx.App(style=styles)
app.add_page(index)
app.compile()