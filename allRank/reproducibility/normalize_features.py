import os
from argparse import ArgumentParser, Namespace

import numpy as np
from sklearn.datasets import load_svmlight_file, dump_svmlight_file


def parse_args() -> Namespace:
    parser = ArgumentParser("Normalize features script")

    parser.add_argument("--ds_path", help="location of the dataset", required=True, type=str)

    return parser.parse_args()


args = parse_args()

x_train, y_train, query_ids_train = load_svmlight_file(os.path.join(args.ds_path, "train.txt"), query_id=True)
x_test, y_test, query_ids_test = load_svmlight_file(os.path.join(args.ds_path, "test.txt"), query_id=True)
x_vali, y_vali, query_ids_vali = load_svmlight_file(os.path.join(args.ds_path, "vali.txt"), query_id=True)

ds_normalized_path = "{}_no_normalized".format(args.ds_path)
os.makedirs(ds_normalized_path, exist_ok=True)

train_normalized_path = os.path.join(ds_normalized_path, "train.txt")
with open(train_normalized_path, "w"):
    dump_svmlight_file(x_train, y_train, train_normalized_path, query_id=query_ids_train)

test_normalized_path = os.path.join(ds_normalized_path, "test.txt")
with open(test_normalized_path, "w"):
    dump_svmlight_file(x_test, y_test, test_normalized_path, query_id=query_ids_test)

vali_normalized_path = os.path.join(ds_normalized_path, "vali.txt")
with open(vali_normalized_path, "w"):
    dump_svmlight_file(x_vali, y_vali, vali_normalized_path, query_id=query_ids_vali)

print("Dataset with no normalization saved here: {}.".format(ds_normalized_path))

