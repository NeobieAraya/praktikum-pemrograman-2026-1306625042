# Modul [03] - [Trigonometri]

**Nama:** [Neobie Araya Ahmad Maulana]  
**NIM:** [1306625042]  
**Kelas:** [Fisika C]  

---

## 1. Problem Statement
> Membuat Program untuk Menghitung Nilai sin dan cos dari pendekatan Mc Laurin

## 2. Mathematical Equation
> $$\sin(x) = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!} + \dots = \sum_{n=0}^{\infty} \frac{(-1)^n}{(2n+1)!} x^{2n+1}$$
> $$\cos(x) = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \frac{x^6}{6!} + \dots = \sum_{n=0}^{\infty} \frac{(-1)^n}{(2n)!} x^{2n}$$
> $$x_{x_{\text{rad}} = x_{\text{deg}} \times \frac{\pi}{180}\text{rad}} = x_{\text{deg}} \times \frac{\pi}{180}$$

## 3. Algorithm
> Mulai (Start)Definisi Fungsi Matematika Rekursif / Pembantu:hitung_faktorial(m): Mengembalikan nilai $m!$.hitung_suku_sin(x, k): Mengembalikan $(-1)^k \frac{x^{2k+1}}{(2k+1)!}$.hitung_suku_cos(x, k): Mengembalikan $(-1)^k \frac{x^{2k}}{(2k)!}$.Loop Utama (While ulang == 'y'):Baca input Nama dan NRM.Baca input Besar sudut (derajat) $\to x_{\text{deg}}$.Konversi sudut: $x_{\text{rad}} \leftarrow x_{\text{deg}} \times \frac{\pi}{180}$.Hitung True Value:$TV_{\text{sin}} \leftarrow \sin(x_{\text{rad}})$$TV_{\text{cos}} \leftarrow \cos(x_{\text{rad}})$Tampilkan $TV_{\text{sin}}$ dan $TV_{\text{cos}}$.Cetak Header Tabel.Inisialisasi variabel perulangan suku:jumlah_suku $\leftarrow 0$AV_sin $\leftarrow 0.0$AV_cos $\leftarrow 0.0$ER_sin $\leftarrow 100.0$ER_cos $\leftarrow 100.0$While Loop (Kondisi Berhenti: ER_sin >= 5 OR ER_cos >= 5):
a. Tambahkan jumlah_suku dengan 1 ($k = \text{jumlah\_suku} - 1$).
b. Hitung penambahan suku MacLaurin:$\text{AV\_sin} \leftarrow \text{AV\_sin} + \text{hitung\_suku\_sin}(x_{\text{rad}}, k)$$\text{AV\_cos} \leftarrow \text{AV\_cos} + \text{hitung\_suku\_cos}(x_{\text{rad}}, k)$
c. Hitung Relative Error:$\text{ER\_sin} \leftarrow \left\vert{} \frac{\text{AV\_sin} - TV_{\text{sin}}}{TV_{\text{sin}}} \right\vert{} \times 100$$\text{ER\_cos} \leftarrow \left\vert{} \frac{\text{AV\_cos} - TV_{\text{cos}}}{TV_{\text{cos}}} \right\vert{} \times 100$
d. Cetak Baris Tabel (jumlah_suku, AV_sin, ER_sin, AV_cos, ER_cos).Minta input Mau menghitung lagi (y/t) ?.Selesai (End)
