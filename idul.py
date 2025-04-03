
import math
import time
import os
import random

def clear_screen():
    """
    Fungsi untuk membersihkan layar terminal.
    Mendukung Windows dan sistem berbasis Unix.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def tampilkan_ucapan():
    """
    Fungsi untuk menampilkan ucapan selamat hari raya idul fitri
    dengan efek ketik terinspirasi dari Lirik.py
    """
    clear_screen()
    
    # Pengaturan delay
    delay_karakter = 0.03   # Delay untuk animasi karakter
    
    # Format: ["teks ucapan", delay_karakter, delay_setelah_baris]
    ucapan = [
        ["", 0, 1.0],  # Jeda awal
        ["SELAMAT HARI RAYA", 0.08, 0.8],
        ["", 0, 0.3],
        ["IDUL FITRI", 0.1, 1.0],
        ["", 0, 0.3],
        ["1446 H", 0.1, 1.0],
        ["", 0, 0.5],
        ["Minal Aidin Wal Faizin", 0.05, 0.8],
        ["Mohon Maaf Lahir dan Batin", 0.05, 1.5],
        ["", 0, 0.5],
        ["Semoga Allah SWT menerima amal ibadah kita", 0.03, 0.8],
        ["dan menjadikan kita sebagai orang-orang", 0.03, 0.8],
        ["yang kembali fitrah", 0.03, 1.5],
        ["", 0, 0.5],
        ["Taqabbalallahu minna wa minkum", 0.05, 0.8],
        ["Shiyamana wa shiyamakum", 0.05, 1.5],
        ["", 0, 1.0],
        ["Memulai animasi bulan sabit dalam 3 detik...", 0.03, 3.0]
    ]
    
    # Tampilkan ucapan dengan efek ketik
    for baris in ucapan:
        teks, delay_char, delay_baris = baris
        
        # Posisi tengah
        posisi = (os.get_terminal_size().columns - len(teks)) // 2
        if posisi < 0:
            posisi = 0
        
        # Tampilkan spasi untuk posisi tengah
        print(" " * posisi, end="", flush=True)
        
        # Tampilkan teks dengan efek ketik
        for karakter in teks:
            print(karakter, end="", flush=True)
            time.sleep(delay_char)
        
        print()  # Pindah baris
        time.sleep(delay_baris)

def tampilkan_kembang_api():
    """
    Fungsi untuk menampilkan animasi kembang api dengan latar belakang masjid
    """
    clear_screen()
    
    # Dimensi layar
    width = 80
    height = 24
    
    # Latar belakang masjid (ASCII art)
    masjid = [
        "                                                                                ",
        "                                                                                ",
        "                                                                                ",
        "                                                                                ",
        "                                                                                ",
        "                                                                                ",
        "                                                                                ",
        "                                                                                ",
        "                                                                                ",
        "                                                                                ",
        "                                                                                ",
        "                                                                                ",
        "                          _____                                                 ",
        "                         /     \\                                                ",
        "                        /       \\                                               ",
        "                       /         \\                                              ",
        "                      /___________\\                                             ",
        "                      |  _   _  |                                               ",
        "                 _____| | | | | |_____                                          ",
        "                /     \\ |_| |_| /     \\                                         ",
        "               /       \\       /       \\                                        ",
        "              /         \\_____/         \\                                       ",
        "             /___________________________\\                                       ",
        "             |   |     |     |     |   |                                        ",
        "             |   |     |     |     |   |                                        ",
        "             |   |     |  o  |     |   |                                        ",
        "             |___|_____|_____|_____|___|                                        ",
        "             |                       |                                          ",
        "             |                       |                                          ",
        "             |_______________________|                                          ",
        "                                                                                ",
        "                                                                                "
    ]
    
    # Karakter untuk kembang api
    kembang_api_chars = [".", "o", "O", "*", "+", "x", "X", "@"]
    
    # Warna (simulasi dengan karakter ASCII)
    colors = [
        kembang_api_chars,  # Normal
        [".", ":", ";", "!", "|", "=", "#", "$"],  # Alternatif 1
        [".", ",", "~", "-", "+", "=", "*", "#"]   # Alternatif 2
    ]
    
    # Durasi animasi (dalam detik)
    durasi = 14  # Diubah menjadi 14 detik
    waktu_mulai = time.time()
    
    # Simulasi kembang api
    class KembangApi:
        def __init__(self, x, y):
            self.x = x
            self.y = y
            self.age = 0
            self.max_age = random.randint(10, 20)
            self.particles = []
            self.color_set = random.choice(colors)
            self.exploded = False
            self.rise_speed = random.uniform(0.3, 0.7)
        
        def update(self):
            if not self.exploded:
                # Kembang api naik
                self.y -= self.rise_speed
                self.age += 1
                
                # Kembang api meledak
                if self.age >= self.max_age:
                    self.exploded = True
                    # Buat partikel
                    num_particles = random.randint(20, 30)
                    for _ in range(num_particles):
                        angle = random.uniform(0, 2 * math.pi)
                        speed = random.uniform(0.2, 0.8)
                        self.particles.append({
                            'x': self.x,
                            'y': self.y,
                            'dx': math.cos(angle) * speed,
                            'dy': math.sin(angle) * speed,
                            'age': 0,
                            'max_age': random.randint(5, 15)
                        })
            else:
                # Update partikel
                for p in self.particles:
                    p['x'] += p['dx']
                    p['y'] += p['dy']
                    p['dy'] += 0.05  # Gravitasi
                    p['age'] += 1
                
                # Hapus partikel yang sudah tua
                self.particles = [p for p in self.particles if p['age'] < p['max_age']]
        
        def draw(self, screen):
            if not self.exploded:
                # Gambar kembang api yang naik
                x, y = int(self.x), int(self.y)
                if 0 <= x < width and 0 <= y < height:
                    screen[y][x] = "|"
                    if y + 1 < height:
                        screen[y + 1][x] = "^"
            else:
                # Gambar partikel
                for p in self.particles:
                    x, y = int(p['x']), int(p['y'])
                    if 0 <= x < width and 0 <= y < height:
                        # Pilih karakter berdasarkan usia partikel
                        char_idx = min(int(p['age'] / p['max_age'] * len(self.color_set)), len(self.color_set) - 1)
                        screen[y][x] = self.color_set[char_idx]
        
        def is_dead(self):
            return self.exploded and len(self.particles) == 0
    
    # Daftar kembang api aktif
    kembang_apis = []
    
    try:
        while time.time() - waktu_mulai < durasi:
            # Buat layar kosong
            screen = [[' ' for _ in range(width)] for _ in range(height)]
            
            # Tambahkan latar belakang masjid
            for y, line in enumerate(masjid):
                if y < height:
                    for x, char in enumerate(line):
                        if x < width and char != ' ':
                            screen[y][x] = char
            
            # Tambahkan kembang api baru secara acak
            if random.random() < 0.1:  # 10% kemungkinan setiap frame
                x = random.randint(10, width - 10)
                y = height - 1
                kembang_apis.append(KembangApi(x, y))
            
            # Update dan gambar semua kembang api
            for ka in kembang_apis:
                ka.update()
                ka.draw(screen)
            
            # Hapus kembang api yang sudah mati
            kembang_apis = [ka for ka in kembang_apis if not ka.is_dead()]
            
            # Tampilkan layar
            clear_screen()
            for row in screen:
                print(''.join(row))
            
            # Tambahkan ucapan di bawah
            pesan = "Selamat Hari Raya Idul Fitri 1446 H"
            print("\n" + " " * ((width - len(pesan)) // 2) + pesan)
            
            # Jeda
            time.sleep(0.1)
    
    except KeyboardInterrupt:
        clear_screen()
        print(".")
    
    # Tampilkan pesan setelah animasi selesai
    clear_screen()
    print("\n\n")
    print(" " * 20 + " ")
    print(" " * 25 + "")
    input("MADE BY REZAWALKER")

def bulan_sabit():
    """
    Fungsi untuk membuat bulan sabit berputar menggunakan ASCII art.
    
    Menggunakan pendekatan sederhana untuk membuat bulan sabit yang jelas
    dan berputar pada porosnya dari kiri ke kanan.
    """
    # Karakter untuk menggambar bulan sabit (dari gelap ke terang)
    chars = ".,-~:;=!*#$@"
    
    # Dimensi layar
    width = 80
    height = 24
    
    # Kecepatan animasi
    speed = 0.05
    
    # Membersihkan layar
    clear_screen()
    
    try:
        # Sudut rotasi
        angle = 0
        
        # Durasi animasi (dalam detik)
        durasi = 15  # Diubah menjadi 15 detik
        waktu_mulai = time.time()
        
        while True:
            # Periksa apakah durasi animasi telah tercapai
            if time.time() - waktu_mulai > durasi:
                break
                
            # Buffer untuk layar
            screen = [[' ' for _ in range(width)] for _ in range(height)]
            
            # Menghitung sinus dan kosinus sudut rotasi
            cos_angle = math.cos(angle)
            sin_angle = math.sin(angle)
            
            # Parameter bulan sabit
            outer_radius = 8  # Radius lingkaran luar (dikurangi agar tidak terlalu besar)
            inner_radius = 6   # Radius lingkaran dalam
            offset_x = 3       # Offset untuk membuat bentuk sabit
            
            # Menggambar bulan sabit
            for y in range(-outer_radius, outer_radius + 1):
                for x in range(-outer_radius, outer_radius + 1):
                    # Menghitung jarak dari pusat lingkaran luar
                    dist_outer = math.sqrt(x*x + y*y)
                    
                    # Menghitung jarak dari pusat lingkaran dalam (digeser)
                    dist_inner = math.sqrt((x - offset_x)*(x - offset_x) + y*y)
                    
                    # Titik berada di dalam lingkaran luar dan di luar lingkaran dalam
                    if dist_outer <= outer_radius and dist_inner >= inner_radius:
                        # Koordinat 3D (z = 0 untuk titik pada bidang xy)
                        x3d = x
                        y3d = y
                        z3d = 0
                        
                        # Rotasi pada sumbu Y (berputar dari kiri ke kanan)
                        x_rot = x3d * cos_angle + z3d * sin_angle
                        z_rot = -x3d * sin_angle + z3d * cos_angle
                        y_rot = y3d
                        
                        # Menghitung normal permukaan untuk pencahayaan
                        # Normal mengarah keluar dari pusat
                        nx = x / dist_outer
                        ny = y / dist_outer
                        nz = 0
                        
                        # Rotasi normal
                        nx_rot = nx * cos_angle + nz * sin_angle
                        nz_rot = -nx * sin_angle + nz * cos_angle
                        
                        # Vektor cahaya (dari arah (1, 1, -1))
                        light_dir = (1, 1, -1)
                        light_len = math.sqrt(sum(c*c for c in light_dir))
                        light_dir = tuple(c/light_len for c in light_dir)
                        
                        # Produk dot dari normal dengan vektor cahaya
                        luminance = nx_rot * light_dir[0] + ny * light_dir[1] + nz_rot * light_dir[2]
                        luminance = max(0.2, luminance)  # Memberikan pencahayaan minimum
                        
                        # Proyeksi ke layar
                        # Menggunakan proyeksi ortografik sederhana karena kita hanya berputar pada sumbu Y
                        scale = 1.0
                        # Posisi bulan sabit digeser ke atas agar tidak terlalu dekat dengan tulisan
                        screen_x = int(width/2 + x_rot * scale)
                        screen_y = int(height/2 - 4 + y_rot * scale)  # Dikurangi 4 untuk menggeser ke atas
                        
                        # Memeriksa apakah titik berada dalam batas layar
                        if 0 <= screen_x < width and 0 <= screen_y < height:
                            # Menentukan karakter berdasarkan luminansi
                            char_index = int(luminance * (len(chars) - 1))
                            screen[screen_y][screen_x] = chars[char_index]
            
            # Menambahkan bintang di sekitar bulan sabit
            stars = [
                (15, 5), (65, 3), (30, 2), (50, 3), (20, 8), 
                (60, 7), (40, 1), (70, 10), (10, 12), (55, 4),
                (25, 6), (45, 5), (35, 9), (75, 8), (5, 3)
            ]
            
            for sx, sy in stars:
                if 0 <= sx < width and 0 <= sy < height:
                    screen[sy][sx] = '*'
            
            # Mencetak layar
            clear_screen()
            
            # Menambahkan tulisan "Idul Fitri" di bawah bulan sabit
            # Posisi tulisan diatur agar ada jarak yang cukup dari bulan sabit
            message = "Selamat Hari Raya Idul Fitri"
            if width >= len(message):
                position = (width - len(message)) // 2
                for i, char in enumerate(message):
                    if 0 <= position + i < width:
                        screen[height - 6][position + i] = char  # Diubah dari -3 menjadi -6
            
            # Menambahkan tulisan "Minal Aidin Wal Faizin" di bawah tulisan Idul Fitri
            message2 = "Minal Aidin Wal Faizin"
            if width >= len(message2):
                position = (width - len(message2)) // 2
                for i, char in enumerate(message2):
                    if 0 <= position + i < width:
                        screen[height - 4][position + i] = char  # Diubah dari -2 menjadi -4
            
            # Menambahkan tahun Hijriah
            message3 = "1446 H"
            if width >= len(message3):
                position = (width - len(message3)) // 2
                for i, char in enumerate(message3):
                    if 0 <= position + i < width:
                        screen[height - 2][position + i] = char  # Diubah dari -1 menjadi -2
            
            # Mencetak layar
            for row in screen:
                print("".join(row))
            
            # Memperbarui sudut rotasi (berputar dari kiri ke kanan)
            angle += 0.1  # Nilai positif untuk berputar dari kiri ke kanan
            
            # Jeda singkat untuk menciptakan efek berputar
            time.sleep(speed)
    
    except KeyboardInterrupt:
        # Menangani interupsi keyboard (Ctrl+C) untuk keluar dengan bersih
        clear_screen()
        print("")
        return False
    
    # Animasi selesai tanpa interupsi
    return True

if __name__ == "__main__":
    # Tampilkan ucapan selamat hari raya terlebih dahulu
    tampilkan_ucapan()
    
    # Jalankan animasi bulan sabit
    animasi_selesai = bulan_sabit()
    
    # Jika animasi selesai tanpa interupsi, tampilkan animasi kembang api
    if animasi_selesai:
        # Tampilkan pesan transisi
        clear_screen()
        print("\n\n\n")
        print(" " * 20 + " ")
        time.sleep(1.5)
        
        # Jalankan animasi kembang api dengan latar belakang masjid
        tampilkan_kembang_api()
