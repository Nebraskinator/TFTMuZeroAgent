import numpy as np

# IMPORTANT: Change this value to the number of cpu cores you want to use (recommended 80% of cpu)
NUM_CPUS = 28

# AI RELATED VALUES START HERE

#### MODEL SET UP ####
HIDDEN_STATE_SIZE = 512
NUM_RNN_CELLS = 2
LSTM_SIZE = int(HIDDEN_STATE_SIZE / NUM_RNN_CELLS)
CONV_FILTERS = HIDDEN_STATE_SIZE / 4
RNN_SIZES = [LSTM_SIZE] * NUM_RNN_CELLS
LAYER_HIDDEN_SIZE = HIDDEN_STATE_SIZE * 2
ROOT_DIRICHLET_ALPHA = 0.5
ROOT_EXPLORATION_FRACTION = 0.25
MINIMUM_REWARD = -300.0
MAXIMUM_REWARD = 300.0
PB_C_BASE = 19652
PB_C_INIT = 1.25
DISCOUNT = 0.997
TRAINING_STEPS = 1e10
OBSERVATION_SIZE = 8667
OBSERVATION_TIME_STEPS = 5
OBSERVATION_TIME_STEP_INTERVAL = 4
INPUT_TENSOR_SHAPE = np.array([OBSERVATION_SIZE])
ACTION_ENCODING_SIZE = 1045
ACTION_CONCAT_SIZE = 81
ACTION_DIM = [6, 38, 10]
# ACTION_DIM = 10
ENCODER_NUM_STEPS = 601
SELECTED_SAMPLES = True
MAX_GRAD_NORM = 5

# Still used in MuZero_torch_agent.py
HEAD_HIDDEN_SIZE = 1024
N_HEAD_HIDDEN_LAYERS = 1

### TIME RELATED VALUES ###
ACTIONS_PER_TURN = 10
CONCURRENT_GAMES = 24
NUM_PLAYERS = 8 
NUM_SAMPLES = 300
NUM_SIMULATIONS = 400
SAMPLES_PER_PLAYER = 128  # Normal is 128
UNROLL_STEPS = 5

### TRAINING ###
BATCH_SIZE = 256
INIT_LEARNING_RATE = 0.01
LEARNING_RATE_DECAY = int(350e3)
LR_DECAY_FUNCTION = 0.1
WEIGHT_DECAY = 1e-5
REWARD_LOSS_SCALING = 1
POLICY_LOSS_SCALING = 1
# Putting this here so that we don't scale the policy by a multiple of 5
# Because we calculate the loss for each of the 5 dimensions.
# I'll add a mathematical way of generating these numbers later.
DEBUG = True

#### TESTING ####
RUN_UNIT_TEST = False
RUN_PLAYER_TESTS = False
RUN_MINION_TESTS = False
RUN_DROP_TESTS = False
RUN_MCTS_TESTS = True
RUN_MAPPING_TESTS = False
LOG_COMBAT = False
