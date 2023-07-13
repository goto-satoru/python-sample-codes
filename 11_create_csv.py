import pandas as pd
import numpy as np

NUM_COLUMNS = 10_000
NUM_ROWS = 60
# NUM_COLUMNS = 10
# NUM_ROWS = 10
CSV_FILENAME = "data10Kx60.csv"

idx = pd.date_range(start="2023-07-06 00:00:00+09:00", periods=NUM_ROWS, freq="1min")

# create sample CSV data
column_names = [f"col{i:04d}" for i in range(NUM_COLUMNS)]
values = np.random.rand(NUM_ROWS, NUM_COLUMNS)
with open(CSV_FILENAME, "w+") as f:
    f.write('timestamp,' + ",".join(column_names) + "\n")
    count = 0
    for row in values:
        f.write(str(idx[count]) + ',' + ",".join(map(str, row)) + "\n")
        count += 1
