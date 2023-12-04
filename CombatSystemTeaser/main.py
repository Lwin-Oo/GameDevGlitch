import tkinter as tk
from tkinter import messagebox, simpledialog
import random

class Action:
    def player_move(self):
        return "You have moved!"

    def player_attack(self, skill, damage):
        return f"You have used {skill} for {damage} damage!"

class Token:
    def __init__(self, movement_token, attack_token):
        self.movement_token = movement_token
        self.attack_token = attack_token

    def count_movement_token(self):
        if self.movement_token > 0:
            self.movement_token -= 1
            return True
        else:
            return False

    def count_attack_token(self):
        if self.attack_token > 0:
            self.attack_token -= 1
            return True
        else:
            return False

class Dragon:
    def __init__(self, strength):
        self.strength = strength

    def receive_damage(self, damage):
        self.strength -= damage
        if self.strength < 0:
            self.strength = 0

    def is_defeated(self):
        return self.strength == 0

class Player:
    def __init__(self, movement_tokens, attack_tokens):
        self.movement_tokens = movement_tokens
        self.attack_tokens = attack_tokens

    def move(self):
        if self.movement_tokens > 0:
            self.movement_tokens -= 1
            return True
        else:
            messagebox.showinfo("No more movement tokens!", "You cannot move anymore.")
            return False

    def attack(self):
        if self.attack_tokens > 0:
            skill_choice = simpledialog.askinteger("Skill Choice", "Enter your skill choice (1-3):", minvalue=1, maxvalue=3)
            if skill_choice:
                self.attack_tokens -= 1
                return skill_choice
        else:
            messagebox.showinfo("No more attack tokens!", "You cannot attack anymore.")
            return 0

class DragonGameGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Dragon Slayer Game")

        self.dragon = Dragon(strength=30)
        self.player = Player(movement_tokens=3, attack_tokens=3)
        self.action = Action()
        self.token = Token(movement_token=self.player.movement_tokens, attack_token=self.player.attack_tokens)

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.master, text="You have encountered a dragon!!!", font=("Helvetica", 14))
        self.label.pack(pady=10)

        self.move_button = tk.Button(self.master, text="Move", command=self.move_action)
        self.move_button.pack(pady=5)

        self.attack_button = tk.Button(self.master, text="Attack", command=self.attack_action)
        self.attack_button.pack(pady=5)

        self.quit_button = tk.Button(self.master, text="Quit", command=self.master.destroy)
        self.quit_button.pack(pady=10)

    def move_action(self):
        if self.player.move():
            movement_choice = messagebox.askquestion("Movement", "Wanna move closer or further?")
            if movement_choice == "yes":
                self.label.config(text="You have moved closer!")
            else:
                self.label.config(text="You have moved further!")

    def attack_action(self):
        skill_choice = self.player.attack()
        if skill_choice:
            damage = 0
            if skill_choice == 1:
                damage = random.randint(5, 10)
            elif skill_choice == 2:
                damage = random.randint(10, 15)
            elif skill_choice == 3:
                damage = random.randint(15, 20)

            result_message = self.action.player_attack(f"Skill {skill_choice}", damage)
            self.dragon.receive_damage(damage)

            if self.dragon.is_defeated():
                result_message += "\n\nCongratulations! You have defeated the dragon!"
                self.disable_buttons()
            else:
                result_message += f"\nDragon's strength: {self.dragon.strength}"

            self.label.config(text=result_message)

    def disable_buttons(self):
        self.move_button.config(state=tk.DISABLED)
        self.attack_button.config(state=tk.DISABLED)


def main():
    root = tk.Tk()
    app = DragonGameGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
