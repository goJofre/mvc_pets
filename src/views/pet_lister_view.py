from src.controllers.interfaces.pet_lister_controller import PetListerControllerInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from .interfaces.view_interface import ViewInterace

class PetListerView(ViewInterace):

    def __init__(self, controler: PetListerControllerInterface) -> None:
        self.__controler = controler

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        body_response = self.__controler.list_pets()

        return HttpResponse(status_code=200, body=body_response)
