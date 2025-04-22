# Count Features

In this example, I count the number of features (parks, schools, sports fields) that are present in a set previously downloaded GIS files (see 'osm_download_1-node'). There is 1 GIS file for each of the 3,223 counties in the continental US (CONUS). 

While it's quite a bit of data, this operation is well within the reasonable capabilities of a personal computer. The HPC - and apptainer - was utilized mostly for learning purposes. 

## Running this code

### 1) Build the container image. 
- See `Build_Apptainer_Image.md`

### 2) Write/edit your sbatch script to run your python script inside the container.
- First, setup your sbatch parameters to suit your needs (memory requirements, email notices, etc.)
- Since all the dependencies for your script are "baked" into the container, there is no environment loading (ie, conda) with this approach. 
- The "meat" of your sbatch script is running your container. This container is setup to take a python script as a paramater, and to execute the script inside the container. With this approach (there are others), the code you want sbatch to run on individual nodes is in the form:
```bash
apptainer run --bind <path_to_local_folder>:<path_in_container> \
    <path to the container sif> \
    <path_to_script_in_container>
```
In this case, the specific command is:
```bash
apptainer run --bind ~/hellgate_demos/apptainer/1_node/:/mnt/project/ \
        ~/hellgate_demos/apptainer/sif/geopy_container.sif \
        /mnt/project/count_features_apptainer.py
```
### Note about file paths inside the container
One confusing thing about containers is dealing with file paths. Remember, containers have a completely isolated namespace. What this means in practice is that a container does not have automatic access to your filesystem. Rather, if your container needs to read or write to files on disk, you need to explicitly mount the required folders inside your container. 

This is what the `--bind` flag does in the command above. It says, "make the folder on my filesystem, `<path_to_local_folder>`, accessible inside the container, at the location `<path_in_container>`. The choice of `<path_in_container>` is completely arbitrary. Since this is intended to be a generic container for use with different kinds of scripts, I chose a generic name for the mounted folder, `/mnt/project`.

In our case, we are using the container to execute a python script that lives on our filesystem (see geo_container.def). This was done so we can use the same container to execute different scripts. So, we mount the folder (or parent folder) where our python script lives, and then pass the location of the script as a parameter to `apptainer run`. Note, that the location of the script that we pass to apptainer is relative to the container's namespace, and the newly-mounted folder: `/mnt/project/count_features_apptainer.py`.

See or example sbatch script, `count_features_batch_1-node.sh`

### 3) Check/modify the file paths in your python script to match the container paths, above.
When you run a python script inside the container, it's running in the namespace of the container. So, if your python script reads from or writes to yfilesystem, the file paths should be relative to the container's namespace. This means changing any path references from from `<path_in_local_folde>` to `<path_in_container>`.

- See `count_features_apptainer.py`

### 4) Run the sbatch script
```bash
sbatch count_features_batch_1-node.sh
```