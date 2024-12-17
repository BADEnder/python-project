import tensorflow as tf
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Embedding, Dense, GlobalAveragePooling1D, Concatenate, Dropout
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

import pandas as pd
import numpy as np

from matplotlib import pyplot as plt 
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split





# Load dataset (replace with your CSV file)
data = pd.read_csv('data.csv')  

cols = ['site', 'pno', 'label1', 'label2', 'label3', 'desc_cn', 'spec', 'desc_en']
data.columns = cols

data = data.drop(labels=['site', 'spec'], axis=1)

data['pno'] = data['pno'].astype('str')
data['desc_cn'] = data['desc_cn'].astype('str')
data['desc_en'] = data['desc_en'].astype('str')

# data.head()

# Preprocess features
text_features = data[['pno', 'desc_cn', 'desc_en']].apply(lambda x: ' '.join(x), axis=1)  # Combine text features



# Tokenize text
max_words = 10000
max_len = 100
tokenizer = Tokenizer(num_words=max_words, oov_token='<OOV>')
tokenizer.fit_on_texts(text_features)
text_sequences = tokenizer.texts_to_sequences(text_features)
text_padded = pad_sequences(text_sequences, maxlen=max_len, padding='post')

# Preprocess labels
label_encoders = {col: LabelEncoder() for col in ['label1', 'label2', 'label3']}
for col in label_encoders:
    data[col] = label_encoders[col].fit_transform(data[col])

labels = np.stack((data['label1'], data['label2'], data['label3']), axis=1)
# labels = [data['label1'], data['label2'], data['label3']]


# print(labels.shape)
# print(text_padded.shape)


# Split data
X_text_train, X_text_test, y_train, y_test = train_test_split(
    text_padded, labels, test_size=0.2, random_state=42
    # text_padded, numeric_features, labels, test_size=0.2, random_state=42
)



# Convert labels to tensors
y_train = [tf.convert_to_tensor(y) for y in zip(*y_train)]
y_test = [tf.convert_to_tensor(y) for y in zip(*y_test)]
# y_train = np.stack([tf.convert_to_tensor(y) for y in zip(*y_train)], axis=1)
# y_test = np.stack([tf.convert_to_tensor(y) for y in zip(*y_test)], axis=1)



# Define model
text_input = Input(shape=(max_len,), name="text_input")

# Text processing layers
embedding = Embedding(max_words, 128)(text_input)
text_representation = GlobalAveragePooling1D()(embedding)

# Concatenate features
combined_features = Concatenate()([text_representation])

# Shared layers
shared = Dense(128, activation='relu')(combined_features)
shared = Dropout(0.5)(shared)

# Separate outputs for each label
label1_output = Dense(len(label_encoders['label1'].classes_), activation='softmax', name="label1_output")(shared)
label2_output = Dense(len(label_encoders['label2'].classes_), activation='softmax', name="label2_output")(shared)
label3_output = Dense(len(label_encoders['label3'].classes_), activation='softmax', name="label3_output")(shared)



# Compile model
model = Model(inputs=[text_input], outputs=[label1_output, label2_output, label3_output])
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=[['accuracy'], ['accuracy'], ['accuracy']]
              )



# # Train the model
history = model.fit(
    X_text_train, y_train,
    validation_data=([X_text_test], y_test),
    epochs=10,
    batch_size=32
)

# Evaluate
# results = model.evaluate([X_text_test, X_num_test], y_test)
results = model.evaluate(X_text_test, y_test)
print("Evaluation Results:", results)



# len(predict)
# len(predict[0])

# Check Data
predict = model.predict(X_text_test)
test_result = [list(np.array(y_test[i])) for i in range(3)]
count = 0
length = len(X_text_test)

# target = 1
for target in range(length):
    for i in range(3):
        # order = np.argmax(predict[i][target])
        if np.argmax(predict[i][target]) != test_result[i][target]:
            # print(np.argmax(predict[0][target]))
            predict_result = []
            current_result = []
            for j in range(3):
              predict_result.append(list(label_encoders[f'label{j+1}'].inverse_transform([np.argmax(predict[j][target])])))
              current_result.append(list(label_encoders[f'label{j+1}'].inverse_transform([test_result[j][target]])))
            print('target: ', target)
            print('predict result: ', predict_result)
            print('current result: ', current_result)

            count += 1
            break 


        # if count < 3:
        #     print(target)
print(count)
# print(predict_result)



def plot_val_accur():
    plt.plot(history.history['val_label1_output_accuracy'])
    plt.plot(history.history['val_label2_output_accuracy'])
    plt.plot(history.history['val_label3_output_accuracy'])
    plt.title('Model Validation Accuracy')
    plt.ylabel('Validation Accuracy')
    plt.xlabel('Epoch')
    plt.legend(['label1', 'label2', 'label3'], loc='upper left')
    plt.show()

def plot_val_loss():
    plt.plot(history.history['val_label1_output_loss'])
    plt.plot(history.history['val_label2_output_loss'])
    plt.plot(history.history['val_label3_output_loss'])
    plt.title('Model Validation loss')
    plt.ylabel('Validation loss')
    plt.xlabel('Epoch')
    plt.legend(['label1', 'label2', 'label3'], loc='upper left')
    plt.show()
