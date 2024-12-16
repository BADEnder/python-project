import pandas as pd 
import numpy as np
import tensorflow as tf
import tensorflow_hub as hub
from matplotlib import pyplot as plt

cols = ['site', 'pno', 'category_1', 'category_2', 'category_3', 'desc_cn', 'spec', 'desc_en']

df = pd.read_csv('data.csv')
# df = pd.read_csv('sample_data.csv')
df.columns = cols


df['label'] = df['category_1']
# df['label'] = df['category_1'] + '_' + df['category_2'] + '_' + df['category_3']


remove_cols = ['category_1', 'category_2', 'category_3']
x_cols = ['site', 'pno', 'desc_cn', 'spec', 'desc_en']

df = df.drop(labels=remove_cols, axis=1)

check_set = set(df['label'].unique())
dict = {}
c = 0
for i in check_set:
    if i not in dict:
        dict[i] = c
        c += 1


df['label'] = df['label'].map(dict)


tokenizer = tf.keras.preprocessing.text.Tokenizer(num_words=500000)
pad_sequences = tf.keras.preprocessing.sequence.pad_sequences

for col in x_cols:
    df[col] = df[col].astype('str')

for col in x_cols:
    tokenizer.fit_on_texts(df[col])

for col in x_cols:
    df[col] = tokenizer.texts_to_sequences(df[col])
    # df[col].values = pad_sequences(df[col].values, maxlen=50)


# ['site', 'pno', 'category_1', 'category_2', 'category_3', 'desc_cn', 'spec', 'desc_en']
col_site = pad_sequences(df['site'].to_numpy(), maxlen=50)
col_pno = pad_sequences(df['pno'].to_numpy(), maxlen=50)
col_desc_cn = pad_sequences(df['desc_cn'].to_numpy(), maxlen=50)
col_spec = pad_sequences(df['spec'].to_numpy(), maxlen=50)
col_desc_en = pad_sequences(df['desc_en'].to_numpy(), maxlen=50)

X, Y = np.stack((col_site, col_pno, col_desc_cn, col_spec, col_desc_en), axis=1), df['label'].values


model = tf.keras.Sequential([
      tf.keras.layers.Flatten(input_shape=(5, 50)),
      tf.keras.layers.Dense(1024, activation='relu'),
      tf.keras.layers.Dense(2048, activation='relu'),
      tf.keras.layers.Dense(len(df['label'].unique()), activation='softmax')
])

model.compile(
            optimizer='adam',
              loss='sparse_categorical_crossentropy',
            # loss=tf.compat.v1.losses.sparse_softmax_cross_entropy,
            metrics=['accuracy']
        )



history = model.fit(
  X, Y, 
  epochs=5, batch_size=32, 
  validation_split=0.2,
#   verbose=0
)


model.evaluate(X, Y)


plt.plot(history.history['accuracy'], label='accuracy')
plt.plot(history.history['val_accuracy'], label='val_accuracy')
plt.title('Accracy of Model')
plt.xlabel('Epoch')
plt.ylabel('%')
plt.legend()

plt.show()