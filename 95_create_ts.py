import os
import pandas as pd
import numpy as np
from cdf_auth_interactive import get_client
from cognite.client.data_classes import TimeSeries

# CSV_FILENAME = "data10x10.csv"
CSV_FILENAME = "data10Kx60.csv"

client = get_client()
data_set = client.data_sets.retrieve(external_id=os.environ['COGNITE_DATA_SET_XID'])
data_set_id = data_set.id

# read data from CSV to pandas dataframe
df = pd.read_csv(CSV_FILENAME)
df.set_index("timestamp", inplace=True)
print(df)

# print(df.columns)
count = 0
for column in df.columns:
    count += 1
    print(count, column)
    # if column type is string, set is_string to True
    is_string = False
    name = f"schema1.table1.{column}"
    description = f"Timeseries test"
    # create Timeseries if not exists
    ts = client.time_series.retrieve(external_id=name)
    if ts is None:
        res  = client.time_series.create(
            TimeSeries(
                name=name,
                external_id=name,
                unit='m',
                is_string=is_string,
                description=description,
                data_set_id=data_set_id,
                metadata={
                    'schema': 'schema1',
                    'table': 'table1'
                }
            ) # type: ignore
        )
