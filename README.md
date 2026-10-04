# Local Search: Hill-Climbing & Simulated Annealing pada 8-Queens Problem

Praktikum Kecerdasan Buatan (P), Topik **Local Search**
Institut Teknologi Del, Semester 5

| | |
|---|---|
| **Nama** | [Nama lengkap] |
| **NIM** | [NIM] |
| **Mata Kuliah** | 11S3242, Kecerdasan Buatan (P) |
| **Topik** | Local Search |

---

## Deskripsi

Proyek ini mengimplementasikan algoritma **Local Search** untuk menyelesaikan **8-Queens Problem**, yaitu menempatkan 8 ratu pada papan catur 8x8 sehingga tidak ada ratu yang saling menyerang. Algoritma yang diimplementasikan:

1. **Hill-Climbing Search**: algoritma greedy yang selalu memilih tetangga terbaik.
2. **Simulated Annealing**: mengizinkan langkah yang lebih buruk dengan probabilitas yang menurun seiring suhu turun, sehingga bisa keluar dari local minimum.
3. **Random-Restart Hill-Climbing** (tugas tambahan): mengulang Hill-Climbing dari state acak yang berbeda hingga solusi ditemukan.

## Tujuan

- Memahami konsep Local Search sebagai metode *iterative improvement*.
- Mengimplementasikan Hill-Climbing dan Simulated Annealing.
- Menganalisis dan membandingkan kinerja kedua algoritma.

## Formulasi Masalah

| Komponen | Penjelasan |
|---|---|
| **State** | List berukuran 8. Indeks = kolom, nilai = baris tempat ratu diletakkan. Contoh: `[0, 4, 7, 5, 2, 6, 1, 3]` |
| **Fungsi objektif (h)** | Jumlah pasangan ratu yang saling menyerang (satu baris atau satu diagonal) |
| **Tetangga** | Memindahkan satu ratu ke baris lain pada kolom yang sama (8 x 7 = 56 tetangga) |
| **Tujuan** | Mencapai state dengan **h = 0** |

Karena h dihitung dan ingin diminimalkan, kasus "terjebak" disebut **local minimum** (setara dengan local maximum pada versi yang memaksimalkan nilai).

## Struktur Proyek

```
.
├── local_search.py   # Seluruh implementasi algoritma dan eksperimen
└── README.md         # Dokumentasi proyek
```

## Persyaratan

- Python 3.8 atau lebih baru (diuji pada Python 3.13.9)
- Hanya memakai library standar: `random`, `math`, `time`
- Tidak perlu instalasi library tambahan

## Cara Menjalankan

```powershell
python local_search.py
```

Program akan menampilkan:

1. Satu kali eksekusi tiap algoritma beserta papan hasilnya.
2. Perbandingan tingkat keberhasilan dan waktu pada 100 percobaan.
3. Pengaruh parameter `temp` dan `cooling_rate` pada Simulated Annealing.

## Deskripsi Fungsi

| Fungsi | Keterangan |
|---|---|
| `random_state()` | Membuat state awal acak |
| `heuristic(state)` | Menghitung h (jumlah pasangan ratu saling menyerang) |
| `get_neighbors(state)` | Menghasilkan seluruh tetangga dari sebuah state |
| `print_board(state)` | Menampilkan papan dalam bentuk teks |
| `hill_climbing(state)` | Hill-Climbing; berhenti saat h = 0 atau tidak ada tetangga yang lebih baik |
| `simulated_annealing(state, temp, cooling_rate, min_temp, max_steps)` | Simulated Annealing dengan pendinginan geometris |
| `random_restart_hill_climbing(max_restarts)` | Hill-Climbing berulang dari state acak |
| `run_experiment(name, func, trials)` | Menjalankan percobaan berulang dan mencetak tingkat keberhasilan serta waktu |

## Cara Kerja Algoritma

**Hill-Climbing**
1. Mulai dari state awal.
2. Evaluasi semua tetangga dan pilih yang h-nya paling kecil.
3. Jika lebih baik dari state saat ini, pindah ke tetangga tersebut dan ulangi.
4. Berhenti jika h = 0 atau tidak ada tetangga yang lebih baik (terjebak).

**Simulated Annealing**
1. Mulai dari state awal dengan suhu `temp`.
2. Pilih satu tetangga secara acak.
3. Hitung `delta = h_sekarang - h_tetangga`. Jika `delta > 0`, tetangga diterima. Jika tidak, diterima dengan probabilitas `e^(delta / T)`.
4. Turunkan suhu: `T = T * cooling_rate`.
5. Berhenti jika h = 0, suhu mencapai `min_temp`, atau langkah mencapai `max_steps`.

**Random-Restart Hill-Climbing**
Jalankan Hill-Climbing dari state acak, ulangi hingga h = 0 atau mencapai `max_restarts` (default 100).

## Parameter

| Parameter | Default | Pengaruh |
|---|---|---|
| `temp` | 10.0 | Suhu awal. Semakin tinggi, semakin besar peluang menerima langkah buruk di awal |
| `cooling_rate` | 0.995 | Laju pendinginan. Mendekati 1 berarti lebih lambat dan lebih teliti |
| `min_temp` | 0.001 | Batas suhu untuk menghentikan pencarian |
| `max_steps` | 100000 | Batas maksimum iterasi |
| `max_restarts` | 100 | Batas restart pada Random-Restart Hill-Climbing |

## Hasil Percobaan

> Isi dengan hasil dari komputermu. Hasil bersifat acak sehingga berbeda tiap eksekusi.

**Perbandingan algoritma (100 percobaan)**

| Algoritma | Berhasil (h = 0) | Persentase | Waktu (detik) |
|---|---|---|---|
| Hill-Climbing | [..]/100 | [..]% | [..] |
| Simulated Annealing | [..]/100 | [..]% | [..] |
| Random-Restart Hill-Climbing | [..]/100 | [..]% | [..] |

**Pengaruh parameter Simulated Annealing (50 percobaan)**

| temp | cooling_rate | Berhasil | Waktu (detik) |
|---|---|---|---|
| 1 | 0.90 | [..]/50 | [..] |
| 1 | 0.99 | [..]/50 | [..] |
| 1 | 0.999 | [..]/50 | [..] |
| 10 | 0.90 | [..]/50 | [..] |
| 10 | 0.99 | [..]/50 | [..] |
| 10 | 0.999 | [..]/50 | [..] |
| 100 | 0.90 | [..]/50 | [..] |
| 100 | 0.99 | [..]/50 | [..] |
| 100 | 0.999 | [..]/50 | [..] |

**Contoh solusi (h = 0)**

```
[tempel papan hasil dari output programmu]
```

## Analisis

**1. Apakah Hill-Climbing selalu berhasil?**
Tidak. Hill-Climbing hanya mempertimbangkan tetangga langsung, sehingga bisa berhenti di *local minimum* (h > 0 tetapi tidak ada tetangga yang lebih baik), *plateau*, atau *ridge*. [Sesuaikan dengan hasilmu.]

**2. Simulated Annealing vs Hill-Climbing**
Simulated Annealing umumnya lebih sering menemukan solusi karena menerima langkah buruk dengan probabilitas `e^(delta/T)`, yang memungkinkan keluar dari local minimum. Saat suhu turun, perilakunya makin menyerupai Hill-Climbing. Konsekuensinya, ia membutuhkan lebih banyak langkah. [Sesuaikan dengan hasilmu.]

**3. Pengaruh `temp` dan `cooling_rate`**
- `cooling_rate` mendekati 1: pencarian lebih lama tetapi kualitas solusi lebih baik.
- `cooling_rate` kecil: pencarian cepat tetapi mudah terjebak.
- `temp` terlalu rendah: eksplorasi minim. `temp` terlalu tinggi: awalnya mirip random walk dan boros langkah.

**Tugas tambahan: Random-Restart**
Dengan banyak restart, tingkat keberhasilan mendekati 100% karena tiap restart punya peluang sukses sendiri. [Tambahkan perbandingan dengan Simulated Annealing dari hasilmu.]

## Kesimpulan

Hill-Climbing sederhana dan cepat tetapi mudah terjebak di local minimum. Simulated Annealing lebih andal karena eksplorasi probabilistiknya, dengan biaya komputasi lebih besar. Random-Restart Hill-Climbing adalah alternatif efektif untuk ruang pencarian sekecil 8-Queens.

## Referensi

- Russell, S. & Norvig, P. *Artificial Intelligence: A Modern Approach*, bab Local Search.
- Materi dan modul praktikum Kecerdasan Buatan, Institut Teknologi Del.
