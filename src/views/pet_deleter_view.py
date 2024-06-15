from src.controllers.interfaces.pet_deleter_controller import PetDeleterControllerInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from .interfaces.view_interface import ViewInterace

class PetDeleterView(ViewInterace):

    def __init__(self, controler: PetDeleterControllerInterface) -> None:
        self.__controler = controler

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        name = http_request.param["name"]
        self.__controler.delete(name)

        return HttpResponse(status_code=204)
