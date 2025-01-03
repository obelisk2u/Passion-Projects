import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('points.csv')
df.columns = ['x', 'y']
betas = []
alphas = []
yavg = df['y'].mean()

for column_name, column_data in df.items():
    xavg = column_data.mean()
    beta = ((column_data - xavg) * (df['y'] - yavg)).sum() / ((column_data - xavg) ** 2).sum()
    betas.append(beta)
    alpha = yavg - beta * xavg
    alphas.append(alpha)

print(alphas, betas)

line = alpha + beta * df['x']
#plt.scatter(df['x'], df['y'], color='blue', label='Data Points')
#plt.plot(df['x'], line, color='red', label='Fitted Line')
#plt.xlabel('X')
#plt.ylabel('Y')
#plt.title('Scatter Plot with Fitted Line')
#plt.show()


