import math
import cmath
import matplotlib.pyplot as plt

complex_numbers = [
    complex(1,1), 
    complex(2,1), 
    complex(6,3), 
    complex(-3,4), 
    complex(6,-1)
]

cn_sum = sum(complex_numbers)
print("Sum of numbers is : ", cn_sum)

for c in complex_numbers:
    r, phi = cmath.polar(c)
    plt.polar([0,phi],[0,r], marker='o')
    print(c)
