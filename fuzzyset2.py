import numpy as np
import matplotlib.pyplot as plt

def equation_of_line(x1, y1, x2, y2):
    slope = (y2 - y1) / (x2 - x1)
    intercept = y1 - slope * x1
    return lambda x: slope * x + intercept

def fuzzy_set_cool(temp):
    if temp <= 10:
        return 1.0
    elif temp >= 20:
        return 0.0
    else:
        line = equation_of_line(10, 1, 20, 0)
        return line(temp)

def fuzzy_set_warm(temp):
    if temp <= 15:
        return 0.0
    elif temp >= 25:
        return 1.0
    else:
        line = equation_of_line(15, 0, 25, 1)
        return line(temp)

def fuzzy_set_union(fuzzy_set1, fuzzy_set2):
    return lambda x: max(fuzzy_set1(x), fuzzy_set2(x))

def fuzzy_set_intersection(fuzzy_set1, fuzzy_set2):
    return lambda x: min(fuzzy_set1(x), fuzzy_set2(x))

def fuzzy_set_complement(fuzzy_set):
    return lambda x: 1.0 - fuzzy_set(x)

# Test the functions by plotting fuzzy sets, union, intersection and complement
x = np.linspace(0, 30, 200)
y_cool = [fuzzy_set_cool(temp) for temp in x]
y_warm = [fuzzy_set_warm(temp) for temp in x]
y_union = [fuzzy_set_union(fuzzy_set_cool, fuzzy_set_warm)(temp) for temp in x]
y_intersection = [fuzzy_set_intersection(fuzzy_set_cool, fuzzy_set_warm)(temp) for temp in x]
y_complement_cool = [fuzzy_set_complement(fuzzy_set_cool)(temp) for temp in x]
y_complement_warm = [fuzzy_set_complement(fuzzy_set_warm)(temp) for temp in x]

fig, axs = plt.subplots(3, 2, figsize=(10, 10))
fig.suptitle('Fuzzy Sets and Operations')

axs[0, 0].plot(x, y_cool, label='Cool')
axs[0, 0].set_title('Cool Fuzzy Set')
axs[0, 0].legend()
plt.plot(x,y_cool)

axs[0, 1].plot(x, y_warm, label='Warm')
axs[0, 1].set_title('Warm Fuzzy Set')
axs[0, 1].legend()
plt.plot(x,y_warm)

axs[1, 0].plot(x, y_union, label='Union')
axs[1, 0].set_title('Union of Cool and Warm')
axs[1, 0].legend()
plt.plot(x,y_union)

axs[1, 1].plot(x, y_intersection, label='Intersection')
axs[1, 1].set_title('Intersection of Cool and Warm')
axs[1, 1].legend()
plt.plot(x,y_intersection)

axs[2, 0].plot(x, y_complement_cool, label='Complement of Cool')
axs[2, 0].set_title('Complement of Cool')
axs[2, 0].legend()
plt.plot(x,y_complement_cool)

axs[2, 1].plot(x, y_complement_warm, label='Complement of Warm')
axs[2, 1].set_title('Complement of Warm')
axs[2, 1].legend()
plt.plot(x,y_complement_warm)

plt.subplots_adjust(hspace= 0.5)
plt.show()