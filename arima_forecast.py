import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

df = pd.read_csv('weather.csv', parse_dates=['date'])
model = ARIMA(df['temp'], order=(1,1,1))
fit = model.fit()
print("ARIMA模型AIC值：", fit.aic)

plt.figure(figsize=(10,4))
plt.plot(df['date'], df['temp'], label='原始温度')
plt.title('ARIMA模型拟合效果')
plt.legend()
plt.savefig('arima_result.png')
print("ARIMA图片已保存")
