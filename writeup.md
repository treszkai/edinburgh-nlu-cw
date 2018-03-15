## Question 1
Refer to implementation in `rnn.py`.

## Question 2a
We modify the `rnn.py` traning code to do a grid search over parameter space, using the following values:
* Number of hidden units: `25, 50`
* Look-back in backpropagation: `0, 2, 5`
* Learning rate: `0.5, 0.1, 0.05`

To run this tuning, just execute the script with no hyperparameter arguments:
```
$> python rnn.py train-lm data dir
```

The code optimizes the RNN model using the first `1000` sentences of the training set, 
for `10` epochs. The results are listed below:

| Hidden Layer Dim  | Lookback  | Learning rate  | Loss  | Adjusted Loss |
|---|---|---|---|---|
| 25 | 0  | 0.5  | 5.0169758618374996 | 5.372951877571648  |
| 25 | 0  | 0.1  | 5.223393290312879  | 5.605366528319337  |
| 25 | 0  | 0.05 | 5.397833785903884  | 5.80177691458608   |
| 25 | 2  | 0.5  | 4.965089619975281  | 5.314530828195693  |
| 25 | 2  | 0.1  | 5.179683685857464  | 5.556151922126156  |
| 25 | 2  | 0.05 | 5.396695506807548  | 5.800495275043421  |
| __25__ | __5__  | __0.5__  | __4.9536389690632365__ | __5.301638026205992__  |
| 25 | 5  | 0.1  | 5.225334464792017  | 5.6075521838230475 |
| 25 | 5  | 0.05 | 5.374936094502318  | 5.775995375743501  |
| 50 | 0  | 0.5  | 4.974252947151467  | 5.324848229691634  |
| 50 | 0  | 0.1  | 5.112052900496995  | 5.480003384304311  |
| 50 | 0  | 0.05 | 5.271529818836897  | 5.659565607087776  |
| 50 | 2  | 0.5  | 5.030228392847363  | 5.387873497266893  |
| 50 | 2  | 0.1  | 5.120321860165079  | 5.489313777266278  |
| 50 | 2  | 0.05 | 5.3096764756303445 | 5.702516640735105  |
| 50 | 5  | 0.5  | 5.012751014095544  | 5.368194931805675  |
| 50 | 5  | 0.1  | 5.129988012287022  | 5.5001973319452055 |
| 50 | 5  | 0.05 | 5.2959524837456735 | 5.687064182072583  |

Thus, for `hidden layer dimension = 25`, `lookback = 5` and `learning rate` = 0.5, 
we have the lowest cross-entropy on the first 1000 sentences of the development set. 

## Question 2b

Training model on `25000` sentences of training set:
```
$> python rnn.py train-lm data 25 5 0.5 25000 1000
```

```
Retained 2000 words from 9954 (88.81% of all tokens)


Training model for 10 epochs
training set: 25000 sentences (batch size 100)
Optimizing loss on 1000 sentences
Vocab size: 2000
Hidden units: 25
Steps for back propagation: 5
Initial learning rate set to 0.5, annealing set to 5

calculating initial mean loss on dev set: 7.798662515757492

epoch 1, learning rate 0.5000   instance 25000  epoch done in 1090.18 seconds   new loss: 4.794482577289604
epoch 2, learning rate 0.4167   instance 25000  epoch done in 1076.89 seconds   new loss: 4.729572300411105
epoch 3, learning rate 0.3571   instance 25000  epoch done in 1046.31 seconds   new loss: 4.639506451586233
epoch 4, learning rate 0.3125   instance 25000  epoch done in 1068.40 seconds   new loss: 4.603703109568141
epoch 5, learning rate 0.2778   instance 25000  epoch done in 1095.79 seconds   new loss: 4.574999420256336
epoch 6, learning rate 0.2500   instance 25000  epoch done in 1059.30 seconds   new loss: 4.524480540439848
epoch 7, learning rate 0.2273   instance 25000  epoch done in 1057.39 seconds   new loss: 4.508409447677186
epoch 8, learning rate 0.2083   instance 25000  epoch done in 991.20 seconds    new loss: 4.491795418798984
epoch 9, learning rate 0.1923   instance 25000  epoch done in 1034.36 seconds   new loss: 4.487813217153281
epoch 10, learning rate 0.1786  instance 25000  epoch done in 1023.19 seconds   new loss: 4.458638446567996

training finished after reaching maximum of 10 epochs
best observed loss was 4.458638446567996, at epoch 10
setting U, V, W to matrices from best epoch
Unadjusted: 86.370
Adjusted for missing vocab: 114.927
```

Evaluating model on full test set:
```
$> python rnn.py predict-q2 data models
```

```
Mean loss: 4.665231887752031
Unadjusted perplexity: 106.190
Adjusted perplexity: 145.025
```

## Question 3a
Testing implementation
```
$> python rnn.py train-np data 25 5 0.5
```

```
Retained 2000 words from 9954 (88.81% of all tokens)


Training model for 1 epochs
training set: 1000 sentences (batch size 100)
Optimizing loss on 1000 sentences
Vocab size: 2000
Hidden units: 25
Steps for back propagation: 5
Initial learning rate set to 0.5, annealing set to 5

calculating initial mean loss on dev set: 7.076089209069355
calculating initial acc on dev set: 0.0

epoch 1, learning rate 0.5000   instance 1000   epoch done in 19.49 seconds     new loss: 0.7753777760495294    new acc: 0.481

training finished after reaching maximum of 1 epochs
best observed loss was 0.7753777760495294, acc 0.481, at epoch 1
setting U, V, W to matrices from best epoch
Accuracy: 0.481
```

## Question 4b

We think that the number prediction problem is a good proxy to investigate the power of the model to learn long-range dependencies.

We want to test the following hypothesis:
* Does the performance of the models degrade as the distance between the verb and subject increases?
* Does LSTM perform better than our vanilla RNN for longer V - Subj distances?

* Can we measure which parts of the input are more relevant for the number agreement decision?
    - Does/Would an attention model recognise/capture which words/word indices are more important for number agreement?
    
We designed two experiments to answer these questions:
* Quantitative....
* Quanlitative attention...

### Log for LSTM with Attention
```
Train on 22500 samples, validate on 2500 samples
Epoch 1/10
22500/22500 [==============================] - 206s 9ms/step - loss: 0.3267 - acc: 0.8635 - val_loss: 0.2190 - val_acc: 0.9128
Epoch 2/10
22500/22500 [==============================] - 206s 9ms/step - loss: 0.2046 - acc: 0.9122 - val_loss: 0.1794 - val_acc: 0.9220
Epoch 3/10
22500/22500 [==============================] - 205s 9ms/step - loss: 0.1745 - acc: 0.9254 - val_loss: 0.1943 - val_acc: 0.9176
Epoch 4/10
22500/22500 [==============================] - 207s 9ms/step - loss: 0.1576 - acc: 0.9319 - val_loss: 0.1879 - val_acc: 0.9232
Epoch 5/10
22500/22500 [==============================] - 207s 9ms/step - loss: 0.1516 - acc: 0.9342 - val_loss: 0.1657 - val_acc: 0.9328
Epoch 6/10
22500/22500 [==============================] - 203s 9ms/step - loss: 0.1371 - acc: 0.9393 - val_loss: 0.1796 - val_acc: 0.9324
Epoch 7/10
22500/22500 [==============================] - 202s 9ms/step - loss: 0.1312 - acc: 0.9444 - val_loss: 0.1924 - val_acc: 0.9284
Epoch 8/10
22500/22500 [==============================] - 202s 9ms/step - loss: 0.1262 - acc: 0.9460 - val_loss: 0.1971 - val_acc: 0.9256
```
