package require pbctools

puts "writing SOD wrapped"

set sod [atomselect top "name SOD" ]
set nf [molinfo top get numframes]
set pathDir [pwd]

puts [lindex $argv 0]
cd /Scr/alutsky/scripts/Analysis/
set nameSim [lindex $argv 0]
set count [lindex $argv 1]
file mkdir "$nameSim"
cd "$nameSim"

#writes the Cla selection to a position file format which stores all positions

set fo [open "$nameSim-$count-SOD.csv" w ]

puts $fo "Frame Number,Index,X,Y,Z"
for { set f 0} {$f <= $nf} {incr f} {
	$sod frame $f
	$sod update

	set sodPos [$sod get {x y z} ]
	set sodLength [llength $sodPos]
	for {set i 0} {$i < $sodLength} {incr i} {
		
		set sodPosIndex [lindex $sodPos $i]

		set sodx [lindex $sodPosIndex 0]
		set sody [lindex $sodPosIndex 1]
		set sodz [lindex $sodPosIndex 2]
		puts $fo "$f,$i,$sodx,$sody,$sodz" 	
	}
}	

close $fo

cd "$pathDir"
