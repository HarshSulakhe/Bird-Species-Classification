from keras.layers import Input,Conv2D,BatchNormalization,ReLU,MaxPooling2D,Dense,Softmax,Flatten
from keras.models import Model
import keras.backend as K
import keras

class BirdNet:
    def build(width,height,depth,classes):
        shape = (height,width,depth)
        chanDim = -1
        if K.image_data_format() == "channels_first":
            shape = (depth,height,width)
            chanDim = 1

        input_img = Input(shape = shape)

        conv_1 = Conv2D(48,(3,3),padding='same')(input_img)
        conv_1 = BatchNormalization()(conv_1)
        conv_1 = ReLU()(conv_1)
        conv_1 = MaxPooling2D((2,2),strides=(2,2))(conv_1)

        conv_2 = Conv2D(64,(3,3),padding='same')(conv_1)
        conv_2 = BatchNormalization()(conv_2)
        conv_2 = ReLU()(conv_2)
        conv_2 = MaxPooling2D((2,2),strides=(2,2))(conv_2)

        conv_3 = Conv2D(128,(3,3),padding='same')(conv_2)
        conv_3 = BatchNormalization()(conv_3)
        conv_3 = ReLU()(conv_3)
        conv_3 = MaxPooling2D((2,2),strides=(2,2))(conv_3)
        conv_3 = keras.layers.concatenate([MaxPooling2D((2,2),strides=(2,2))(conv_2),conv_3], axis=-1)

        conv_4 = Conv2D(256,(3,3),padding='same')(conv_3)
        conv_4 = BatchNormalization()(conv_4)
        conv_4 = ReLU()(conv_4)
        conv_4 = MaxPooling2D((2,2),strides=(2,2))(conv_4)
        conv_4 = keras.layers.concatenate([MaxPooling2D((8,8),strides=(8,8))(conv_1),conv_4], axis=-1)

        conv_5 = Conv2D(512,(3,3),padding='same')(conv_4)
        conv_5 = BatchNormalization()(conv_5)
        conv_5 = ReLU()(conv_5)

        fc_1 = Flatten()(conv_5)
        fc_1 = Dense(4096)(fc_1)

        fc_2 = Dense(4096)(fc_1)

        predictions = Dense(200,activation='softmax')(fc_2)

        model = Model(inputs = input_img, outputs = predictions)
        return model

# model.compile(metrics=['accuracy'],loss='categorical_crossentropy',optimizer = 'adam')
