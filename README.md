# University of Edinburgh: Natural Language Understanding coursework (spring 2018)

## Authors

In random order:
 - Marcio Fonseca
 - Laszlo Treszkai

## Coursework descriptions

In `nlu-coursework.pdf`. 

In a nutshell, the task was to write some required functions for training an RNN using NumPy,
including forward propagation of values and backpropagation of derivatives.

Actually, we trained two separate RNNs:
 - one for language modeling,
 - another for predicting the whether the subject is plural or not. Example:
    - "The key <> on the table ." -> singular (0);
    - "The keys <> on the table ." -> plural (1). 

Much of the learning machinery was provided.
Our contribution is writing the following methods of the `RNN` class in `code/rnn.py`:
- `predict()`, to predict an output sequence y for a given input sequence x
- `acc_deltas()`, to accumulate the updates for U, V, W matrices of the RNN
- `acc_deltas_np()`, likewise, for the number prediction (NP) model
- `acc_deltas_bptt()`, to perform the backpropagation correctly (including the partial derivatives through time)
- `acc_deltas_bptt_np()`, likewise, for the NP model;
- `compute_loss()`, to compute the loss for a given prediction and target;
- `compute_loss_np()`, likewise, for the NP model;
- `compute_acc_np()`, to compute the accuracy of the NP model;
- `compare_num_pred()`, without description;
- `compute_mean_loss()`, to calculate the mean loss for the whole dataset.

We also added code for the hyperparameter grid search, while preserving the original argument order of the module. 

## Coursework report

A report of our work is given in `report.pdf`.
Of special interest is our answer to the last exercise (pp. 4–5),
which was a free-from question, where we performed two experiments:
 - How well does an RNN vs. an LSTM perform on the number prediction task, as a function of the distance between the noun and the verb? (Main contributor: Laszlo Treszkai.)
 - How much does the use of attention increase the accuracy on the number prediction task, and how are the attention weights distributed? (Main contributor: Marcio Fonseca.)

## Requirements

- numpy
- gensim
- pandas

## Usage

For learning a language model,
run `python rnn.py train-lm <hdim> <lookback> <lr>`,
where
 - `<hdim>` = number of hidden dimensions,
 - `<lookback>` = number of time steps to backpropagate the derivatives through time (BPTT),
 - `<lr>` = learning rate.   
 
Or `python rnn.py train-lm foo bar baz true`
which performs a grid search on the product space of
 - `hdim` ∈ {25, 50, 100},
 - `lookback` ∈ {0, 2, 5},
 - `lr` ∈ {0.1, 0.5, 0.1, 0.05}

(The arguments `foo`, `bar`, `baz` are ignored in this case.)

## Testing

Tests were provided in `code/test.py`, which can be executed by `python code/test.py`.

## Disclaimer

This repository is for informational purposes only, without warranty.

It does not accurately reflect the present knowledge or coding skills of the authors.

The coursework report was selected as exemplary (as well as the report of one other group).
