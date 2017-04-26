NMT-Keras
=========

Neural Machine Translation with Keras (+ Theano backend).

.. image:: ../../examples/documentation/attention_nmt_model.png
   :scale: 80 %
   :alt: alternate text
   :align: left

Features
********

 * Attention model over the input sequence of annotations.
 * Peeked decoder: The previously generated word is an input of the current timestep.
 * Beam search decoding.
 * Ensemble decoding.
 * Support for GRU/LSTM networks.
 * Multilayered residual GRU/LSTM networks.
 * N-best list generation (as byproduct of the beam search process).
 * Unknown words replacement.
 * Use of pretrained (Glove_ or Word2Vec_) word embedding vectors.
 * MLPs for initializing the RNN hidden and memory state.
 * Spearmint_ wrapper for hyperparameter optimization.

.. _Spearmint: https://github.com/HIPS/Spearmint
.. _Glove: http://nlp.stanford.edu/projects/glove/
.. _Word2Vec: https://code.google.com/archive/p/word2vec/

Guide
=====
.. toctree::
   :maxdepth: 3

   requirements
   usage
   resources
   tutorial
   modules
   help


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
