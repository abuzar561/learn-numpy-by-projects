# 💡 Project: “Dice Roll Simulator & Analyzer” 🎲
import numpy as np

rolls = np.random.randint(1, 7, size=100)
print('all Dice rolls\n:', rolls)

for i in range (1, 7):
    count = np.count_nonzero(rolls == i)
    print (f'number {i} came {count} times.')

value, count = np.unique(rolls, return_counts=True)
most_common = value[np.argmax(count)]
print("\nMost frequent number:", most_common)