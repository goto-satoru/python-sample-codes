import arrow
import pandas as pd
from cdf_auth_interactive import get_client
from cognite.client.data_classes import TimeSeries

NUM_COLUMNS = 10_000
NUM_ROWS = 60
CSV_FILENAME = "data10Kx60.csv"
# NUM_COLUMNS = 10
# NUM_ROWS = 10
# CSV_FILENAME = "data10x10.csv"

client = get_client()

data_set = client.data_sets.retrieve(external_id='chiba-sample')
# print(data_set.id, data_set.name)

# read CSV file, put into pandas dataframe
df = pd.read_csv(CSV_FILENAME)
df.set_index("timestamp", inplace=True)
print(df)

# build datapoints list for insert_multiple
datapoints = []
for i in range(NUM_COLUMNS):
    column_name = f"col{i:04d}"
    # if i % 1000 == 0:
    # print(i, name)
    # print(i, df[name])
    datapoints.append({
        "externalId": f"schema1.table1.{column_name}",
        "datapoints": [(int(arrow.get(ts).timestamp()*1000), v) for ts, v in df[column_name].items()]
    })

start = arrow.now()
print(start)
client.time_series.data.insert_multiple(datapoints)
end = arrow.now()
print(f"Inserting {NUM_ROWS} rows with 10,000 columns and 'insert_multiple' took {end - start} sec.")
