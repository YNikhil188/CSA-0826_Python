import pandas as pd
import matplotlib.pyplot as plt
#from matplotlib import pyplot as plt
var = pd.read_excel("e:\\t\\1.xlsx")
var.plot(kind='box', figsize=(5,4))
plt.title('test title')
plt.xlabel('hhh')
plt.ylabel('xxx')
print(var)
plt.show()