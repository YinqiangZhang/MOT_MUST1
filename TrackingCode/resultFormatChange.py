import numpy as np
import os

if not os.path.exists('./modified_results/'):
    os.makedirs('./modified_results/')

for i in range(1, 6):
    name = 'a' + str(i)
    a1 = np.loadtxt('./results/' + name + '.txt', dtype=float, delimiter=',')
    a1 = a1[np.argsort(a1[:, 0])]
    id_num = len(np.unique(a1[:, 1]))
    print(id_num)

    np.savetxt('./modified_results/'+name+'.txt', a1[:, :6], fmt='%d,%d,%.1f,%.1f,%.1f,%.1f')
