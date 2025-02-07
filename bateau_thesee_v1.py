class Part:
    def __init__(self, name, material):
        self.name = name
        self.material = material

    def change_material(self, new_material):
        self.material = new_material

    def __str__(self):
        return f"part name: {self.name}\npart material: {self.material}"
    

class Ship(Part):
    def __init__(self, name, material, name_ship, parts):
        super().__init__(name, material)
        self.__name_ship = name_ship
        self.__parts = {part.name for part in parts}

    def display_state(self):
        for part in self.__parts.values():
            print(f"part: {part}")
    
    def replace_part(self, part_name, new_part):
        self.name = part_name
        self.__parts[part_name] = new_part
        return self.__parts
    
bateau = Ship("coque", "metal", "bato test", {Part("coque", "metal"), Part("mat", "bois"), Part("voile", "jute")})

bateau.display_state()