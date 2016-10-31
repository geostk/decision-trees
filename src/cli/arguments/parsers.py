import argparse
import ast
from core.dataset.constants import *
from .constants import *

# helping methods
def evalTF(string):
	return ast.literal_eval(string.title())

# Default parser
DEFAULT_PARSER = argparse.ArgumentParser(
	# prog = 'decision-tree.py'
	# usage = (generated by default)
	description = """Given a dataset either from local or remote origins,
	analyzes the data to generate a decision tree that will be able to classify
	the data according to the attribute specified and finally validate the
	accuracy against a training set, or trying to classify random examples""",
	epilog = "<> with ♥ in ETSE UAB by ccebrecos, davidlj95 & joel.sanz",
	add_help = True,
	allow_abbrev = True
)
DEFAULT_PARSER.add_argument("-v","--version",
	action="version",
	version="Decision-Tree classifier 0.2 (alpha)")
# Data related
DEFAULT_PARSER.add_argument("-d","--dataset",
	action="store",
	nargs="?",
	help="""specifies the dataset to load (default is %s). Will try to load inside the folder specified, that is a subfolder of %s, the first file ended with .%s for a training set, the first file ended with .%s for a validation set, and the first file ended with .%s for a feature meanings file. """%(DATASET_DEFAULT, DATASET_PATH, DATASET_TRAINING_EXT, DATASET_VALIDATION_EXT, DATASET_FEATURES_EXT),
	type=str,
	choices=DATASETS,
	default=DATASET_DEFAULT,
)
DEFAULT_PARSER.add_argument("--show-dataset",
	metavar="true|false",
	action="store",
	nargs="?",
	help="""enables or disables printing dataset information (%s
	by default)"""%("enabled" if SHOW_DATASET_DEFAULT else "disabled"),
	type=evalTF,
	const=True,
	default=SHOW_DATASET_DEFAULT
)
DEFAULT_PARSER.add_argument("--show-tree",
	metavar="true|false",
	action="store",
	nargs="?",
	help="""enables or disables printing the decision tree to screen (%s
	by default)"""%("enabled" if SHOW_TREE_DEFAULT else "disabled"),
	type=evalTF,
	const=True,
	default=SHOW_TREE_DEFAULT
)
DEFAULT_PARSER.add_argument("-a","--algorithm",
	action="store",
	help="""sets the algorithm to use to classify the training set into a
	decision tree. Default is %s"""%ALGORITHM_DEFAULT,
	type=str,
	choices=ALGORITHMS,
	default=ALGORITHM_DEFAULT
)
DEFAULT_PARSER.add_argument("-c","--classifier",
	metavar="variable",
	action="store",
	help="""sets the classifier variable to use to generate the decision tree.
	It has to be a column from the dataset, either as a number or if the dataset has the feature names, by its name. By default, we use the column %d
	of the dataset)"""%TARGET_DEFAULT,
	type=str,
	default=TARGET_DEFAULT
)
DEFAULT_PARSER.add_argument("-s","--splitter",
	action="store",
	help="""sets the splitting meta-algorithm to use to generate the training sets and validation sets from the dataset if in the specified dataset no validation set is present. Default is %s"""%(SPLITTER_DEFAULT),
	type=str,
	choices=SPLITTERS,
	default=SPLITTER_DEFAULT
)
DEFAULT_PARSER.add_argument("-p","--percent",
	metavar="%",
	action="store",
	help="""when using holdout splitter, sets the percentage (expressed between 0 and 1) that sets how many items will be sent to the training set from the whole dataset if no validation set is available for the dataset specified. Default is %f"""%
		(HOLDOUT_PERCENT_DEFAULT),
	type=float,
	default=HOLDOUT_PERCENT_DEFAULT
)
DEFAULT_PARSER.add_argument("-k","--cross-validation-k",
	metavar="groups",
	action="store",
	help="""when using cross-validation splitter, sets the k-number of groups to divide the dataset into in order to in each k-iteration, consider the k-group as validation set and the other groups as training sets. When k=number of samples, the cross-validation is switched into leave1out. Value has to be between %d <= k <= number of samples of the dataset. Default is %s"""%(CROSSVALID_K_MIN, CROSSVALID_K),
	type=int,
	default=CROSSVALID_K
)
DEFAULT_PARSER.add_argument("-t",
	action="count",
	help="""records the algorithm's computation time and shows them. You can
	add levels of timings by specifying repeating argument. Default timing
	level is %d"""%TIMERS_DEFAULT,
	default = TIMERS_DEFAULT
)
DEFAULT_PARSER.add_argument("-l","--log-level",
	metavar="level",
	action="store",
	help="""specifies the level of events to log. events upper from that level
	will be displayed. Default is %s"""%(LOG_DEFAULT),
	type=str,
	choices=LOGS,
	default=LOG_DEFAULT
)
