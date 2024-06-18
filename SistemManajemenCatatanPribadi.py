import csv
import tkinter as tk
from tkinter import ttk, messagebox, filedialog

class Catatan:
class ManajemenCatatan:

if __name__ == "__main__":
import csv
import tkinter as tk
from tkinter import ttk, messagebox, filedialog

class Catatan:
    def _init_(self, id_catatan, kategori, isi, tanggal):
        self.id_catatan = id_catatan
        self.kategori = kategori
        self.isi = isi
        self.tanggal = tanggal

class ManajemenCatatan:
    def _init_(self):
        self.catatan = []
        self.stack_dihapus = []

    def muat_catatan(self, filename):
        try:
            with open(filename, newline='', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile)
                next(reader)  # Skip header row
                self.catatan = [Catatan(row[0], row[1], row[2], row[3]) for row in reader]
        except FileNotFoundError:
            self.catatan = []

    def simpan_catatan(self, filename):
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['id_catatan', 'kategori', 'isi_catatan', 'tanggal'])
            for catatan in self.catatan:
                writer.writerow([catatan.id_catatan, catatan.kategori, catatan.isi, catatan.tanggal])

    def tambah_catatan(self, catatan):
        self.catatan.append(catatan)

    def perbarui_catatan(self, id_catatan, kategori, isi, tanggal):
        for catatan in self.catatan:
            if catatan.id_catatan == id_catatan:
                catatan.kategori = kategori
                catatan.isi = isi
                catatan.tanggal = tanggal
                return True
        return False

    def hapus_catatan(self, id_catatan):
        for catatan in self.catatan:
            if catatan.id_catatan == id_catatan:
                self.stack_dihapus.append(catatan)  # Tambahkan ke stack sebelum dihapus
                self.catatan.remove(catatan)
                return True
        return False

    def cari_catatan(self, kunci, nilai):
        hasil = []
        if kunci == "kategori":
            hasil = [catatan for catatan in self.catatan if nilai.lower() in catatan.kategori.lower()]
        elif kunci == "tanggal":
            nilai_format = nilai.replace("-", "")
            hasil = [catatan for catatan in self.catatan if nilai_format in catatan.tanggal.replace("-", "")]
        return hasil

    def urutkan_catatan(self, kunci):
        if kunci == "kategori":
            self.catatan.sort(key=lambda catatan: catatan.kategori.lower())
        elif kunci == "tanggal":
            self.catatan.sort(key=lambda catatan: catatan.tanggal.replace("-", ""), reverse=True)

    def pulihkan_catatan(self):
        if self.stack_dihapus:
            catatan_dipulihkan = self.stack_dihapus.pop()
            self.catatan.append(catatan_dipulihkan)
            return True
        return False

class Aplikasi(tk.Tk):
    def _init_(self, manajemen_catatan):
        super()._init_()
        self.manajemen_catatan = manajemen_catatan
        self.title("Sistem Manajemen Catatan Pribadi")
        self.geometry("1200x700")

        self.style = ttk.Style(self)
        self.style.configure('TButton', padding=6, relief='flat', background='#ccc')
        self.style.configure('TFrame', padding=10)
        self.style.configure('Treeview', rowheight=25)
        self.style.configure('Treeview.Heading', font=('Helvetica', 12, 'bold'))

        self.buat_widget()

    def buat_widget(self):
        self.tree = ttk.Treeview(self, columns=("ID", "Kategori", "Isi", "Tanggal"), show='headings')
        self.tree.column("ID", width=100, anchor=tk.CENTER)
        self.tree.column("Kategori", width=100, anchor=tk.CENTER)
        self.tree.column("Isi", stretch=True)
        self.tree.column("Tanggal", width=100, anchor=tk.CENTER)
        self.tree.heading("ID", text="ID", anchor=tk.CENTER)
        self.tree.heading("Kategori", text="Kategori", anchor=tk.CENTER)
        self.tree.heading("Isi", text="Isi")
        self.tree.heading("Tanggal", text="Tanggal", anchor=tk.CENTER)
        self.tree.pack(expand=True, fill='both', pady=10, padx=10)
