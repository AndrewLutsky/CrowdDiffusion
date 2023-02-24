package require pbctools
#prints SOD
puts "writing SOD wrapped"

#sets selection of sodium ions
set sod [atomselect top "name SOD" ]
#gets the number of frames and current directory
set nf [molinfo top get numframes]
set pathDir [pwd]

#prints the name of the simulation andn changes directory to output directory
puts [lindex $argv 0]
cd ~/Desktop/CrowdDiffusion/

#sets name of the simulation and how many runs
set nameSim [lindex $argv 0]
set count [lindex $argv 1]
#creates a directory and changes to new directory
file mkdir "$nameSim"
cd "$nameSim"

#writes the Sod selection to a position file format which stores all positions

#opens a new file
set fo [open "$nameSim-$count-SOD.csv" w ]

#puts in header information
puts $fo "Frame Number,Index,X,Y,Z"
#loops through each frame
for { set f 0} {$f <= $nf} {incr f} {
	#updates the selection to frame f
	$sod frame $f
	$sod update
	
	#gets the position of each atom in the selection
	set sodPos [$sod get {x y z} ]
	#gets the length of that list
	set sodLength [llength $sodPos]
	#loops through that list of indices
	for {set i 0} {$i < $sodLength} {incr i} {
		#sets the index number
		set sodPosIndex [lindex $sodPos $i]
		#gets the x,y, and z values
		set sodx [lindex $sodPosIndex 0]
		set sody [lindex $sodPosIndex 1]
		set sodz [lindex $sodPosIndex 2]
		#outputs in order of frame number, atom index, x, y, and z
		puts $fo "$f,$i,$sodx,$sody,$sodz" 	
	}
}	

#closes the file
close $fo

#returns to previous directory
cd "$pathDir"
