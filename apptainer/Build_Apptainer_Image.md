# Building an Apptainer Container Image

Container images are portable snapshots of the contents and congifurations of a container. They are a complete blueprint for building and running a container instance. 

In Apptainer, container images are stored as .sif files, and their "recipe" is stored in .def files.  

## Building geo_container.def

In my `apptainer build geopy_container.sif geopy_container.def`