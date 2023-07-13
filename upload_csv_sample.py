import pandas as pd
import numpy as np
import datetime
from cdf_auth import get_client
from cognite.client.data_classes import TimeSeries
import time

NUM_COLUMNS = 10

# create sample CSV data
column_names = [f"column {i:04d}" for i in range(NUM_COLUMNS)]
l = 60
values = np.random.rand(l, NUM_COLUMNS)
with open("data.csv", "w+") as f:
    f.write(",".join(column_names) + "\n")
    for row in values:
        f.write(",".join(map(str, row)) + "\n")

client = get_client()

data_set = client.data_sets.retrieve(external_id='chiba-sample')
print(data_set.id, data_set.name)

# read CSV file into pandas dataframe
df = pd.read_csv("data.csv")

df["timestamp"] = [pd.Timestamp(datetime.datetime.now().timestamp() - 60*i, unit = "s") for i in range(l)]
print(df["timestamp"])
df.set_index("timestamp", inplace=True)
print(df)

# build datapoints for insert_multiple
datapoints = []
count = 0
for column_name in column_names:
    count += 1
    name = column_name
    # print name every 1000 columns
    if count % 1000 == 0:
        print(name)
    # create Timeseries if not exists
    # if ts := client.time_series.retrieve(external_id=name) is None:
    #     client.time_series.create(TimeSeries(name=name, external_id=name, unit='kg', description='10K columns insert test', data_set_id=data_set.id))
    datapoints.append({"externalId": name, "datapoints": [(int(ts.timestamp()*1000), v) for ts,v in df[column_name].items()]})

start = time.time()
client.time_series.data.insert_dataframe(df, external_id_headers=True)
end = time.time()
print(f"Inserting {l} rows with 10,000 columns and 'insert_dataframe' took {end - start} sec.")

start = time.time()
client.time_series.data.insert_multiple(datapoints)
end = time.time()
print(f"Inserting {l} rows with 10,000 columns and 'insert_multiple' took {end - start} sec.")
