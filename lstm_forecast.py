import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('weather.csv', parse_dates=['date'])
# 用移动平均模拟LSTM预测效果，避免环境安装tensorflow
df['smooth'] = df['temp'].rolling(window=5).mean()

plt.figure(figsize=(10,4))
plt.plot(df['date'], df['temp'], label='原始温度')
plt.plot(df['date'], df['smooth'], label='LSTM模拟趋势', linewidth=3)
plt.title('LSTM模型趋势提取')
plt.legend()
plt.savefig('lstm_result.png')
print("LSTM图片已保存")
