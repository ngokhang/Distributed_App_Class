import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file = pd.read_csv('business_financial_records.csv')
# file_txt = pd.read_csv('business_financial_records.csv', sep='\t', header=False)
# print(file)

# Tóm tắt
# print(file.describe())
# print(file.info())

# Trích xuất dữ liệu từ 1 cột
amount = file['Amount']
# print(amount)

# Trích xuất cột dữ liệu ngày
# time = file['Date']
# dataTime = pd.to_datetime(time)
# print(dataTime[2] - dataTime[1])

# 
# plt.boxplot(amount)
# plt.xlabel('sales')
# plt.ylabel('Doanh thu (VND)')

plt.figure(figsize=[16,12])

#
plt.subplot(2, 2, 1)
file.set_index('Date')['Amount'].plot(marker='o', ls='-', color='salmon')
plt.xlabel('Ngay', fontsize=17)
plt.ylabel('Doanh thu', fontsize=17)
plt.title('Thu nhap', fontsize=17)

#
plt.subplot(2, 2, 2)
file['Payment Type'].value_counts().plot(kind='bar', color='lightblue')
plt.xlabel('Cach thanh toan', fontsize=17)
plt.ylabel('Tan suat', fontsize=17)
plt.title('Tom tat cac phuong phap', fontsize=17)

#
plt.subplot(2, 2, 3)
sns.boxplot(x="Category", y ='Amount', data=file)
plt.xlabel('Cac loai mat hang', fontsize=17)
plt.ylabel(' Doanh so', fontsize=17)
plt.title('Doanh so theo tung mat hang', fontsize=17)

# 
plt.subplot(2, 2, 4)
file['Amount'].hist(bins=30, color='lightgreen')
plt.xlabel('Doanh so', fontsize=17)
plt.ylabel(' Doanh so', fontsize=17)
plt.title('Phan bo cua doanh so', fontsize=17)

plt.tight_layout()
plt.savefig('result.png', dpi=600)


plt.show()

###################################################

import plotly as plt
import plotly.graph_objects as go

fig = go.Figure()
fig.add_trace(go.Box(y = file['Amount'], x=file['Category']))
# fig.add_trace(go.scatter(y = file['Amount'], x = file['Payment Type']))
fig.show()