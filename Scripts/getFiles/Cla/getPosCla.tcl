package require pbctools

puts "writing CLA wrapped"

set cla [atomselect top "name CLA" ]
set nf [molinfo top get numframes]
set pathDir [pwd]

puts [lindex $argv 0]
cd /Scr/alutsky/scripts/Analysis/
set nameSim [lindex $argv 0]
set count [lindex $argv 1]
file mkdir "$nameSim"
cd "$nameSim"

#writes the Cla selection to a position file format which stores all positions

set fo [open "$nameSim-$count-CLA.csv" w ]

puts $fo "Frame Number,Index,X,Y,Z"
for { set f 0} {$f <= $nf} {incr f} {
	$cla frame $f
	$cla update

	set claPos [$cla get {x y z} ]
	set claLength [llength $claPos]
	for {set i 0} {$i < $claLength} {incr i} {
		
		set claPosIndex [lindex $claPos $i]

		set clax [lindex $claPosIndex 0]
		set clay [lindex $claPosIndex 1]
		set claz [lindex $claPosIndex 2]
		puts $fo "$f,$i,$clax,$clay,$claz" 	
	}
}	

close $fo

cd "$pathDir"
