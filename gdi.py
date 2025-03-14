import tkinter as tk
import random
import os
import sys

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("         ")
        self.state("zoomed")  # Размер окна на весь экран
        self.geometry("+0+0")  # Окно появляется в левом верхнем углу экрана
        self.attributes("-transparentcolor", "#ffffff")  # Прозрачный фон
        self.attributes("-topmost", True)  # Окно поверх других окон
        self.overrideredirect(True)  # Удаление рамок

        self.canvas = tk.Canvas(self, width=self.winfo_screenwidth(), height=self.winfo_screenheight(), bg="#ffffff")
        self.canvas.pack()

        self.figures = []
        self.create_figures()

        self.update()

    def create_figures(self):
        for _ in range(500):
            x = random.randint(0, self.winfo_screenwidth())
            y = random.randint(0, self.winfo_screenheight())
            width = random.randint(10, 100)
            height = random.randint(10, 100)
            color = self.random_color()
            speed_x = random.randint(-10, 10)
            speed_y = random.randint(-10, 10)

            if random.random() < 0.5:
                figure = self.canvas.create_rectangle(x, y, x + width, y + height, fill=color)
            else:
                figure = self.canvas.create_oval(x, y, x + width, y + height, fill=color)

            self.figures.append((figure, x, y, width, height, color, speed_x, speed_y))

    def update(self):
        for i, (figure, x, y, width, height, color, speed_x, speed_y) in enumerate(self.figures):
            x += speed_x
            y += speed_y

            if x < 0 or x + width > self.winfo_screenwidth():
                speed_x *= -1
            if y < 0 or y + height > self.winfo_screenheight():
                speed_y *= -1

            self.canvas.coords(figure, x, y, x + width, y + height)

            if random.random() < 0.5:
                self.canvas.delete(figure)
                del self.figures[i]

        if len(self.figures) < 500:
            self.create_figures()

        self.after(1, self.update)  # Обновление каждые 1 мс (около 1000 кадров в секунду)

    def random_color(self):
        return "#{:06x}".format(random.randint(0, 0xFFFFFF))

    def on_close(self):
        self.destroy()
        self.restart()

    def restart(self):
        os.execl(sys.executable, sys.executable, *sys.argv)

if __name__ == "__main__":
    app = Application()
    app.protocol("WM_DELETE_WINDOW", app.on_close)
    app.mainloop()