import tkinter as tk
import requests

def search_book():
    isbn = entry.get()
    url = f'https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}'
    
    response = requests.get(url)
    data = response.json()
    
    if 'items' in data:
        title = data['items'][0]['volumeInfo']['title']
        authors = ', '.join(data['items'][0]['volumeInfo'].get('authors', ['著者情報なし']))
        result_label.config(text=f"タイトル: {title}\n著者: {authors}")
    else:
        result_label.config(text="本が見つかりませんでした")

root = tk.Tk()
root.title("簡単蔵書検索")

entry = tk.Entry(root)
entry.pack()

search_button = tk.Button(root, text="検索", command=search_book)
search_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
