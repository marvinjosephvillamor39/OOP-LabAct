class FlamesGame:
    def __init__(self, name1, name2):
        self.name1 = name1.replace(' ', '').lower()
        self.name2 = name2.replace(' ', '').lower()

    def remove_common_letters(self):
        for ch in self.name1[:]:  # Iterate over a copy of name1
            if ch in self.name2:
                self.name1 = self.name1.replace(ch, "", 1)
                self.name2 = self.name2.replace(ch, "", 1)

    def calculate_count(self):
        return len(self.name1) + len(self.name2)

    def get_relationship_status(self):
        flames_list = ["Friends", "Lovers", "Affection", "Marriage", "Enemy", "Sibling"]
        
        while len(flames_list) > 1:
            count = self.calculate_count()
            split_index = (count % len(flames_list)) - 1
            
            if split_index >= 0:
                flames_list = flames_list[split_index + 1:] + flames_list[:split_index]
            else:
                flames_list = flames_list[:len(flames_list) - 1]
        
        return flames_list[0]

if __name__ == "__main__":
    # Get input from the user
    name1 = input("Enter the first name: ")
    name2 = input("Enter the second name: ")
    
    flames_game = FlamesGame(name1, name2)
    
    flames_game.remove_common_letters()
    
    relationship = flames_game.get_relationship_status()
    print("Relationship:", relationship)
