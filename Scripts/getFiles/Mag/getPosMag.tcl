package require pbctools
#prints Mag 
puts "writing MAG wrapped"

#selects magnesium ions
set mag [atomselect top "name MG" ]
#sets the number of frames and the path directory
set nf [molinfo top get numframes]
set pathDir [pwd]

#prints the name of the simulation
puts [lindex $argv 0]
#changes directory to output directory
cd ~/Desktop/CrowdDiffusion/
#sets name of the simulation and the number of runs
set nameSim [lindex $argv 0]
set count [lindex $argv 1]

#creates a new directory and changes to that new directory
file mkdir "$nameSim"
cd "$nameSim"

#writes the MAG selection to a position file format which stores all positions

#opens the file
set fo [open "$nameSim-$count-MAG.csv" w ]

#puts header information
puts $fo "Frame Number,Index,X,Y,Z"

#loops through each frame
for { set f 0} {$f <= $nf} {incr f} {
	#changes the selection to frame f and updates that selection
	$mag frame $f
	$mag update
	
	#gets a list of all positions of each index of the selection mag
	set magPos [$mag get {x y z} ]
	#gets the length of the list
	set magLength [llength $magPos]

	#loops through the indices of the list
	for {set i 0} {$i < $magLength} {incr i} {
		#sets the index
		set magPosIndex [lindex $magPos $i]
		#gets the x, y, and z
		set magx [lindex $magPosIndex 0]
		set magy [lindex $magPosIndex 1]
		set magz [lindex $magPosIndex 2]	
		#outputs in order of frame number, atom index, x, y, and z
		puts $fo "$f,$i,$magx,$magy,$magz" 	
	}
}	

#closes the file
close $fo

#goes to previous directory
cd "$pathDir"
