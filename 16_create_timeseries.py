from msvcrt import LK_LOCK
import os
import sys
import pandas as pd
import numpy as np
from cdf_auth_interactive import get_client
from cognite.client.data_classes import TimeSeries


def create_ts(csv_file):
    # read table info from the first row of CSV(UTF-8 encoded)
    table_info = pd.read_csv(csv_file, nrows=1, encoding='utf-8')
    # print(table_info)
    for index, row in table_info.iterrows():
        print(f"Table name        {row['テーブル名']}")
        print(f"Table description {row['テーブル名称']}")
        table_name = row['テーブル名']
        table_description = row['テーブル名称']

    # read column info from CSV(UTF-8 encoded) to pandas dataframe
    df = pd.read_csv(csv_file, skiprows=NUM_SKIP_ROWS, encoding='utf-8')

    for index, row in df.iterrows():
        if row['タイムスタンプ'] == '〇':   # recommended to use true/false instead of 〇
            continue
        print(f"----- Column #{index}")
        print(f"external_id = {row['external_id']}")
        print(f"name        = {row['name']}")
        # print(f"is_string   = {row['is_string'].lower()}")
        print(f"is_string   = {row['is_string'].lower()}")

        # create Timeseries if not exists
        ts = client.time_series.retrieve(external_id=row['external_id'])
        if ts is None:
            res = client.time_series.create(
                TimeSeries(
                    name=row['name'],
                    external_id=row['external_id'],
                    is_string=row['is_string'],
                    # unit='m',
                    # description=description,
                    data_set_id=data_set_id,
                    metadata={
                        'table_name': table_name,
                        'table_description': table_description,
                    }
                ) # type: ignore
            )

#-------------------------------------------------------------------
NUM_SKIP_ROWS = 4   # No. of header rows to skip
if len(sys.argv) > 1:
    csv_file = sys.argv[1]
else:
    print(f"\nUsage: python3 {os.path.basename(sys.argv[0])} <csv_file>\n")
    exit(1)

# connect to CDF
client = get_client()
data_set = client.data_sets.retrieve(external_id=os.environ['COGNITE_DATA_SET_XID'])
data_set_id = data_set.id
print(f"Data set name: {data_set.name}")
print(f"Data set description: {data_set.description}")

create_ts(csv_file)
