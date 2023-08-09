from icrawler.builtin import GoogleImageCrawler
from tkinter import *
from tkinter import messagebox,filedialog

root = Tk()
root["bg"] = "grey"
root.title("Parser image by _sineD_0")

name = StringVar()
quantity = StringVar()
path = StringVar()

def parse():
    try:
        path.set(filedialog.askdirectory(title="сохранить в"))
        google_crawler = GoogleImageCrawler(storage={'root_dir': path.get()})
        google_crawler.crawl(keyword=name.get(), max_num=int(quantity.get()))
        messagebox.showinfo("INFO",f"картинки успешно скачаны в {path.get()}")
    except Exception:
        messagebox.showerror("ERROR","неизвестная ошыбка")
help_text_for_name = Label(text="По какому запросу искать картинки",bg="grey")
name_input = Entry(textvariable=name,bg="grey")
help_text_for_quantity = Label(text="По какому запросу искать картинки",bg="grey")
quantity_input = Entry(textvariable=quantity,bg="grey")
path_btn = Button(text="сохранить",bg="grey",command=parse)

help_text_for_name.pack()
name_input.pack()
help_text_for_quantity.pack()
quantity_input.pack()
path_btn.pack()

root.mainloop()