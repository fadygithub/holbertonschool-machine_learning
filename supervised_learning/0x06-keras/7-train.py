#!/usr/bin/env python3
"""Learning rate decay Module"""
import tensorflow.keras as K


def train_model(network, data, labels, batch_size,
                epochs, validation_data=None,
                early_stopping=False, patience=0,
                learning_rate_decay=False, alpha=0.1,
                decay_rate=1, verbose=True, shuffle=False):
    """Function that performs learning rate decay if validation_data exists"""
    if validation_data:
        early_stop = K.callbacks.EarlyStopping(
            monitor='val_loss', mode='min', patience=patience)
        early_stop = [early_stop]
        if learning_rate_decay is True:
            def scheduler(epoch):
                return alpha / (1 + decay_rate * epoch)
            lr_decay = K.callbacks.LearningRateScheduler(
                schedule=scheduler, verbose=1)
            early_stop.append(lr_decay)
    else:
        early_stop = None
    History = network.fit(
                        x=data,
                        y=labels,
                        batch_size=batch_size,
                        epochs=epochs,
                        verbose=verbose,
                        shuffle=shuffle,
                        validation_data=validation_data,
                        callbacks=early_stop)
    return History
