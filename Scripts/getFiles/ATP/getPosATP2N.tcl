package require pbctools

#prints writing ATP
puts "writing ATP"


#selector for ATP segments
set ATP [atomselect top "segname TP1 to TP9 TQ0 to TQ9"]

#sets number of frames and path to a variable
set nf [molinfo top get numframes]
set pathDir [pwd]

#prints first argument
puts [lindex $argv 0]

#changes directory to output directory
cd ~/Desktop/CrowdDiffusion/

#sets name and count of how many runs
set nameSim [lindex $argv 0]
set count [lindex $argv 1]
#creates a directory after name of Sim and changes to that directory
file mkdir "$nameSim"
cd "$nameSim"

#writes the ATP selection to a position file format which stores all positions


#opens file
set fo [open "$nameSim-$count-ATP.csv" w ]

#puts header
puts $fo "Frame Number,Index,X,Y,Z"
#loops over each frame
for { set f 0} {$f <= $nf} {incr f} {
	#Updates ATP selection to frame f
	$ATP frame $f
	$ATP update
	
	#gets a list of all atoms in ATP selection in frame f
	set ATPPos [$ATP get {x y z segname} ]
	#gets length of the list
	set ATPLength [llength $ATPPos]

	#loops through each index of the list
	for {set i 0} {$i < $ATPLength} {incr i} {
		
		#gets the index
		set ATPPosIndex [lindex $ATPPos $i]
		#gets X,Y, and Z
		set ATPx [lindex $ATPPosIndex 0]
		set ATPy [lindex $ATPPosIndex 1]
		set ATPz [lindex $ATPPosIndex 2]
		#gets ATP segment name
		set ATPseg [lindex $ATPPosIndex 3]

		#outputs in order of frame number, atom index, x, y, z, and segment
		puts $fo "$f,$i,$ATPx,$ATPy,$ATPz,$ATPseg" 	
	}
}	

#closes the file
close $fo


#goes to original directory
cd "$pathDir"
