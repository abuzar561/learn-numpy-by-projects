import numpy as np
data = np.array([
                [10, 20, 30], 
                [40, 50, 60], 
                [70, 80, 90]
    ])

reshaped_data = data.reshape(3, 3)
print ('\nArray:', data)
print ('\nShape:', data.shape)
print ('\nSize:', data.size)
print ('\nDaimantion:', data.ndim)
print ('\nReshaped data:', reshaped_data)
