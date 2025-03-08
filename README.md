# **Kriptografi Al-Kindi dengan Python**  

## **Deskripsi Proyek**  
Proyek ini mengimplementasikan **kriptografi klasik** berdasarkan metode **Al-Kindi**, yang mencakup:  
✅ **Enkripsi & Dekripsi Sederhana** (Substitusi monoalfabetik)  
✅ **Metode Transposisi** (Mengacak urutan huruf dalam pesan)  
✅ **Metode Komposit** (Gabungan beberapa teknik untuk meningkatkan keamanan)  

Tujuan proyek ini adalah memahami prinsip dasar **kriptografi klasik** serta bagaimana pesan dapat dienkripsi dan didekripsi menggunakan **Python**.  

---

## **Metode yang Digunakan**  

### **1. Enkripsi & Dekripsi Sederhana (Substitusi Monoalfabetik)**  
Metode ini menggantikan setiap huruf dalam teks dengan huruf lain berdasarkan aturan tertentu. Salah satu implementasinya adalah **Caesar Cipher**, yang menggunakan pergeseran huruf.  

**Contoh Enkripsi Caesar Cipher (shift = 3):**  
- **Plaintext** : `HELLO`  
- **Ciphertext** : `KHOOR`  

**Rumus Enkripsi:**  
\[
C = (P + k) \mod 26
\]  
**Rumus Dekripsi:**  
\[
P = (C - k) \mod 26
\]  
Di mana:  
- **C** = Ciphertext  
- **P** = Plaintext  
- **k** = Pergeseran (shift)  

---

### **2. Metode Transposisi**  
Metode ini mengubah urutan karakter dalam teks tanpa mengubah karakter itu sendiri. Salah satu contoh adalah **Columnar Transposition Cipher**, di mana teks dibagi ke dalam kolom dan dibaca dalam urutan tertentu.  

**Contoh Transposisi Kolom (Key = "3214")**  
- **Plaintext** : `KRIPTOGRAFI`  
- **Ditulis dalam Kolom**:  
  ```
  K R I P  
  T O G R  
  A F I  
  ```
- **Ciphertext (dibaca sesuai key)** : `IPGRKTROAFI`  

---

### **3. Metode Komposit (Substitusi + Transposisi)**  
Metode ini menggabungkan **substitusi** dan **transposisi** untuk meningkatkan keamanan pesan.  
- Pertama, teks dienkripsi menggunakan metode **Caesar Cipher**.  
- Kemudian, hasil enkripsi diproses menggunakan **Columnar Transposition Cipher**.  
- Hasil akhirnya lebih sulit dipecahkan dibandingkan metode individu.  

**Contoh:**  
- **Plaintext:** `HELLO WORLD`  
- **Langkah 1 - Substitusi:** `KHOOR ZRUOG`  
- **Langkah 2 - Transposisi:** `ZRUOGKHOOR`  


## **Fitur Utama**  
✅ **Enkripsi & Dekripsi dengan metode klasik**  
✅ **Implementasi Substitusi Monoalfabetik (Caesar Cipher)**  
✅ **Metode Transposisi Kolom untuk menyusun ulang teks**  
✅ **Metode Komposit untuk meningkatkan keamanan**  
✅ **Implementasi menggunakan Python & pustaka standar**  

## **Teknologi yang Digunakan**  
🔹 **Python**  
🔹 **Pandas & NumPy** (Pemrosesan data)  
🔹 **Pustaka bawaan Python** (string manipulation)  

## **Hasil & Visualisasi**  
1️⃣ **Teks sebelum dan sesudah enkripsi**  
2️⃣ **Perbandingan metode enkripsi sederhana vs transposisi**  
3️⃣ **Keamanan yang lebih tinggi dengan metode komposit**  

