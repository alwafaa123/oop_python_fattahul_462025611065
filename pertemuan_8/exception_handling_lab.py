class SaldoMinimalError(Exception):
    """Exception kustom jika penarikan melebihi saldo yang tersedia."""
    def __init__(self, pesan="Error: Saldo tidak mencukupi untuk melakukan penarikan!"):
        self.pesan = pesan
        super().__init__(self.pesan)

class DompetSaku:
    def __init__(self, pemilik, saldo_awal):
        self.pemilik = pemilik
        self.__saldo = saldo_awal

    def cek_saldo(self):
        return self.__saldo

    def tarik_tunai(self, jumlah):
        print(f"\n--- Memproses penarikan sejumlah: Rp{jumlah} ---")
        if jumlah > self.__saldo:
            raise SaldoMinimalError(f"Error: Gagal menarik Rp{jumlah}. Saldo {self.pemilik} hanya Rp{self.__saldo}!")

        self.__saldo -= jumlah
        print(f"selamat Penarikan berhasil! Saldo sekarang: Rp{self.__saldo}")

if __name__ == "__main__":
    dompet_fattahul = DompetSaku("Fattahul", 50000)
    try:
        dompet_fattahul.tarik_tunai(20000)
    except SaldoMinimalError as error:
        print(error)
    finally:
        print("Pesan Sistem: Proses pemeriksaan transaksi 1 selesai.")

    print("-" * 50)
    try:
        dompet_fattahul.tarik_tunai(40000)
    except SaldoMinimalError as error:
        print(f"Tertangkap Kamera Keamanan: {error}")
    finally:
        print("Pesan Sistem: Proses pemeriksaan transaksi 2 selesai.")