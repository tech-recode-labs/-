import tkinter as tk

root = tk.Tk()  # ウィンドウを作る
root.title("こんにちはTkinter")

label = tk.Label(root, text="Hello, World!")
label.pack()

button = tk.Button(root, text="クリックしてね", command=lambda: label.config(text="クリックされた！"))
button.pack()

root.mainloop()  # ウィンドウを表示し続ける
