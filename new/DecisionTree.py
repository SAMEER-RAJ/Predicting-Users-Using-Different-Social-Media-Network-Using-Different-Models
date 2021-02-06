import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#%matplotlib inline

from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

df=pd.read_csv('C:\\Users\\HP\\OneDrive\\Desktop\\proc\\^BSESN.csv')
df.index=df['Date']

ff = pd.DataFrame(df, columns=['Close'])
ff=ff.reset_index()
ff['Date']=pd.to_datetime(ff.Date,format='%Y-%m-%d')
ff.isna().values.any()
ff.dropna(inplace=True)
import matplotlib.dates as mdates

years = mdates.YearLocator() # Get every year
yearsFmt = mdates.DateFormatter('%Y') # Set year format

# Create subplots to plot graph and control axes
fig, ax = plt.subplots()
ax.plot(ff['Date'], ff['Close'])

# Format the ticks
ax.xaxis.set_major_locator(years)
ax.xaxis.set_major_formatter(yearsFmt)

lo=str(ff.Date.dt.year[0])

hi=str(ff.Date.dt.year[len(ff.Date)-1])


# Set figure title
plt.title('Close Number Of Users History '+lo+'-'+hi, fontsize=16)
# Set x label
plt.xlabel('Date', fontsize=14)
# Set y label
plt.ylabel('Closing Number Of Users ', fontsize=14)

# Rotate and align the x labels
fig.autofmt_xdate()

# Show plot
plt.show()




# Import package for splitting data set
from sklearn.model_selection import train_test_split
#from sklearn.svm import SVR

train, test = train_test_split(ff, test_size=0.20)

# Reshape index column to 2D array for .fit() method
X_train = np.array(train.index).reshape(-1, 1)
y_train = train['Close']



X_test = np.array(test.index).reshape(-1, 1)
y_test = test['Close']

y_train=y_train.astype('int')
y_test=y_test.astype('int')

#from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeClassifier 
model = DecisionTreeClassifier()
# Fit linear model using the train data set
model.fit(X_train, y_train)


y_pred = model.predict(X_test)
ff['Prediction'] = model.predict(np.array(ff.index).reshape(-1, 1))
randints = np.random.randint(2550, size=25)

# Select row numbers == random numbers
df_sample = ff[ff.index.isin(randints)]

# Create subplots to plot graph and control axes
fig, ax = plt.subplots()
df_sample.plot(x='Date', y=['Close', 'Prediction'], kind='bar', ax=ax)

# Set figure title
plt.title('Decision Tree->Comparison Predicted vs Actual Number Of Users in Sample data selection', fontsize=16)

# 

# Set x label
plt.xlabel('Date', fontsize=14)

# Set y label
plt.ylabel('Number Of Users', fontsize=14)

# Show plot
plt.show()




from sklearn.metrics import explained_variance_score
print('Accuracy by DecisionTree -> ',explained_variance_score(y_test, y_pred))

