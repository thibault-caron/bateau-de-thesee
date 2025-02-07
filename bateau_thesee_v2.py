# Définir la classe Part
class Part:
    def __init__(self, name, material):
        self.name = name
        self.material = material

    def change_material(self, new_material):
        """Changer le matériau de la pièce."""
        self.material = new_material

    def __str__(self):
        """Retourner une description de la pièce."""
        return f"Pièce: {self.name}, Matériau: {self.material}"


class Ship(Part):
    """Définir la classe Ship, héritant de Part"""
    def __init__(self, name):
        super().__init__(name, "N/A") 
        self.__parts = {}

    def add_part(self, part):
        """Ajouter une pièce au bateau."""
        self.__parts[part.name] = part

    def display_state(self):
        """Afficher l'état du bateau avec la liste des pièces."""
        print(f"État du bateau '{self.name}':")
        if not self.__parts:
            print("Aucune pièce à afficher.")
        else:
            for part in self.__parts.values():
                print(part)

    def replace_part(self, part_name, new_part):
        """Remplacer une pièce existante par une nouvelle."""
        if part_name in self.__parts:
            print(f"Remplacement de la pièce: {part_name}")
            self.__parts[part_name] = new_part
        else:
            print(f"Aucune pièce trouvée avec le nom '{part_name}'")

    def change_part(self, part_name, new_material):
        """Changer le matériau d'une pièce existante."""
        if part_name in self.__parts:
            print(f"Changement du matériau de la pièce '{part_name}' en '{new_material}'")
            self.__parts[part_name].change_material(new_material)
        else:
            print(f"Aucune pièce trouvée avec le nom '{part_name}'")


class RacingShip(Ship):
    """classe RacingShip, héritant de Ship"""
    def __init__(self, name, max_speed):
        super().__init__(name)
        self.max_speed = max_speed

    def display_speed(self):
        """Afficher la vitesse maximale du RacingShip."""
        print(f"Vitesse maximale du '{self.name}' : {self.max_speed} km/h")


if __name__ == "__main__":
    # Création des pièces
    piece1 = Part("Coque", "Bois")
    piece2 = Part("Mât", "Bois")
    piece3 = Part("Voile", "Toile")

    # Création du bateau
    bateau = RacingShip("Bateau de Thésée", "120")
    
    # Ajouter les pièces au bateau
    bateau.add_part(piece1)
    bateau.add_part(piece2)
    bateau.add_part(piece3)
    
    # Afficher l'état du bateau
    bateau.display_state()
    bateau.display_speed()
    
    # # Remplacer une pièce
    # new_piece = Part("Coque", "Acier")
    # bateau.replace_part("Coque", new_piece)
    
    # # Afficher l'état du bateau après remplacement
    # bateau.display_state()

    # # Changer le matériau d'une pièce existante
    # bateau.change_part("Mât", "Acier")
    # bateau.display_state()
