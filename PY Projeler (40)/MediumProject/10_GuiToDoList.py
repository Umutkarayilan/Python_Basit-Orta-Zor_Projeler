import tkinter as tk  # GUI için kullanılır
from tkinter import messagebox

# Ana pencereyi oluşturur
root = tk.Tk()
root.title("To-Do List")

# Görev listesi için liste kutusu
gorev_listesi = tk.Listbox(root, width=50, selectmode=tk.SINGLE)
gorev_listesi.pack(pady=10)

# Yeni görev eklemek için giriş alanı
gorev_entry = tk.Entry(root, width=40)
gorev_entry.pack(pady=5)

# Görev ekleme fonksiyonu
def ekle_gorev():
    gorev = gorev_entry.get()
    if gorev:
        gorev_listesi.insert(tk.END, gorev)
        gorev_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Uyarı", "Boş görev eklenemez.")

# Görev silme fonksiyonu
def sil_gorev():
    secilen = gorev_listesi.curselection()
    if secilen:
        gorev_listesi.delete(secilen)
    else:
        messagebox.showwarning("Uyarı", "Silinecek görev seçin.")

# Butonları oluşturur
ekle_button = tk.Button(root, text="Görev Ekle", command=ekle_gorev)
ekle_button.pack(pady=5)

sil_button = tk.Button(root, text="Görev Sil", command=sil_gorev)
sil_button.pack(pady=5)

# Uygulamayı çalıştırır
root.mainloop()
