package require pbctools

puts "writing ATP"

#selects all ATP segments
set ATP [atomselect top "segname TP1 to TP3"]

#gets number of frames
set nf [molinfo top get numframes]
#stores current path
set pathDir [pwd]

#prints first argument
puts [lindex $argv 0]

#changes the directory to the Analysis Folder

#this directory is where you store output
cd ~/Desktop/CrowdDiffusion/Analysis
#sets the name of the simulation, and the number of runs

set nameSim [lindex $argv 0]
set count [lindex $argv 1]
#creates a new directory with the name of the simulation
file mkdir "$nameSim"
cd "$nameSim"

#writes the ATP selection to a position file format which stores all positions

#opens csv files
set fo [open "$nameSim-$count-ATP.csv" w ]

#puts the header information
puts $fo "Frame Number,Index,X,Y,Z"
for { set f 0} {$f <= $nf} {incr f} {
	#updates selection of ATP's to frame f
	$ATP frame $f
	$ATP update
	
	#gets the position of all ATP atoms
	set ATPPos [$ATP get {x y z segname} ]
	#sets the length of this list to loop through
	set ATPLength [llength $ATPPos]
	
	#loops through each atom in ATP list of atoms
	for {set i 0} {$i < $ATPLength} {incr i} {
		#sets the position index
		set ATPPosIndex [lindex $ATPPos $i]
		#sets the x,y, and z
		set ATPx [lindex $ATPPosIndex 0]
		set ATPy [lindex $ATPPosIndex 1]
		set ATPz [lindex $ATPPosIndex 2]
		#sets the segment number of ATP
		set ATPseg [lindex $ATPPosIndex 3]

		#outputs in order of frame number, atom index, x, y, z, and segment
		puts $fo "$f,$i,$ATPx,$ATPy,$ATPz,$ATPseg" 	
	}
}	

#closes the files
close $fo

#goes back to original directory
cd "$pathDir"
