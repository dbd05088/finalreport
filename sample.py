import datasets
import pandas as pd
import pyarrow as pa
import pyarrow.dataset as ds
from datasets import Dataset


train_df = pd.DataFrame({
     "label" : [1, 2, 3],
     "text" : ["apple", "pear", "strawberry"]
})

test_df = pd.DataFrame({
     "label" : [2, 2, 1],
     "text" : ["banana", "pear", "apple"]
})

train_dataset = dataset = ds.dataset(pa.Table.from_pandas(train_df).to_batches())
test_dataset = dataset = ds.dataset(pa.Table.from_pandas(test_df).to_batches())
my_dataset_dict = datasets.DatasetDict({"train":train_dataset,"test":test_dataset})