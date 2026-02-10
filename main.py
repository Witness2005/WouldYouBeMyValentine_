
import customtkinter as ctk


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class App(ctk.CTk):
    def __init__(self):
        super().__init__()


        self.title("My love proposal")
        self.geometry("400x240")


        self.label = ctk.CTkLabel(self, text="Texto de Prueba", font=("Arial", 20))
        self.label.pack(pady=40)

        self.button = ctk.CTkButton(self, text="Click", command=self.button_callback)
        self.button.pack(pady=10)

    def button_callback(self):
        print("Botón presionado")


if __name__ == "__main__":
    app = App()
    app.mainloop()