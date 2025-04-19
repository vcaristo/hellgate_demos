#OSM_Download

In this example, we download GIS features (parks, schools, and sports fields) from OpenStreetMaps (OSM) for the entire continental United States (CONUS). I use a single node to download data for 3,223 counties in series. In this case, the HPC was utilized msotly for its robustness and storage capacity. The entire operation took 7 hours and 20 minutes to complete. 

## Running this code
1. First, open a shell on login node. 
2. From the command line, navigate to to folder /hellgate_demos/conda_examples/osm_download_1-node. 
3. Create a new conda environment from the environment from the **environment.yml** file: `conda env create -f environment.yml'.  

This creates an environment called 'us_osm_env', which has all the required packages for running the python script. You can check this by executing `conda env list` from your command line. 

4. Modify the sbatch script, as necessary (at a minimum, perhaps add your own email for alterts)
5. Execute the SBATCH script: `sbatch osm_download_batch.sh`. Note, this is a relative path that assumes your cwd is the same folder as the script. If this isn't the case, navigate to this folder, or replace `osm_download_batch.sh` with the full path to the script (relative or absolute) 