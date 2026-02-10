
import customtkinter as ctk


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        #Columnas
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)
        self.grid_columnconfigure(2, weight=1)
        #Columnas
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)


        self.title("My love proposal")
        self.geometry("400x240")


        self.label = ctk.CTkLabel(self, text="¿Quieres ser mi San Valentin?", font=("Arial", 20))
        self.label.grid(row=0, column=1, padx=10, pady=10)

        self.yes_button = ctk.CTkButton(self, text="Siiii", command=self.button_callback)
        self.yes_button.grid(row=1, column=0, padx=10, pady=10)

        self.no_button = ctk.CTkButton(self, text="noooo", command=self.button_callback)
        self.no_button.grid(row=1, column=2, padx=10, pady=10)

    def button_callback(self):
        print("Botón presionado")



if __name__ == "__main__":
    app = App()
    app.mainloop()