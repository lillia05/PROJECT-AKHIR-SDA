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

        self.frame = ttk.Frame(self)
        self.frame.pack(fill='x')

        self.tombol_muat = ttk.Button(self.frame, text="Muat", command=self.muat_catatan)
        self.tombol_muat.pack(side='left', padx=5)

        self.tombol_simpan = ttk.Button(self.frame, text="Simpan", command=self.simpan_catatan)
        self.tombol_simpan.pack(side='left', padx=5)

        self.tombol_tambah = ttk.Button(self.frame, text="Tambah", command=self.tambah_catatan)
        self.tombol_tambah.pack(side='left', padx=5)

        self.tombol_perbarui = ttk.Button(self.frame, text="Perbarui", command=self.input_perbarui_catatan)
        self.tombol_perbarui.pack(side='left', padx=5)

        self.tombol_hapus = ttk.Button(self.frame, text="Hapus", command=self.hapus_catatan)
        self.tombol_hapus.pack(side='left', padx=5)

        self.tombol_cari = ttk.Button(self.frame, text="Cari", command=self.cari_catatan)
        self.tombol_cari.pack(side='left', padx=5)

        self.tombol_urutkan = ttk.Button(self.frame, text="Urutkan", command=self.urutkan_catatan)
        self.tombol_urutkan.pack(side='left', padx=5)

        self.tombol_pulihkan = ttk.Button(self.frame, text="Pulihkan", command=self.pulihkan_catatan)
        self.tombol_pulihkan.pack(side='left', padx=5)

    def muat_catatan(self):
        filename = filedialog.askopenfilename(filetypes=[("File CSV", "*.csv")])
        if filename:
            self.manajemen_catatan.muat_catatan(filename)
            self.perbarui_tree()
            messagebox.showinfo("Sukses", "Catatan berhasil dimuat!")

    def simpan_catatan(self):
        filename = filedialog.asksaveasfilename(filetypes=[("File CSV", "*.csv")])
        if filename:
            self.manajemen_catatan.simpan_catatan(filename)
            messagebox.showinfo("Sukses", "Catatan berhasil disimpan!")

    def tambah_catatan(self):
        self.edit_catatan()

    def input_perbarui_catatan(self):
        item_terpilih = self.tree.selection()
        if item_terpilih:
            id_catatan = self.tree.item(item_terpilih[0])['values'][0]
            catatan = next((n for n in self.manajemen_catatan.catatan if n.id_catatan == id_catatan), None)
            if catatan:
                self.edit_catatan(catatan, id_catatan)

    def hapus_catatan(self):
        self.input_hapus_catatan()

    def input_hapus_catatan(self):
        self.jendela_hapus = tk.Toplevel(self)
        self.jendela_hapus.title("Hapus Catatan")

        tk.Label(self.jendela_hapus, text="Masukkan ID Catatan yang ingin dihapus:").grid(row=0, column=0, padx=5, pady=5)
        self.id_hapus = tk.Entry(self.jendela_hapus)
        self.id_hapus.grid(row=0, column=1, padx=5, pady=5)

        ttk.Button(self.jendela_hapus, text="Hapus", command=self.konfirmasi_hapus_catatan).grid(row=1, column=0, columnspan=2, pady=5)

    def konfirmasi_hapus_catatan(self):
        id_catatan = self.id_hapus.get()
        if self.manajemen_catatan.hapus_catatan(id_catatan):
            self.perbarui_tree()
            messagebox.showinfo("Sukses", "Catatan berhasil dihapus!")
        else:
            messagebox.showerror("Error", "ID Catatan tidak ditemukan!")
        self.jendela_hapus.destroy()

    def cari_catatan(self):
        self.jendela_cari = tk.Toplevel(self)
        self.jendela_cari.title("Cari Catatan")

        tk.Label(self.jendela_cari, text="Cari Berdasarkan:").grid(row=0, column=0, padx=5, pady=5)
        self.kunci_cari = ttk.Combobox(self.jendela_cari, values=["kategori", "tanggal"])
        self.kunci_cari.grid(row=0, column=1, padx=5, pady=5)
        self.kunci_cari.current(0)

        tk.Label(self.jendela_cari, text="Nilai:").grid(row=1, column=0, padx=5, pady=5)
        self.nilai_cari = tk.Entry(self.jendela_cari)
        self.nilai_cari.grid(row=1, column=1, padx=5, pady=5)

        ttk.Button(self.jendela_cari, text="Cari", command=self.konfirmasi_cari_catatan).grid(row=2, column=0, columnspan=2, pady=5)
