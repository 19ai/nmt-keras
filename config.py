
def load_parameters():
    '''
        Loads the defined parameters
    '''

    # Input data params
    DATASET_NAME = 'turista'
    FILL = 'end'                                  # whether we fill the 'end' or the 'start' of the sentence with 0s
    SRC_LAN = 'es'                                # Language of the outputs
    TRG_LAN = 'en'                                # Language of the outputs

    DATA_ROOT_PATH = '/media/HDD_2TB/DATASETS/%s/' % DATASET_NAME

    # SRC_LAN or TRG_LAN will be added to the file names
    TEXT_FILES = {'train': 'DATA/training.',  'val': 'DATA/dev.', 'test': 'DATA/test.'}

    # Dataset parameters
    INPUTS_IDS_DATASET = ['source_text', 'state_below']     # Corresponding inputs of the dataset
    OUTPUTS_IDS_DATASET = ['target_text']                   # Corresponding outputs of the dataset
    INPUTS_IDS_MODEL = ['source_text', 'state_below']       # Corresponding inputs of the built model
    OUTPUTS_IDS_MODEL = ['target_text']                     # Corresponding outputs of the built model

    # Evaluation params
    METRICS = ['coco']  # Metric used for evaluating model after each epoch (leave empty if only prediction is required)
    EVAL_ON_SETS = ['val']                        # Possible values: 'train', 'val' and 'test' (external evaluator)
    EVAL_ON_SETS_KERAS = []                       # Possible values: 'train', 'val' and 'test' (Keras' evaluator)
    START_EVAL_ON_EPOCH = 5                       # First epoch where the model will be evaluated
    EVAL_EACH_EPOCHS = True                       # Select whether evaluate between N epochs or N updates
    EVAL_EACH = 5                                 # Sets the evaluation frequency (epochs or updates)

    # Search parameters
    SAMPLING = 'max_likelihood'                   # Possible values: multinomial or max_likelihood (recommended)
    TEMPERATURE = 1                               # Multinomial sampling parameter
    BEAM_SEARCH = True                            # Switches on-off the beam search procedure
    BEAM_SIZE = 12                                # Beam size (in case of BEAM_SEARCH == True)
    NORMALIZE_SAMPLING = True                     # Normalize hypotheses scores according to their length
    ALPHA_FACTOR = .6                             # Normalization according to length**ALPHA_FACTOR (https://arxiv.org/pdf/1609.08144v1.pdf)

    # Sampling params: Show some samples during training
    SAMPLE_ON_SETS = ['train', 'val']             # Possible values: 'train', 'val' and 'test'
    N_SAMPLES = 5                                 # Number of samples generated
    START_SAMPLING_ON_EPOCH = 1                   # First epoch where the model will be evaluated
    SAMPLE_EACH_UPDATES = 1000                    # Sampling frequency

    #TODO: WIP! Other subword methods?
    POS_UNK = False
    HEURISTIC = 1

    # Word representation params
    TOKENIZATION_METHOD = 'tokenize_none'    # Select which tokenization we'll apply

    # Input text parameters
    INPUT_VOCABULARY_SIZE = 0  # Size of the input vocabulary. Set to 0 for using all, otherwise will be truncated to these most frequent words.
    MIN_OCCURRENCES_VOCAB = 0  # Minimum number of occurrences allowed for the words in the vocabulay. Set to 0 for using them all.
    MAX_INPUT_TEXT_LEN = 50    # Maximum length of the input sequence

    # Output text parameters
    OUTPUT_VOCABULARY_SIZE = 0      # vocabulary of output text. Set to 0 for autosetting, otherwise will be truncated
    MAX_OUTPUT_TEXT_LEN = 50        # set to 0 if we want to use the whole answer as a single class
    MAX_OUTPUT_TEXT_LEN_TEST = 100  # Maximum length of the output sequence at test time

    # Optimizer parameters (see model.compile() function)
    LOSS = 'categorical_crossentropy'

    # Not used!
    ##########
    LR_DECAY = 20  # number of minimum number of epochs before the next LR decay
    LR_GAMMA = 0.8  # multiplier used for decreasing the LR
    ##########

    OPTIMIZER = 'Adam'      # Optimizer
    LR = 0.001              # (recommended values - Adam 0.001 - Adadelta 1.0
    WEIGHT_DECAY = 1e-4     # L2 regularization
    CLIP_C = 1.             # During training, clip gradients to this norm
    SAMPLE_WEIGHTS = True   # Select whether we use a weights matrix (mask) for the data outputs

    # Training parameters
    MAX_EPOCH = 500          # Stop when computed this number of epochs
    BATCH_SIZE = 50

    HOMOGENEOUS_BATCHES = False # Use batches with homogeneous output lengths for every minibatch (Dangerous)
    PARALLEL_LOADERS = 8        # Parallel data batch loaders
    EPOCHS_FOR_SAVE = 1         # Number of epochs between model saves
    WRITE_VALID_SAMPLES = True  # Write valid samples in file

    # Early stop parameters
    EARLY_STOP = True           # Turns on/off the early stop protocol
    PATIENCE = 2000             # We'll stop if the val STOP_METRIC does not improve after this number of evaluations
    STOP_METRIC = 'Bleu_4'      # Metric for the stop


    # Model parameters
    MODEL_TYPE = 'GroundHogModel'
    CLASSIFIER_ACTIVATION = 'softmax'

    # Input text parameters
    GLOVE_VECTORS = None              # Path to pretrained vectors. Set to None if you don't want to use pretrained vectors.
    GLOVE_VECTORS_TRAINABLE = True    # Finetune or not the word embedding vectors.
    TEXT_EMBEDDING_HIDDEN_SIZE = 354  # When using pretrained word embeddings, this parameter must match with the word embeddings size

    # Encoder layer dimensions
    ENCODER_HIDDEN_SIZE = 289         # For models with RNN encoder
    BIDIRECTIONAL_ENCODER = True      # Use bidirectional encoder
    N_LAYERS_DECODER = 1              # Stack this number of encoding layers

    # Decoder layer dimensions
    DECODER_HIDDEN_SIZE = 289         # For models with RNN decoder
    N_LAYERS_DECODER = 1              # Stack this number of deenoding layers

    # additional Fully-Connected layers's sizes applied before softmax.
    # Here we should specify the activation function and the output dimension
    # (e.g DEEP_OUTPUT_LAYERS = [('tanh', 600), ('relu',400), ('relu':200)])
    DEEP_OUTPUT_LAYERS = [('maxout', TEXT_EMBEDDING_HIDDEN_SIZE/2)]

    INIT_LAYERS = ['tanh']      # FC layers for initializing the first RNN state
                                # Here we should only specify the activation function of each layer (as they have a potentially fixed size)
                                # (e.g INIT_LAYERS = ['tanh', 'relu'])

    # Regularizers
    USE_DROPOUT = False                 # Use dropout
    DROPOUT_P = 0.5                     # Percentage of units to drop

    USE_NOISE = False                    # Use gaussian noise during training
    NOISE_AMOUNT = 0.01                 # Amount of noise

    USE_BATCH_NORMALIZATION = True      # If True it is recommended to deactivate Dropout
    BATCH_NORMALIZATION_MODE = 1        # See documentation in Keras' BN

    USE_PRELU = False                   # use PReLU activations
    USE_L2 = False                      # L2 normalization on the features

    # Results plot and models storing parameters
    EXTRA_NAME = '' # This will be appended to the end of the model name
    MODEL_NAME = DATASET_NAME + '_' + MODEL_TYPE + '_txtemb_' + str(TEXT_EMBEDDING_HIDDEN_SIZE) + \
                  '_blstm_' + str(BIDIRECTIONAL_ENCODER) +\
                 '_' + str(ENCODER_HIDDEN_SIZE) + \
                 '_lstm_' + str(DECODER_HIDDEN_SIZE) + \
                 '_deepout_' + '_'.join([layer[0] for layer in DEEP_OUTPUT_LAYERS]) + \
                 '_' + OPTIMIZER

    MODEL_NAME += EXTRA_NAME

    STORE_PATH = 'trained_models/' + MODEL_NAME  + '/' # Models and evaluation results will be stored here
    DATASET_STORE_PATH = 'datasets/'                   # Dataset instance will be stored here

    SAMPLING_SAVE_MODE = 'list'                        # 'list' or 'vqa'
    VERBOSE = 1                                        # Verbosity level
    RELOAD = 0                                         # If 0 start training from scratch, otherwise the model
                                                       # Saved on epoch 'RELOAD' will be used
    REBUILD_DATASET = True                             # Build again or use stored instance
    MODE = 'training'                                  # 'training' or 'sampling' (if 'sampling' then RELOAD must
                                                       # be greater than 0 and EVAL_ON_SETS will be used)

    # Extra parameters for special trainings
    TRAIN_ON_TRAINVAL = False  # train the model on both training and validation sets combined
    FORCE_RELOAD_VOCABULARY = False  # force building a new vocabulary from the training samples applicable if RELOAD > 1

    # ============================================
    parameters = locals().copy()
    return parameters
