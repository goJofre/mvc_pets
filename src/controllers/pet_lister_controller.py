from src.models.sqlite.interfaces.pets_repository import PetsRepositoryInterface
from src.models.sqlite.entities.pets import PetsTable
from .interfaces.pet_lister_controller import PetListerControllerInterface

class PetListerController(PetListerControllerInterface):
    def __init__(self, pet_repository: PetsRepositoryInterface) -> None:
        self.__pet_repository = pet_repository

    def list_pets(self) -> dict:
        pets = self.__get_pets_in_db()
        response_formated = self.__format_response(pets)
        return response_formated

    def __get_pets_in_db(self) -> list[PetsTable]:
        pets = self.__pet_repository.list_pets()
        return pets

    def __format_response(self, pets: list[PetsTable]) -> dict:
        formatted_pets = []
        for pet in pets:
            formatted_pet = {
                "id": pet.id,
                "name": pet.name,
                "type": pet.type,
            }
            formatted_pets.append(formatted_pet)

        return {
            "data": {
                "type": "Pets",
                "count": len(pets),
                "attributes": {
                     "pets": formatted_pets
                }
            }
        }
