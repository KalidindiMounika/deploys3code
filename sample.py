##Contains Duplicates

import numpy as np
arr = np.array([10,20,13,11,20,17,14,10])
for i in range(len(arr)-1,0,-1):
    for j in range(i):
        if arr[j] == arr[i]:
            print(arr[j])
