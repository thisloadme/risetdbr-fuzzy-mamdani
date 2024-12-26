import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# Membuat variabel linguistik
permintaan = ctrl.Antecedent(np.arange(14868, 23433, 1), 'permintaan')
persediaan = ctrl.Antecedent(np.arange(1170, 3191, 1), 'persediaan')
produksi = ctrl.Consequent(np.arange(14105, 25001, 1), 'produksi')

# Membuat fungsi keanggotaan
permintaan['sedikit'] = fuzz.gaussmf(permintaan.universe, 14868, 1000)
permintaan['sedang'] = fuzz.gaussmf(permintaan.universe, 19150, 1000)
permintaan['banyak'] = fuzz.gaussmf(permintaan.universe, 23432, 1000)

# permintaan['sedikit'] = fuzz.trimf(permintaan.universe, [14868, 14868, 19150])
# permintaan['sedang'] = fuzz.trimf(permintaan.universe, [14868, 19150, 23432])
# permintaan['banyak'] = fuzz.trimf(permintaan.universe, [19150, 23432, 23432])

# permintaan.view()
# plt.show()
# exit()

persediaan['sedikit'] = fuzz.gaussmf(persediaan.universe, 1170, 1000)
persediaan['sedang'] = fuzz.gaussmf(persediaan.universe, 2180, 1000)
persediaan['banyak'] = fuzz.gaussmf(persediaan.universe, 3190, 1000)

produksi['sedikit'] = fuzz.gaussmf(produksi.universe, 14105, 1000)
produksi['sedang'] = fuzz.gaussmf(produksi.universe, 19552.5, 1000)
produksi['banyak'] = fuzz.gaussmf(produksi.universe, 25000, 1000)

# Membuat aturan
aturan1 = ctrl.Rule(permintaan['sedikit'] & persediaan['sedikit'], produksi['sedikit'])
aturan2 = ctrl.Rule(permintaan['sedikit'] & persediaan['sedikit'], produksi['sedang'])
aturan3 = ctrl.Rule(permintaan['sedikit'] & persediaan['sedang'], produksi['sedikit'])
aturan4 = ctrl.Rule(permintaan['sedikit'] & persediaan['sedang'], produksi['sedang'])
aturan5 = ctrl.Rule(permintaan['sedikit'] & persediaan['sedang'], produksi['banyak'])
aturan6 = ctrl.Rule(permintaan['sedikit'] & persediaan['banyak'], produksi['sedikit'])
aturan7 = ctrl.Rule(permintaan['sedikit'] & persediaan['banyak'], produksi['sedang'])
aturan8 = ctrl.Rule(permintaan['sedang'] & persediaan['sedikit'], produksi['sedikit'])
aturan9 = ctrl.Rule(permintaan['sedang'] & persediaan['sedikit'], produksi['sedang'])
aturan10 = ctrl.Rule(permintaan['sedang'] & persediaan['sedikit'], produksi['banyak'])
aturan11 = ctrl.Rule(permintaan['sedang'] & persediaan['sedang'], produksi['sedikit'])
aturan12 = ctrl.Rule(permintaan['sedang'] & persediaan['sedang'], produksi['sedang'])
aturan13 = ctrl.Rule(permintaan['sedang'] & persediaan['sedang'], produksi['banyak'])
aturan14 = ctrl.Rule(permintaan['sedang'] & persediaan['banyak'], produksi['sedikit'])
aturan15 = ctrl.Rule(permintaan['sedang'] & persediaan['banyak'], produksi['sedang'])
aturan16 = ctrl.Rule(permintaan['sedang'] & persediaan['banyak'], produksi['banyak'])
aturan17 = ctrl.Rule(permintaan['banyak'] & persediaan['sedikit'], produksi['sedang'])
aturan18 = ctrl.Rule(permintaan['banyak'] & persediaan['sedikit'], produksi['banyak'])
aturan19 = ctrl.Rule(permintaan['banyak'] & persediaan['sedang'], produksi['sedang'])
aturan20 = ctrl.Rule(permintaan['banyak'] & persediaan['sedang'], produksi['sedang'])
aturan21 = ctrl.Rule(permintaan['banyak'] & persediaan['banyak'], produksi['sedang'])
aturan22 = ctrl.Rule(permintaan['banyak'] & persediaan['banyak'], produksi['banyak'])

# Membuat sistem kontrol
sistem_kontrol_produksi = ctrl.ControlSystem([
    aturan1,aturan2,aturan3,aturan4,aturan5,aturan6,aturan7,aturan8,aturan9,aturan10,aturan11,aturan12,
    aturan13,aturan14,aturan15,aturan16,aturan17,aturan18,aturan19,aturan20,aturan21,aturan22
    ])
sistem_produksi = ctrl.ControlSystemSimulation(sistem_kontrol_produksi)

# Memberikan input ke sistem kontrol
sistem_produksi.input['permintaan'] = 21945
sistem_produksi.input['persediaan'] = 1824

# Melakukan komputasi
sistem_produksi.compute()

# Menampilkan hasil
print(sistem_produksi.output['produksi'])

# Menampilkan visual
produksi.view(sim=sistem_produksi)
plt.show()