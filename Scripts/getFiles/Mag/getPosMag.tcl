package require pbctools

puts "writing MAG wrapped"

set mag [atomselect top "name MG" ]
set nf [molinfo top get numframes]
set pathDir [pwd]

puts [lindex $argv 0]
cd /Scr/alutsky/scripts/Analysis/
set nameSim [lindex $argv 0]
set count [lindex $argv 1]
file mkdir "$nameSim"
cd "$nameSim"

#writes the Cla selection to a position file format which stores all positions

set fo [open "$nameSim-$count-MAG.csv" w ]

puts $fo "Frame Number,Index,X,Y,Z"
for { set f 0} {$f <= $nf} {incr f} {
	$mag frame $f
	$mag update

	set magPos [$mag get {x y z} ]
	set magLength [llength $magPos]
	for {set i 0} {$i < $magLength} {incr i} {
		
		set magPosIndex [lindex $magPos $i]

		set magx [lindex $magPosIndex 0]
		set magy [lindex $magPosIndex 1]
		set magz [lindex $magPosIndex 2]
		puts $fo "$f,$i,$magx,$magy,$magz" 	
	}
}	

close $fo

cd "$pathDir"
