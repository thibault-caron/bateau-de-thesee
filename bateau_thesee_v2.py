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
        self.history = []

    def add_part(self, part):
        """Ajouter une pièce au bateau."""
        self.__parts[part.name] = part
        self.history.append(f"Ajout de la pièce: {part.name} ({part.material})")

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
            self.history.append(f"Remplacement de la pièce '{part_name}' par '{new_part.name}' ({new_part.material})")
            print(f"Remplacement de la pièce: {part_name}")
            self.__parts[part_name] = new_part
        else:
            print(f"Aucune pièce trouvée avec le nom '{part_name}'")

    def change_part(self, part_name, new_material):
        """Changer le matériau d'une pièce existante."""
        if part_name in self.__parts:
            old_material = self.__parts[part_name].material
            self.__parts[part_name].change_material(new_material)
            self.history.append(f"Changement du matériau de la pièce '{part_name}' de '{old_material}' à '{new_material}'")
            print(f"Changement du matériau de '{part_name}' en '{new_material}'.")
        else:
            print(f"Aucune pièce trouvée avec le nom '{part_name}'")

    def display_history(self):
        """Afficher l'historique des modifications."""
        if not self.history:
            print("Aucune modification n'a été effectuée.")
        else:
            print("Historique des modifications:")
            for record in self.history:
                print(record)


class RacingShip(Ship):
    """classe RacingShip, héritant de Ship"""
    def __init__(self, name, max_speed):
        super().__init__(name)
        self.max_speed = max_speed

    def display_speed(self):
        """Afficher la vitesse maximale du RacingShip."""
        print(f"Vitesse maximale du '{self.name}' : {self.max_speed} noeuds")


def show_menu():
    """Fonction pour afficher le menu"""
    print("\n--- Menu ---")
    print("1. Ajouter une pièce")
    print("2. Remplacer une pièce")
    print("3. Modifier le matériau d'une pièce")
    print("4. Afficher l'état du bateau")
    print("5. Afficher l'historique des modifications")
    print("6. Quitter")


def menu_interactif(bateau):
    """Fonction pour gérer les choix du menu"""
    while True: 
        choice = input("Choisissez une option ('0' pour afficher les options): ")
        if choice == "0":
            show_menu()
        elif choice == "1":
            part_name = input("Nom de la pièce à ajouter: ")
            material = input("Matériau de la pièce: ")
            new_part = Part(part_name, material)
            bateau.add_part(new_part)
        elif choice == "2":
            part_name = input("Nom de la pièce à remplacer: ")
            new_part_name = input("Nom de la nouvelle pièce: ")
            new_material = input("Matériau de la nouvelle pièce: ")
            new_part = Part(new_part_name, new_material)
            bateau.replace_part(part_name, new_part)
        elif choice == "3":
            part_name = input("Nom de la pièce à modifier: ")
            new_material = input("Nouveau matériau: ")
            bateau.change_part(part_name, new_material)
        elif choice == "4":
            bateau.display_state()
        elif choice == "5":
            bateau.display_history()
        elif choice == "6":
            print("Quitter le programme.")
            break
        else:
            print("Choix invalide. Veuillez essayer à nouveau.")


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
    
    # Démarrer le menu interactif
    menu_interactif(bateau)
