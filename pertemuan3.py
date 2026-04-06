import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzz
from skfuzzy import control as ctrl

terjual  = ctrl.Antecedent(np.arange(0, 101, 1),     'barang_terjual')
minta    = ctrl.Antecedent(np.arange(0, 301, 1),     'permintaan')
harga    = ctrl.Antecedent(np.arange(0, 100001, 1),  'harga_item')
profit   = ctrl.Antecedent(np.arange(0, 4000001, 1), 'profit')
stok     = ctrl.Consequent(np.arange(0, 1001, 1),    'stok_makanan')

terjual['rendah'] = fuzz.trimf(terjual.universe, [0,  0,  40])
terjual['sedang'] = fuzz.trimf(terjual.universe, [30, 50, 70])
terjual['tinggi'] = fuzz.trimf(terjual.universe, [60, 100, 100])

minta['rendah'] = fuzz.trimf(minta.universe, [0,   0,   100])
minta['sedang'] = fuzz.trimf(minta.universe, [50,  150, 250])
minta['tinggi'] = fuzz.trimf(minta.universe, [200, 300, 300])

harga['murah'] = fuzz.trimf(harga.universe, [0,     0,      40000])
harga['sedang'] = fuzz.trimf(harga.universe, [30000, 50000,  80000])
harga['mahal'] = fuzz.trimf(harga.universe, [60000, 100000, 100000])

profit['rendah'] = fuzz.trimf( profit.universe, [0,       0,       1000000])
profit['sedang'] = fuzz.trimf( profit.universe, [1000000, 2000000, 2500000])
profit['banyak'] = fuzz.trapmf(profit.universe, [1500000, 2500000, 4000000, 4000000])

stok['sedang'] = fuzz.trimf(stok.universe, [100, 500,  900])
stok['banyak'] = fuzz.trimf(stok.universe, [600, 1000, 1000])

r1 = ctrl.Rule(terjual['tinggi'] & minta['tinggi'] & harga['murah'] & profit['banyak'], stok['banyak'])
r2 = ctrl.Rule(terjual['tinggi'] & minta['tinggi'] & harga['murah'] & profit['sedang'], stok['sedang'])
r3 = ctrl.Rule(terjual['tinggi'] & minta['sedang'] & harga['murah'] & profit['sedang'], stok['sedang'])
r4 = ctrl.Rule(terjual['sedang'] & minta['tinggi'] & harga['murah'] & profit['sedang'], stok['sedang'])
r5 = ctrl.Rule(terjual['sedang'] & minta['tinggi'] & harga['murah'] & profit['banyak'], stok['banyak'])
r6 = ctrl.Rule(terjual['rendah'] & minta['rendah'] & harga['sedang'] & profit['sedang'], stok['sedang'])

sistem   = ctrl.ControlSystem([r1, r2, r3, r4, r5, r6])
simulasi = ctrl.ControlSystemSimulation(sistem)

simulasi.input['barang_terjual'] = 80
simulasi.input['permintaan']     = 255
simulasi.input['harga_item']     = 25000
simulasi.input['profit']         = 3500000

simulasi.compute()
hasil = simulasi.output['stok_makanan']

print("--- HASIL PERHITUNGAN LOGIKA FUZZY ---")
print(f"Barang Terjual : 80")
print(f"Permintaan     : 255")
print(f"Harga per Item : 25.000")
print(f"Profit         : 3.500.000")
print("--------------------------------------")
print(f"Rekomendasi Stok: {hasil:.2f} unit")

terjual.view()
minta.view()
harga.view()
profit.view()
stok.view()
stok.view(sim=simulasi)
plt.show()