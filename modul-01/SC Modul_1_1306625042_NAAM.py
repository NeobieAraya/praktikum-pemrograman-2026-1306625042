#Program Konversi Suhu Celcius - Reamur - Fahrenheit
print("Program Konversi Suhu")
print("Nama : Neobie Araya Ahmad Maulana")
print("NIM : 1306625042")

#input parameter suhu
suhu_awal = float(input("suhu awal = "))
suhu_akhir = float(input("suhu akhir = "))
selang = float(input("selang = "))
# Tabel konversi suhu
print("\nTabel Konversi Suhu:")
print("No | Celcius(°C) | Reamur(°R) | Fahrenheit(°F)")
print("-" * 45)

# Perulangan dan konversi suhu menggunakan while loop
C = suhu_awal
No = 1
while C <= suhu_akhir:
    F = (C * 9/5) + 32
    R = 4/5 * C
    print(f"{No:2d}  |  {C:8.1f}  |  {R:8.1f}  |  {F:8.1f}")
    C += selang
    No += 1
print()
print("Selesai")