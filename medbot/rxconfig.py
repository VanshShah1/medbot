import reflex as rx

class MedbotConfig(rx.Config):
    pass

config = MedbotConfig(
    app_name="medbot",
    db_url="sqlite:///reflex.db",
    env=rx.Env.DEV,
)