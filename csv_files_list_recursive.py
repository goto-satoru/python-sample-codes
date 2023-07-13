import os

def get_csv_file_paths(directory):
    csv_file_paths = []

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".csv"):
                csv_file_paths.append(os.path.join(root, file))

    return csv_file_paths

# Example usage
directory = "./csv"
csv_paths = get_csv_file_paths(directory)

# Print the paths of CSV files
for path in csv_paths:
    print(path)
    # upload CSV data into CDF Timeseries/Datapoints
