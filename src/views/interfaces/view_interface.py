from abc import ABC, abstractmethod
from src.views.http_types import http_request
from src.views.http_types import http_response

class ViewInterace(ABC):

    @abstractmethod
    def handle(self, http_resquest: http_request) -> http_response:
        pass
