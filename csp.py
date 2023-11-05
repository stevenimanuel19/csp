# Fungsi untuk mencari pemetaan warna menggunakan algoritma backtracking
def color_mapping(csp, assignment, colors):
    # Base case: Jika semua simpul sudah diberi warna, maka selesai.
    if len(assignment) == len(csp):
        return True

    # Memilih simpul yang belum diberi warna.
    current_node = select_unassigned_node(csp, assignment)

    # Mencoba warna yang mungkin untuk simpul saat ini.
    for color in colors:
        if is_color_valid(current_node, color, assignment, csp):
            assignment[current_node] = color
            if color_mapping(csp, assignment, colors):
                return True
            assignment[current_node] = None

    return False

# Fungsi untuk memilih simpul yang belum diberi warna.
def select_unassigned_node(csp, assignment):
    for node in csp:
        if node not in assignment:
            return node

# Fungsi untuk memeriksa apakah warna yang diberikan pada simpul saat ini valid.
def is_color_valid(node, color, assignment, csp):
    for neighbor in csp[node]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

# Fungsi utama
def main():
    # Definisi grafik csp
    csp = {
        "Steven": ["Zendy", "Jeje"],
        "Rexy": [],
        "David": ["Steven", "Rexy"],
        "Ryan": ["Steven", "David"],
        "edmund": ["Zendy"],
        "Zendy": ["Steven", "Edmund", "David", "Jeje", "Rexy", "Ryan"],
        "Jeje": ["Steven"],
        "Kaon": []
    }

    # Daftar warna 
    colors = ["biru", "merah", "abu abu", "pink"]

    # Assignment awal kosong
    assignment = {}

    # Memanggil fungsi color_mapping untuk mencari pemetaan warna
    if color_mapping(csp, assignment, colors):
        print("Color Mapping :")
        for node, color in assignment.items():
            print(f"{node} ==> {color}")
    else:
        print("Tidak ada solusi yang memenuhi")

# Memastikan bahwa main() hanya dijalankan jika ini adalah program utama.
if __name__ == "__main__":
    main()