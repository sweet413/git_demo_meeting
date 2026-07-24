import pandas as pd
import numpy as np

dates = pd.date_range(start='2025-01-01', periods=200, freq='D')
trend = np.linspace(15, 25, 200)
seasonal = 8 * np.sin(np.linspace(0, 10*np.pi, 200))
noise = np.random.normal(0, 2, 200)
temperature = trend + seasonal + noise

df = pd.DataFrame({'date': dates, 'temp': temperature})
df.to_csv('weather.csv', index=False)
print("数据生成成功！前5行：")
print(df.head())
print("123")
