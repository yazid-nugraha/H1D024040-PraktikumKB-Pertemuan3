import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzz
from skfuzzy import control as ctrl

info    = ctrl.Antecedent(np.arange(0, 101, 1), 'kejelasan_informasi')
syarat  = ctrl.Antecedent(np.arange(0, 101, 1), 'kejelasan_persyaratan')
petugas = ctrl.Antecedent(np.arange(0, 101, 1), 'kemampuan_petugas')
sarpas  = ctrl.Antecedent(np.arange(0, 101, 1), 'ketersediaan_sarpas')
puas    = ctrl.Consequent(np.arange(0, 401, 1), 'kepuasan_pelayanan')

for var in [info, syarat, petugas, sarpas]:
    var['tidak']     = fuzz.trapmf(var.universe, [0,  0,  60, 75])
    var['cukup']     = fuzz.trimf (var.universe, [60, 75, 90])
    var['memuaskan'] = fuzz.trapmf(var.universe, [75, 90, 100, 100])

puas['tidak']     = fuzz.trapmf(puas.universe, [0,   0,   50,  75])
puas['kurang']    = fuzz.trapmf(puas.universe, [50,  75,  100, 150])
puas['cukup']     = fuzz.trapmf(puas.universe, [100, 150, 250, 275])
puas['memuaskan'] = fuzz.trapmf(puas.universe, [250, 275, 325, 350])
puas['sangat']    = fuzz.trapmf(puas.universe, [325, 350, 400, 400])

r1  = ctrl.Rule(info['tidak']     & syarat['tidak']     & petugas['tidak']     & sarpas['tidak'],     puas['kurang'])
r2  = ctrl.Rule(info['tidak']     & syarat['tidak']     & petugas['tidak']     & sarpas['cukup'],     puas['cukup'])
r3  = ctrl.Rule(info['tidak']     & syarat['tidak']     & petugas['tidak']     & sarpas['memuaskan'], puas['cukup'])
r4  = ctrl.Rule(info['tidak']     & syarat['tidak']     & petugas['cukup']     & sarpas['tidak'],     puas['cukup'])
r5  = ctrl.Rule(info['tidak']     & syarat['tidak']     & petugas['cukup']     & sarpas['cukup'],     puas['cukup'])
r6  = ctrl.Rule(info['tidak']     & syarat['tidak']     & petugas['cukup']     & sarpas['memuaskan'], puas['cukup'])
r7  = ctrl.Rule(info['tidak']     & syarat['tidak']     & petugas['memuaskan'] & sarpas['tidak'],     puas['cukup'])
r8  = ctrl.Rule(info['tidak']     & syarat['tidak']     & petugas['memuaskan'] & sarpas['cukup'],     puas['cukup'])
r9  = ctrl.Rule(info['tidak']     & syarat['tidak']     & petugas['memuaskan'] & sarpas['memuaskan'], puas['memuaskan'])
r10 = ctrl.Rule(info['tidak']     & syarat['cukup']     & petugas['tidak']     & sarpas['tidak'],     puas['cukup'])
r11 = ctrl.Rule(info['tidak']     & syarat['cukup']     & petugas['tidak']     & sarpas['cukup'],     puas['cukup'])
r12 = ctrl.Rule(info['tidak']     & syarat['cukup']     & petugas['tidak']     & sarpas['memuaskan'], puas['cukup'])
r13 = ctrl.Rule(info['tidak']     & syarat['cukup']     & petugas['cukup']     & sarpas['tidak'],     puas['cukup'])
r14 = ctrl.Rule(info['tidak']     & syarat['cukup']     & petugas['cukup']     & sarpas['cukup'],     puas['cukup'])
r15 = ctrl.Rule(info['tidak']     & syarat['cukup']     & petugas['cukup']     & sarpas['memuaskan'], puas['memuaskan'])
r16 = ctrl.Rule(info['tidak']     & syarat['cukup']     & petugas['memuaskan'] & sarpas['tidak'],     puas['cukup'])
r17 = ctrl.Rule(info['tidak']     & syarat['cukup']     & petugas['memuaskan'] & sarpas['cukup'],     puas['memuaskan'])
r18 = ctrl.Rule(info['tidak']     & syarat['cukup']     & petugas['memuaskan'] & sarpas['memuaskan'], puas['memuaskan'])
r19 = ctrl.Rule(info['tidak']     & syarat['memuaskan'] & petugas['tidak']     & sarpas['tidak'],     puas['cukup'])
r20 = ctrl.Rule(info['tidak']     & syarat['memuaskan'] & petugas['tidak']     & sarpas['cukup'],     puas['cukup'])
r21 = ctrl.Rule(info['tidak']     & syarat['memuaskan'] & petugas['tidak']     & sarpas['memuaskan'], puas['memuaskan'])
r22 = ctrl.Rule(info['tidak']     & syarat['memuaskan'] & petugas['cukup']     & sarpas['tidak'],     puas['cukup'])
r23 = ctrl.Rule(info['tidak']     & syarat['memuaskan'] & petugas['cukup']     & sarpas['cukup'],     puas['memuaskan'])
r24 = ctrl.Rule(info['tidak']     & syarat['memuaskan'] & petugas['cukup']     & sarpas['memuaskan'], puas['memuaskan'])
r25 = ctrl.Rule(info['tidak']     & syarat['memuaskan'] & petugas['memuaskan'] & sarpas['tidak'],     puas['memuaskan'])
r26 = ctrl.Rule(info['tidak']     & syarat['memuaskan'] & petugas['memuaskan'] & sarpas['cukup'],     puas['memuaskan'])
r27 = ctrl.Rule(info['tidak']     & syarat['memuaskan'] & petugas['memuaskan'] & sarpas['memuaskan'], puas['sangat'])
r28 = ctrl.Rule(info['cukup']     & syarat['tidak']     & petugas['tidak']     & sarpas['tidak'],     puas['cukup'])
r29 = ctrl.Rule(info['cukup']     & syarat['tidak']     & petugas['tidak']     & sarpas['cukup'],     puas['cukup'])
r30 = ctrl.Rule(info['cukup']     & syarat['tidak']     & petugas['tidak']     & sarpas['memuaskan'], puas['cukup'])
r31 = ctrl.Rule(info['cukup']     & syarat['tidak']     & petugas['cukup']     & sarpas['tidak'],     puas['cukup'])
r32 = ctrl.Rule(info['cukup']     & syarat['tidak']     & petugas['cukup']     & sarpas['cukup'],     puas['cukup'])
r33 = ctrl.Rule(info['cukup']     & syarat['tidak']     & petugas['cukup']     & sarpas['memuaskan'], puas['memuaskan'])
r34 = ctrl.Rule(info['cukup']     & syarat['tidak']     & petugas['memuaskan'] & sarpas['tidak'],     puas['cukup'])
r35 = ctrl.Rule(info['cukup']     & syarat['tidak']     & petugas['memuaskan'] & sarpas['cukup'],     puas['memuaskan'])
r36 = ctrl.Rule(info['cukup']     & syarat['tidak']     & petugas['memuaskan'] & sarpas['memuaskan'], puas['memuaskan'])
r37 = ctrl.Rule(info['cukup']     & syarat['cukup']     & petugas['tidak']     & sarpas['tidak'],     puas['cukup'])
r38 = ctrl.Rule(info['cukup']     & syarat['cukup']     & petugas['tidak']     & sarpas['cukup'],     puas['cukup'])
r39 = ctrl.Rule(info['cukup']     & syarat['cukup']     & petugas['tidak']     & sarpas['memuaskan'], puas['memuaskan'])
r40 = ctrl.Rule(info['cukup']     & syarat['cukup']     & petugas['cukup']     & sarpas['tidak'],     puas['cukup'])
r41 = ctrl.Rule(info['cukup']     & syarat['cukup']     & petugas['cukup']     & sarpas['cukup'],     puas['memuaskan'])
r42 = ctrl.Rule(info['cukup']     & syarat['cukup']     & petugas['cukup']     & sarpas['memuaskan'], puas['memuaskan'])
r43 = ctrl.Rule(info['cukup']     & syarat['cukup']     & petugas['memuaskan'] & sarpas['tidak'],     puas['memuaskan'])
r44 = ctrl.Rule(info['cukup']     & syarat['cukup']     & petugas['memuaskan'] & sarpas['cukup'],     puas['memuaskan'])
r45 = ctrl.Rule(info['cukup']     & syarat['cukup']     & petugas['memuaskan'] & sarpas['memuaskan'], puas['sangat'])
r46 = ctrl.Rule(info['cukup']     & syarat['memuaskan'] & petugas['tidak']     & sarpas['tidak'],     puas['cukup'])
r47 = ctrl.Rule(info['cukup']     & syarat['memuaskan'] & petugas['tidak']     & sarpas['cukup'],     puas['memuaskan'])
r48 = ctrl.Rule(info['cukup']     & syarat['memuaskan'] & petugas['tidak']     & sarpas['memuaskan'], puas['memuaskan'])
r49 = ctrl.Rule(info['cukup']     & syarat['memuaskan'] & petugas['cukup']     & sarpas['tidak'],     puas['memuaskan'])
r50 = ctrl.Rule(info['cukup']     & syarat['memuaskan'] & petugas['cukup']     & sarpas['cukup'],     puas['memuaskan'])
r51 = ctrl.Rule(info['cukup']     & syarat['memuaskan'] & petugas['cukup']     & sarpas['memuaskan'], puas['sangat'])
r52 = ctrl.Rule(info['cukup']     & syarat['memuaskan'] & petugas['memuaskan'] & sarpas['tidak'],     puas['memuaskan'])
r53 = ctrl.Rule(info['cukup']     & syarat['memuaskan'] & petugas['memuaskan'] & sarpas['cukup'],     puas['sangat'])
r54 = ctrl.Rule(info['cukup']     & syarat['memuaskan'] & petugas['memuaskan'] & sarpas['memuaskan'], puas['sangat'])
r55 = ctrl.Rule(info['memuaskan'] & syarat['tidak']     & petugas['tidak']     & sarpas['tidak'],     puas['cukup'])
r56 = ctrl.Rule(info['memuaskan'] & syarat['tidak']     & petugas['tidak']     & sarpas['cukup'],     puas['cukup'])
r57 = ctrl.Rule(info['memuaskan'] & syarat['tidak']     & petugas['tidak']     & sarpas['memuaskan'], puas['memuaskan'])
r58 = ctrl.Rule(info['memuaskan'] & syarat['tidak']     & petugas['cukup']     & sarpas['tidak'],     puas['cukup'])
r59 = ctrl.Rule(info['memuaskan'] & syarat['tidak']     & petugas['cukup']     & sarpas['cukup'],     puas['memuaskan'])
r60 = ctrl.Rule(info['memuaskan'] & syarat['tidak']     & petugas['cukup']     & sarpas['memuaskan'], puas['memuaskan'])
r61 = ctrl.Rule(info['memuaskan'] & syarat['tidak']     & petugas['memuaskan'] & sarpas['tidak'],     puas['memuaskan'])
r62 = ctrl.Rule(info['memuaskan'] & syarat['tidak']     & petugas['memuaskan'] & sarpas['cukup'],     puas['memuaskan'])
r63 = ctrl.Rule(info['memuaskan'] & syarat['tidak']     & petugas['memuaskan'] & sarpas['memuaskan'], puas['sangat'])
r64 = ctrl.Rule(info['memuaskan'] & syarat['cukup']     & petugas['tidak']     & sarpas['tidak'],     puas['cukup'])
r65 = ctrl.Rule(info['memuaskan'] & syarat['cukup']     & petugas['tidak']     & sarpas['cukup'],     puas['memuaskan'])
r66 = ctrl.Rule(info['memuaskan'] & syarat['cukup']     & petugas['tidak']     & sarpas['memuaskan'], puas['memuaskan'])
r67 = ctrl.Rule(info['memuaskan'] & syarat['cukup']     & petugas['cukup']     & sarpas['tidak'],     puas['memuaskan'])
r68 = ctrl.Rule(info['memuaskan'] & syarat['cukup']     & petugas['cukup']     & sarpas['cukup'],     puas['memuaskan'])
r69 = ctrl.Rule(info['memuaskan'] & syarat['cukup']     & petugas['cukup']     & sarpas['memuaskan'], puas['sangat'])
r70 = ctrl.Rule(info['memuaskan'] & syarat['cukup']     & petugas['memuaskan'] & sarpas['tidak'],     puas['memuaskan'])
r71 = ctrl.Rule(info['memuaskan'] & syarat['cukup']     & petugas['memuaskan'] & sarpas['cukup'],     puas['sangat'])
r72 = ctrl.Rule(info['memuaskan'] & syarat['cukup']     & petugas['memuaskan'] & sarpas['memuaskan'], puas['sangat'])
r73 = ctrl.Rule(info['memuaskan'] & syarat['memuaskan'] & petugas['tidak']     & sarpas['tidak'],     puas['memuaskan'])
r74 = ctrl.Rule(info['memuaskan'] & syarat['memuaskan'] & petugas['tidak']     & sarpas['cukup'],     puas['memuaskan'])
r75 = ctrl.Rule(info['memuaskan'] & syarat['memuaskan'] & petugas['tidak']     & sarpas['memuaskan'], puas['sangat'])
r76 = ctrl.Rule(info['memuaskan'] & syarat['memuaskan'] & petugas['cukup']     & sarpas['tidak'],     puas['memuaskan'])
r77 = ctrl.Rule(info['memuaskan'] & syarat['memuaskan'] & petugas['cukup']     & sarpas['cukup'],     puas['sangat'])
r78 = ctrl.Rule(info['memuaskan'] & syarat['memuaskan'] & petugas['cukup']     & sarpas['memuaskan'], puas['sangat'])
r79 = ctrl.Rule(info['memuaskan'] & syarat['memuaskan'] & petugas['memuaskan'] & sarpas['tidak'],     puas['sangat'])
r80 = ctrl.Rule(info['memuaskan'] & syarat['memuaskan'] & petugas['memuaskan'] & sarpas['cukup'],     puas['sangat'])
r81 = ctrl.Rule(info['memuaskan'] & syarat['memuaskan'] & petugas['memuaskan'] & sarpas['memuaskan'], puas['sangat'])

sistem   = ctrl.ControlSystem([
    r1,  r2,  r3,  r4,  r5,  r6,  r7,  r8,  r9,
    r10, r11, r12, r13, r14, r15, r16, r17, r18,
    r19, r20, r21, r22, r23, r24, r25, r26, r27,
    r28, r29, r30, r31, r32, r33, r34, r35, r36,
    r37, r38, r39, r40, r41, r42, r43, r44, r45,
    r46, r47, r48, r49, r50, r51, r52, r53, r54,
    r55, r56, r57, r58, r59, r60, r61, r62, r63,
    r64, r65, r66, r67, r68, r69, r70, r71, r72,
    r73, r74, r75, r76, r77, r78, r79, r80, r81
])
simulasi = ctrl.ControlSystemSimulation(sistem)

simulasi.input['kejelasan_informasi']   = 80
simulasi.input['kejelasan_persyaratan'] = 60
simulasi.input['kemampuan_petugas']     = 50
simulasi.input['ketersediaan_sarpas']   = 90

simulasi.compute()
hasil = simulasi.output['kepuasan_pelayanan']

print("--- HASIL PERHITUNGAN LOGIKA FUZZY ---")
print(f"Kejelasan Informasi   : 80")
print(f"Kejelasan Persyaratan : 60")
print(f"Kemampuan Petugas     : 50")
print(f"Ketersediaan Sarpas   : 90")
print("--------------------------------------")
print(f"Kepuasan Masyarakat   : {hasil:.2f}")

info.view()
syarat.view()
petugas.view()
sarpas.view()
puas.view()
puas.view(sim=simulasi)
plt.show()