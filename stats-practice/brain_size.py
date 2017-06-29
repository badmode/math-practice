import pandas
import matplotlib.pyplot as plt
data = pandas.read_csv('brain_size.csv', sep=';', na_values=".")
print(data)
# .describe() shows the basic statistical character of the data
print(data.describe())
pandas.plotting.scatter_matrix(data[['Weight', 'Height', 'MRI_Count']])

# for some reason pandas scatters are no-shows. Need plt etc . . . 
plt.show()
