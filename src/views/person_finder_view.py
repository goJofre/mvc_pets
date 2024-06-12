from src.controllers.interfaces.person_finder_controller import PersonFinderControllerInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from .interfaces.view_interface import ViewInterace

class PersonFinderView(ViewInterace):

    def __init__(self, controler: PersonFinderControllerInterface) -> None:
        self.__controler = controler

    def handle(self, http_resquest: HttpRequest) -> HttpResponse:
        person_id = http_resquest.param["person_id"]
        body_response = self.__controler.find(person_id)

        return HttpResponse(status_code=200, body=body_response)
