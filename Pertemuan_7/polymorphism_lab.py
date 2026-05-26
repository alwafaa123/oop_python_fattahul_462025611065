
class AlatPembayaran:
    def proses_bayar(self, jumlah):
        raise NotImplementedError("Subclass harus mengimplementasikan metode ini!")

class KartuKredit(AlatPembayaran):
    def __init__(self, nomor_kartu):
        self.nomor_kartu = nomor_kartu

    def proses_bayar(self, jumlah):
        biaya_admin = 5000
        total = jumlah + biaya_admin
        print(f"[Kartu Kredit {self.nomor_kartu}] Memproses pembayaran...")
        print(f"-> Jumlah: Rp{jumlah} + Admin: Rp{biaya_admin} | Total Dipotong: Rp{total}")

class EWallet(AlatPembayaran):
    def __init__(self, nomor_hp):
        self.nomor_hp = nomor_hp

    def proses_bayar(self, jumlah):
        # Logika unik untuk E-Wallet (ada cashback)
        cashback = jumlah * 0.05  # Cashback 5%
        print(f"[E-Wallet {self.nomor_hp}] Memproses pembayaran...")
        print(f"-> Uang keluar: Rp{jumlah} | Anda mendapatkan Cashback: Rp{int(cashback)}")


def jalankan_transaksi(objek_pembayaran, jumlah):
    print("\n--- Memulai Transaksi Baru ---")
    objek_pembayaran.proses_bayar(jumlah)

pembayaran_cc = KartuKredit("4560-1234-8888")
pembayaran_ovo = EWallet("081234567890")

jalankan_transaksi(pembayaran_cc, 150000)
jalankan_transaksi(pembayaran_ovo, 80000)
