import sys
import time
import os

def clear_screen():
    # Fungsi untuk membersihkan layar terminal
    os.system('cls' if os.name == 'nt' else 'clear')

def lirik_nji():
    # Bersihkan layar terlebih dahulu
    clear_screen()
    
    # Pengaturan delay default
    delay_animasi = 0.03   # Delay untuk animasi
    
    # =============================================
    # CARA MENGATUR DELAY UNTUK SETIAP BARIS LIRIK
    # =============================================
    # Format: ["teks lirik", delay_karakter, delay_setelah_baris]
    #
    # delay_karakter: Waktu tunggu setelah setiap karakter ditampilkan (dalam detik)
    #   - Nilai kecil (0.01-0.03): Karakter muncul CEPAT
    #   - Nilai sedang (0.04-0.07): Karakter muncul NORMAL
    #   - Nilai besar (0.08-0.15): Karakter muncul LAMBAT
    #
    # delay_setelah_baris: Waktu tunggu setelah baris selesai ditampilkan (dalam detik)
    #   - Nilai kecil (0.2-0.4): Jeda SINGKAT sebelum baris berikutnya
    #   - Nilai sedang (0.5-0.8): Jeda NORMAL sebelum baris berikutnya
    #   - Nilai besar (1.0-2.0): Jeda LAMA sebelum baris berikutnya
    #
    # Contoh:
    # ["Baris cepat", 0.01, 0.3]  <- Karakter muncul CEPAT, jeda SINGKAT
    # ["Baris normal", 0.05, 0.5] <- Karakter muncul NORMAL, jeda NORMAL
    # ["Baris lambat", 0.1, 1.0]  <- Karakter muncul LAMBAT, jeda LAMA
    #
    # Gunakan [None, 0, 0] untuk menandai akhir paragraf (akan menambahkan baris kosong)
    # =============================================
    
    lirik = [
        # PARAGRAF 1 - Contoh variasi kecepatan
        ["You know I want you", 0.10, 0.5],          # <-- LAMBAT: delay_karakter = 0.10
        ["It's not a secret I try to hide", 0.04, 0.5],  # <-- NORMAL: delay_karakter = 0.04
        ["You know you want me", 0.05, 0.5],
        ["So don't keep saying our hands are tied", 0.04, 0.5],
        ["You claim it's not in the cards", 0.05, 0.5],
        ["And faith is pulling you miles away", 0.04, 0.5],
        ["And out of reach from me", 0.05, 0.5],
        ["But you're hearing my heart", 0.04, 0.5],
        ["So who can stop me if I decide your my destiny?", 0.05, 1.0],  # <-- Jeda LAMA di akhir: delay_setelah_baris = 1.0
        [None, 0, 0],  # Akhir paragraf - menambahkan baris kosong
        
        # PARAGRAF 2 - Chorus dengan kecepatan lebih cepat
        ["What if we rewrite the stars?", 0.03, 0.5],    # <-- CEPAT: delay_karakter = 0.03
        ["Say you were made to be mine", 0.04, 0.5],
        ["Nothing could keep us apart", 0.03, 0.5],
        ["You'll be the one I was meant to find", 0.04, 0.5],
        ["It's up to you and it's up to me", 0.03, 0.5],
        ["No one could say what we get to be", 0.04, 0.5],
        ["So why don't we rewrite the stars?", 0.03, 0.5],
        ["And maybe the world could be ours tonight", 0.04, 1.0],
        [None, 0, 0],  # Akhir paragraf
        
        # Paragraf berikutnya...
        ["You think it's easy", 0.05, 0.5],
        ["You think I don't wanna run to you, yeah", 0.04, 0.5],
        ["But there are mountains", 0.05, 0.5],
        ["And there are doors that we can't walk through", 0.04, 0.5],
        ["I know you're wondering why", 0.05, 0.5],
        ["Because we're able to be just you and me within these walls", 0.03, 0.5],
        ["But when we go outside you're gonna wake up", 0.04, 0.5],
        ["And see that it was hopeless after all", 0.05, 1.0],
        [None, 0, 0],  # Akhir paragraf
        
        ["No one can rewrite the stars", 0.05, 0.5],
        ["How can you say you'll be mine?", 0.04, 0.5],
        ["Everything keeps us apart", 0.05, 0.5],
        ["And I'm not the one you were meant to find", 0.04, 0.5],
        ["It's not up to you, it's not up to me", 0.05, 0.5],
        ["When everyone tells us what we can be", 0.04, 0.5],
        ["And how come we rewrite the stars?", 0.05, 0.5],
        ["Say that the world can be ours tonight", 0.04, 1.0],
        [None, 0, 0],  # Akhir paragraf
        
        ["All I want is to fly with you", 0.05, 0.5],
        ["All I want is to fall with you", 0.04, 0.5],
        ["So just give me all of you", 0.05, 0.5],
        ["It feels impossible", 0.04, 0.5],
        ["Is it impossible?", 0.05, 1.0],
        [None, 0, 0],  # Akhir paragraf
        
        ["And how do we rewrite the stars?", 0.05, 0.5],
        ["Say you were made to be mine", 0.04, 0.5],
        ["And nothing could keep us apart", 0.05, 0.5],
        ["'Cause you are the one I was meant to find", 0.04, 0.5],
        ["It's up to you, and it's up to me", 0.05, 0.5],
        ["No one could say what we get to be", 0.04, 0.5],
        ["And why don't we rewrite the stars?", 0.05, 0.5],
        ["Changing the world to be ours", 0.04, 1.0],
        [None, 0, 0],  # Akhir paragraf
        
        ["You know I want you", 0.05, 0.5],
        ["It's not a secret I try to hide", 0.04, 0.5],
        ["But I can't have you", 0.05, 0.5],
        ["We're bound to break and my hands are tied", 0.04, 1.0],
        [None, 0, 0]  # Akhir paragraf
    ]
    
    # Tampilkan judul
    print("\n== Rewrite The Stars - The Greatest Showman ==")
    time.sleep(2)
    
    i = 0
    while i < len(lirik):
        item = lirik[i]
        
        # Jika teks adalah None, ini adalah akhir paragraf
        if item[0] is None:
            print('')  # Tambah baris kosong antar paragraf
            i += 1
            continue
            
        # Ambil data dari item saat ini
        baris_lagu = item[0]           # Teks lirik
        delay_karakter = item[1]       # Delay setelah setiap karakter
        delay_setelah_baris = item[2]  # Delay setelah baris selesai
        
        # Tampilkan setiap karakter dengan delay
        for karakter in baris_lagu:
            print(karakter, end='')
            time.sleep(delay_animasi)  # Delay animasi (konstan)
            sys.stdout.flush()
            time.sleep(delay_karakter)  # Delay karakter (bervariasi per baris)
        
        # Tunggu setelah baris selesai
        time.sleep(delay_setelah_baris)  # Delay setelah baris (bervariasi per baris)
        print('')
        i += 1
    
    print("\ncode by rezawalker")

# Panggil fungsi untuk menjalankannya
if __name__ == "__main__":
    lirik_nji()