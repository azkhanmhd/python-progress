import time
import tkinter as tk


def currentTime():
    getTime = time.strftime("%H:%M:%S")
    showTime.config(text=getTime)
    showTime.after(1000, currentTime)

window = tk.Tk()
window.geometry("300x100")
window.resizable(False, False)
window.title("---Clock---")
window.configure(bg="black")

showTime = tk.Label(window, font=("Arial", 50), fg="lime", bg="black")
showTime.place(relx=0.5, rely=0.5, anchor="center")


currentTime()
window.mainloop()
