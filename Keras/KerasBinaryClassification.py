import tensorflow as tf
from keras.models import Sequential
import pandas as pd
from keras.layers import Dense

url = 'https://raw.githubusercontent.com/werowe/logisticRegressionBestModel/master/KidCreative.csv'

data = pd.read_csv(url, delimiter=',')

labels=data['Buy']
features = data.iloc[:,2:16]

model = Sequential()

model.add(Dense(units=64, activation='relu', input_dim=1))
model.add(Dense(units=14, activation='softmax'))

model.compile(loss='categorical_crossentropy',
              optimizer='sgd',
              metrics=['accuracy'])

model.fit(labels, features,
          batch_size=12,
          epochs=10,
          verbose=1,
          validation_data=(labels, features))
          
model.evaluate(labels, features, verbose=0)

model.summary()
