
package require pbctools

#prints writing CLA
puts "writing CLA wrapped"


#selects Cla atoms
set cla [atomselect top "name CLA" ]
#gets the number of frames total and sets the path to a variable
set nf [molinfo top get numframes]
set pathDir [pwd]

#prints name of the simulation
puts [lindex $argv 0]

#changes directory to output directory
cd ~/Desktop/CrowdDiffusion
#sets the name of the simulation and number of runs
set nameSim [lindex $argv 0]
set count [lindex $argv 1]

#creates a new directory and changes to new directory
file mkdir "$nameSim"
cd "$nameSim"

#writes the Cla selection to a position file format which stores all positions
#opens file
set fo [open "$nameSim-$count-CLA.csv" w ]

#puts in header information
puts $fo "Frame Number,Index,X,Y,Z"

#loops through each frame
for { set f 0} {$f <= $nf} {incr f} {
	#updates selection to the frame number f
	$cla frame $f
	$cla update
	
	#gets position of Cla ions
	set claPos [$cla get {x y z} ]
	#gets length of the list of Cla Ion positions
	set claLength [llength $claPos]
	#loops through their indeces
	for {set i 0} {$i < $claLength} {incr i} {
		#sets index variable
		set claPosIndex [lindex $claPos $i]
		#sets X,Y, and Z
		set clax [lindex $claPosIndex 0]
		set clay [lindex $claPosIndex 1]
		set claz [lindex $claPosIndex 2]
		#outputs in order of frame number, atom index, x, y, and z
		puts $fo "$f,$i,$clax,$clay,$claz" 	
	}
}	

#closes the file
close $fo

#changes back to original path
cd "$pathDir"
