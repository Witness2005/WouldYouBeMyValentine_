import customtkinter as ctk
import os
import sys
import subprocess

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("My love proposal")
        self.geometry("400x240")
        self.configure(fg_color="#FFC0CB")

        self.grid_columnconfigure((0, 1, 2), weight=1)
        self.grid_rowconfigure((0, 1), weight=1)
        self.label = ctk.CTkLabel(
            self,
            text="¿Quieres ser mi San Valentin🥺🥺🥺?",
            font=("Arial", 20, "bold"),
            text_color="black"
        )
        self.label.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

        self.yes_button = ctk.CTkButton(
            self,
            text="Siiii",
            command=lambda: self.ejecutar_video(resource_path("yesCase.mp4"))
        )
        self.yes_button.grid(row=1, column=0, padx=10, pady=10)

        self.no_button = ctk.CTkButton(
            self,
            text="noooo",
            fg_color="#D32F2F",
            hover_color="#B71C1C",
            command=lambda: self.ejecutar_video(resource_path("noCase.mp4"))
        )
        self.no_button.grid(row=1, column=2, padx=10, pady=10)

    def ejecutar_video(self, ruta_video):
        if not os.path.exists(ruta_video):
            print(f"Error: No encuentro el archivo {ruta_video}")
            return

        if sys.platform == "win32":
            os.startfile(ruta_video)
        elif sys.platform == "darwin":
            subprocess.call(["open", ruta_video])
        else:
            subprocess.call(["xdg-open", ruta_video])


if __name__ == "__main__":
    app = App()
    app.mainloop()