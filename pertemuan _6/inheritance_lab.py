class Perangkat:
    def __init__(self, merk):
        self.merk = merk
        print(f"Inisialisasi Perangkat: {self.merk}")

    def info(self):
        print(f"Ini adalah perangkat merk {self.merk}")

class Smartphone(Perangkat):
    def __init__(self, merk):
        super().__init__(merk)
        print("Fitur Smartphone: Bisa menelepon.")

    def info(self):
        super().info()
        print("Menambahkan detail: Perangkat ini memiliki koneksi 5G.")

class Kamera(Perangkat):
    def __init__(self, merk):
        super().__init__(merk)
        print("Fitur Kamera: Bisa memotret resolusi tinggi.")

    def info(self):
        print("Menambahkan detail: Perangkat ini memiliki sensor optik.")

class SmartphoneKamera(Smartphone, Kamera):
    def __init__(self, merk):
        super().__init__(merk)
        print("SmartphoneKamera siap digunakan!")

    def tampilkan_info(self):
        print(f"\n--- Info Produk: {self.merk} ---")
        super().info()

gadget = SmartphoneKamera("Samsung")
gadget.tampilkan_info()

print("\nUrutan MRO:")
for cls in SmartphoneKamera.mro():
    print(cls.__name__)