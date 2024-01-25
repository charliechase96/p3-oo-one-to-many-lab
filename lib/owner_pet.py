class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]

    all = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner

        if owner:
            owner.add_pet(self)

        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet type: {pet_type}. Must be one of {Pet.PET_TYPES}")
        
        Pet.all.append(self)
    
    def set_owner(self, owner):
        if not isinstance(owner, Owner):
            raise Exception("Owner must be an instance of Owner class")
        self.owner = owner

class Owner:
    def __init__(self, name):
        self.name = name
        self._pets = []
    
    def pets(self):
        return self._pets
    
    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Pet must be an instance of Pet class")
        pet.set_owner(self)
        self._pets.append(pet)
    
    def sort_pets_by_name(self):
        return sorted(self._pets, key=self.get_sorted_pets)
    
    def get_sorted_pets(self):
        return sorted(self._pets, key=lambda pet: pet.name)