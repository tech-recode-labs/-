import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO

# 外部ファイルからアプリIDを読み込み
with open('config.txt', 'r') as f:
    applicationId = f.readline().strip()

def search_book(event=None):
    isbn = entry.get()
    url = f'https://app.rakuten.co.jp/services/api/BooksBook/Search/20170404?format=json&isbn={isbn}&applicationId={applicationId}'
    
    response = requests.get(url)
    data = response.json()
    
    if 'Items' in data and data['Items']:
        item = data['Items'][0]['Item']
        title = item['title']
        author = item['author']
        image_url = item['mediumImageUrl']
        
        result_label.config(text=f"タイトル: {title}\n著者: {author}")
        
        # 画像取得と表示
        img_data = requests.get(image_url).content
        img = Image.open(BytesIO(img_data))
        img = img.resize((100, 150))  # サイズ調整
        photo = ImageTk.PhotoImage(img)
        image_label.config(image=photo)
        image_label.image = photo  # 参照保持
    else:
        result_label.config(text="本が見つかりませんでした")
        image_label.config(image='')  # 画像クリア
    
    entry.delete(0, tk.END)
    entry.focus_set()

root = tk.Tk()
root.title("楽天APIで蔵書検索")

entry = tk.Entry(root)
entry.pack()
entry.bind("<Return>", search_book)
entry.focus_set()

search_button = tk.Button(root, text="検索", command=search_book)
search_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

image_label = tk.Label(root)
image_label.pack()

root.lift()
root.attributes('-topmost', True)
root.after_idle(root.attributes, '-topmost', False)

root.mainloop()
