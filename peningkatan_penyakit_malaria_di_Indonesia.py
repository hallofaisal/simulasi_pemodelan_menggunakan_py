
import numpy as np
import matplotlib.pyplot as plt

# Parameter Model
beta = 0.3  # Tingkat penularan
gamma = 0.1  # Tingkat pemulihan
N = 10000    # Total populasi
I0 = 1       # Jumlah awal terinfeksi
R0 = 0       # Jumlah awal yang sembuh
S0 = N - I0  # Jumlah awal yang rentan

# Waktu simulasi
t = np.linspace(0, 160, 160)  # 160 hari

# Inisialisasi array untuk menyimpan nilai S, I, R
S = np.zeros(len(t))
I = np.zeros(len(t))
R = np.zeros(len(t))

# Set nilai awal
S[0] = S0
I[0] = I0
R[0] = R0

# Simulasi
for day in range(1, len(t)):
    S[day] = S[day - 1] - (beta * S[day - 1] * I[day - 1] / N)
    I[day] = I[day - 1] + (beta * S[day - 1] * I[day - 1] / N) - (gamma * I[day - 1])
    R[day] = R[day - 1] + (gamma * I[day - 1])

# Visualisasi
plt.figure(figsize=(10, 6))
plt.plot(t, S, label='Rentan (S)', color='blue')
plt.plot(t, I, label='Terinfeksi (I)', color='red')
plt.plot(t, R, label='Sembuh (R)', color='green')
plt.title('Model Penyebaran Malaria (SIR)')
plt.xlabel('Hari')
plt.ylabel('Jumlah Orang')
plt.legend()
plt.grid()
plt.show()

