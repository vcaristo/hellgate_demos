# Building an Apptainer Container Image

Container images are portable snapshots of the contents and congifurations of a container. They are a complete blueprint for building and running a container instance.  

In Apptainer, container images are stored as .sif files, and their "recipe" is stored in .def files.  

## Building geo_container.def

The .def file contains all of the instructions needed to build and run a container:
- the `%post` section includes all of the packages and libraries that you code needs to run, obviating the need for conda environments or the like. 
- the %runscript tells Apptainer what the execute inside the container when it's called.

To keep things organized, we'll create our .sif file in folder, `sif`. Navigate to the folder that contains 'geo_container.def', and run the following code:

```bash
mkdir -p ../sif
apptainer build ../sif/geopy_container.sif geopy_container.def
```