import geopandas as gpd
from pathlib import Path
import pandas as pd
import os

# apptainer path 
base = Path('/mnt/project')
data_path = base / "data"

# setup output file
layers = ['parks', 'pitches', 'sports_centres', 'schools']
result = pd.DataFrame(columns = ['state', 'county'] + layers)

# list all the state folders

states = [f.name for f in data_path.iterdir() if f.is_dir()]

# there is only one state in the data folder 
for state in states:
    state_path = data_path / state

    files = [f for f in state_path.iterdir() if f.is_file()] # full file paths

    for county_gpk_path in files:
        county_name = county_gpk_path.name.split(".gpkg")[0]
        
        # initial county data record
        county_data = {'state':state, 'county':county_name}
        
        for layer in layers:
            try:
                gdf = gpd.read_file(county_gpk_path, layer=layer)
                county_data[layer] = len(gdf)
            except:         # in case layer doesn't exist
                county_data[layer] = 0

        # add county data to result
        result.loc[len(result)] = county_data

os.makedirs(base / "output", exist_ok=True)
result.to_csv(base / "output" / "features_count.csv")