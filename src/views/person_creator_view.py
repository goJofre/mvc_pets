from src.controllers.interfaces.person_creator_controller import PersonCreatorControllerInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from .interfaces.view_interface import ViewInterace

class PersonCreatorView(ViewInterace):

    def __init__(self, controller: PersonCreatorControllerInterface) -> None:
        self.__controller = controller

    def handle(self, http_resquest: HttpRequest) -> HttpResponse:
        person_info = http_resquest.body
        body_response = self.__controller.create(person_info)

        return HttpResponse(status_code=201,  body=body_response)
