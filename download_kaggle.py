import kagglehub
from pathlib import Path

# Download latest version
path = kagglehub.dataset_download("rtatman/188-million-us-wildfires")
print("Path to dataset files:", path)

# Optional: list CSV files
p = Path(path)
csvs = list(p.rglob("*.csv"))
print(f"Found {len(csvs)} CSV file(s):")
for f in csvs:
    print("-", f)
