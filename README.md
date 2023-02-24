This repository is a storage of my various scripts that I have refined. This is a distillation of all of the scripts that
I have used and want to show. Most of these scripts require VMD. The 1N.tcl and 2N.tcl scripts require you to open VMD
and pass arguments into it in this fashion:

set argv [list "Simulation name" "# of trajectory files" "TrajectoryName_"]



This also requires that your trajectory file names are formatted in a way that uses an integer at the end. For example, you
would format your trajectory files as Run_1.dcd, Run_2.dcd, and so on. 

The output of using 1N and 2N scripts are csv files that generally take up large storage size. These csv files are organized 
according to the header written below:

The getFile scripts outputs in order of frame number, atom index, x, y, z, (segment)

Note that depending on the getFile script segment may or may not be included.


Simulation setups are located in the Protein directory along with the buildN.tcl script. This repository will later contain the
psfgen tool log of the created system. Additionally, this repository doesn't contain the right scripts for the crowded dataframe
as of 2.24.2023 and should contain this script as of 2.27.2023.
