from src.models.sqlite.entities.pets import PetsTable
from .pet_lister_controller import PetListerController

class MockPetsRepository:
    def list_pets(self):
        return [
            PetsTable(id = 4, name="Fluffy", type="Cat"),
            PetsTable(id=47, name="Buddy", type="Dog"),
        ]

def test_list_pets():
    controller =  PetListerController(MockPetsRepository())
    response = controller.list_pets()

    expected_response = {
         "data": {
                "type": "Pets",
                "count": 2,
                "attributes": {
                     "pets": [
                         {"id": 4, "name": "Fluffy", "type": "Cat"},
                         {"id": 47, "name": "Buddy", "type": "Dog"}
                     ]
                }
            }
    }

    assert response == expected_response
