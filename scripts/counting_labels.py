from collections import defaultdict
from tqdm.auto import tqdm

def count_labels(dataset):
    label_counter = defaultdict(int)
    for _, label in tqdm(dataset, desc="Counting labels"):
        label_counter[label] += 1
    return label_counter
