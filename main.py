import os
import random
import tkinter as tk
from tkinter import messagebox, Entry, Label, Frame
from PIL import Image, ImageTk
from fuzzywuzzy import fuzz

# plant_families = ['Asteraceae', 'Orchidaceae', 'Dubs']
plant_families = ['Asteraceae', 'Adoxaceae', 'Berberidaceae', 'Plantaginaceae', 'Apiaceae', 'Iridaceae', 'Polemoniaceae', 'Rosaceae', 'Onagraceae', 'Aceraceae', 'Hamamelidaceae', 'Oleaceae', 'Brassicaceae', 'Lauraceae', 'Araceae', 'Fagaceae', 'Salicaceae', 'Violaceae', 'Saxifragaceae', 'Fabaceae', 'Caryophyllaceae', 'Cactaceae', 'Montiaceae', 'Ericaceae', 'Cornaceae', "Dubs", 'Solanaceae', 'Hydrophyllaceae', 'Boraginaceae', 'Juncaceae', 'Cyperaceae', 'Poaceae', 'Typhaceae', 'Orchidaceae', 'Liliaceae', 'Magnoliaceae', 'Betulaceae', 'Ranunculaceae', 'Lamiaceae', 'Caprifoliaceae']

random.shuffle(plant_families)

class App:
    def __init__(self, master):
        self.master = master
        self.current_index = 0
        self.incorrect_answers = []
        self.image_frame = None
        self.answer_entry = None
        self.master.title("Plant Family Quiz")
        self.master.geometry("1000x900")
        self.create_widgets()

    def create_widgets(self):
        if self.image_frame:
            self.image_frame.destroy()

        if self.answer_entry:
            self.answer_entry.destroy()

        if self.current_index < len(plant_families):
            self.image_frame = Frame(self.master)
            self.images = [ImageTk.PhotoImage(Image.open(os.path.join('img', plant_families[self.current_index], f'Image_{i+1}.jpg')).resize((400,350))) for i in range(4)]
            random.shuffle(self.images)
            for i, img in enumerate(self.images):
                label = tk.Label(self.image_frame, image=img)
                label.grid(row=i//2, column=i%2)

            self.image_frame.pack()

            self.answer_entry = tk.Entry(self.master, font=("arial", 24), fg="white", bg="black")
            self.answer_entry.pack()
            self.answer_entry.focus_set()
            self.answer_entry.bind("<Return>", self.check_answer)
        else:
            self.show_summary()

    def check_answer(self, event=None):
        answer = self.answer_entry.get().strip()
        correct_answer = plant_families[self.current_index]
        if answer.lower() == correct_answer.lower():
            messagebox.showinfo("Correct", "You got it right!")
            self.answer_entry.delete(0, tk.END)
            self.current_index += 1
            self.create_widgets()

        elif fuzz.ratio(answer.lower(), correct_answer.lower()) >= 80:
            messagebox.showinfo("Close", "You were close!")
        else:
            # plant_families.append(correct_answer)
            messagebox.showinfo("Incorrect", f"You got it wrong! The correct answer is {correct_answer}")
            self.incorrect_answers.append((answer, correct_answer))
            self.answer_entry.delete(0, tk.END)
            self.create_widgets()

    def show_summary(self):
        summary_label = tk.Label(self.master, text="Congratulations, you've finished the quiz!", font=("arial", 24))
        summary_label.pack()

        if self.incorrect_answers:
            incorrect_label = tk.Label(self.master, text="You had trouble with the following plant families:", font=("arial", 20))
            incorrect_label.pack()

            incorrect_flowers = [flower[1] for flower in self.incorrect_answers]
            unique_incorrect_answers = set(incorrect_flowers)
            error_rate = len(unique_incorrect_answers) / len(plant_families) * 100

            for answer, correct_answer in self.incorrect_answers:
                if len(answer) < 1 or answer == "idk":
                    family_label = tk.Label(self.master, text=f"You didn't know: {correct_answer}")
                else:
                    family_label = tk.Label(self.master, text=f"Your answer: {answer} | Correct answer: {correct_answer}")
                family_label.pack()

            error_rate_label = tk.Label(self.master, text=f"Accuracy: {100 - error_rate:.2f}%     :D", font=("arial", 20))
            error_rate_label.pack()
        else:
            perfect_label = tk.Label(self.master, text="You got all the plant families correct, great job!", font=("arial", 24))
            perfect_label.pack()

root = tk.Tk()
app = App(root)
root.mainloop()