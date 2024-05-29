import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({'font.size': 15})


arrayFile = './results.npz'
npzdata = np.load(arrayFile, allow_pickle=False)


sieve_results = npzdata['sieve_results']
swap_results = npzdata['swap_results'] 
encompassing_results = npzdata['encompassing_results']
chasing_results = npzdata['chasing_results'] 

sieve_consistency = npzdata['sieve_consistency'] 
swap_consistency = npzdata['swap_consistency']
encompassing_consistency = npzdata['encompassing_consistency']
chasing_consistency = npzdata['chasing_consistency']           

plt.plot(sieve_results, '--',label = 'Sieve')
plt.plot(swap_results, '--',label = 'Swapping')
plt.plot(chasing_results, label = 'Chasing')
plt.plot(encompassing_results, label = 'Encompassing')
plt.xlabel('Stream')
plt.ylabel('Value')
plt.legend()
plt.savefig('rome-kmedoid-objective.pdf',bbox_inches='tight')
plt.close()


plt.plot(sieve_consistency,'--', label = 'Sieve')
plt.plot(swap_consistency, '--',label = 'Swapping')
plt.plot(chasing_consistency, label = 'Chasing')
plt.plot(encompassing_consistency, label = 'Encompassing')
plt.xlabel('Stream')
plt.ylabel('Consistency')
plt.legend()
plt.savefig('rome-kmedoid-consistency.pdf',bbox_inches='tight')
plt.close()

