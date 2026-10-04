import random
import math
import time

N = 8  # ukuran papan dan jumlah ratu


# ---------------------------------------------------------
# Langkah 2: Representasi state dan fungsi objektif
# ---------------------------------------------------------
def random_state():
    """Buat state acak: indeks = kolom, nilai = baris ratu."""
    return [random.randint(0, N - 1) for _ in range(N)]


def heuristic(state):
    """Hitung h = jumlah pasangan ratu yang saling menyerang."""
    h = 0
    for i in range(N):
        for j in range(i + 1, N):
            same_row = state[i] == state[j]
            same_diagonal = abs(state[i] - state[j]) == (j - i)
            if same_row or same_diagonal:
                h += 1
    return h


def get_neighbors(state):
    """Semua tetangga: pindahkan satu ratu ke baris lain di kolomnya (8 x 7 = 56)."""
    neighbors = []
    for col in range(N):
        for row in range(N):
            if row != state[col]:
                neighbor = state.copy()
                neighbor[col] = row
                neighbors.append(neighbor)
    return neighbors


def print_board(state):
    """Tampilkan papan dalam bentuk teks (Q = ratu)."""
    for row in range(N):
        print(" ".join("Q" if state[col] == row else "." for col in range(N)))


# ---------------------------------------------------------
# Langkah 3: Hill-Climbing Search
# ---------------------------------------------------------
def hill_climbing(state):
    current = state.copy()
    steps = 0
    while True:
        h_current = heuristic(current)
        if h_current == 0:
            return current, h_current, steps

        best_neighbor = None
        best_h = h_current
        for neighbor in get_neighbors(current):
            h_neighbor = heuristic(neighbor)
            if h_neighbor < best_h:
                best_h = h_neighbor
                best_neighbor = neighbor

        # Tidak ada tetangga yang lebih baik -> terjebak (local minimum)
        if best_neighbor is None:
            return current, h_current, steps

        current = best_neighbor
        steps += 1


# ---------------------------------------------------------
# Langkah 4: Simulated Annealing
# ---------------------------------------------------------
def simulated_annealing(state, temp=10.0, cooling_rate=0.995,
                        min_temp=0.001, max_steps=100000):
    current = state.copy()
    h_current = heuristic(current)
    steps = 0

    while temp > min_temp and h_current > 0 and steps < max_steps:
        # Pilih satu tetangga secara acak
        col = random.randrange(N)
        row = random.randrange(N)
        if row == current[col]:
            continue
        neighbor = current.copy()
        neighbor[col] = row
        h_neighbor = heuristic(neighbor)

        delta = h_current - h_neighbor  # positif = lebih baik
        if delta > 0 or random.random() < math.exp(delta / temp):
            current = neighbor
            h_current = h_neighbor

        temp *= cooling_rate
        steps += 1

    return current, h_current, steps


# ---------------------------------------------------------
# Tugas Tambahan: Random-Restart Hill-Climbing
# ---------------------------------------------------------
def random_restart_hill_climbing(max_restarts=100):
    result, h, restarts = None, None, 0
    for restarts in range(1, max_restarts + 1):
        result, h, _ = hill_climbing(random_state())
        if h == 0:
            break
    return result, h, restarts


# ---------------------------------------------------------
# Langkah 5: Menjalankan kode
# ---------------------------------------------------------
def run_experiment(name, func, trials=100):
    success = 0
    start = time.time()
    for _ in range(trials):
        _, h, _ = func()
        if h == 0:
            success += 1
    elapsed = time.time() - start
    print(f"{name:<28} berhasil: {success:>3}/{trials}  "
          f"({success / trials * 100:5.1f}%)  waktu: {elapsed:.2f} detik")


if __name__ == "__main__":
    print("=== SATU KALI JALAN ===")
    start_state = random_state()
    print("State awal :", start_state, "| h =", heuristic(start_state))

    sol, h, steps = hill_climbing(start_state)
    print("\n[Hill-Climbing]")
    print("State akhir:", sol, "| h =", h, "| langkah =", steps)
    print_board(sol)

    sol, h, steps = simulated_annealing(start_state)
    print("\n[Simulated Annealing]")
    print("State akhir:", sol, "| h =", h, "| langkah =", steps)
    print_board(sol)

    sol, h, restarts = random_restart_hill_climbing()
    print("\n[Random-Restart Hill-Climbing]")
    print("State akhir:", sol, "| h =", h, "| restart =", restarts)
    print_board(sol)

    print("\n=== PERBANDINGAN (100 percobaan) ===")
    run_experiment("Hill-Climbing",
                   lambda: hill_climbing(random_state()))
    run_experiment("Simulated Annealing",
                   lambda: simulated_annealing(random_state()))
    run_experiment("Random-Restart HC",
                   lambda: random_restart_hill_climbing())

    print("\n=== PENGARUH PARAMETER SA ===")
    for t in (1, 10, 100):
        for c in (0.90, 0.99, 0.999):
            run_experiment(f"SA temp={t}, cooling={c}",
                           lambda t=t, c=c: simulated_annealing(
                               random_state(), temp=t, cooling_rate=c),
                           trials=50)