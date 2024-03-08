from .routers import all_controllers
from ninja_extra import NinjaExtraAPI

app = NinjaExtraAPI(app_name="Online Shop")


app.register_controllers(
    *all_controllers
)