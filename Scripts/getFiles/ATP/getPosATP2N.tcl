package require pbctools

puts "writing ATP"

set ATP [atomselect top "segname TP1 to TP9 TQ0 to TQ9"]
set nf [molinfo top get numframes]
set pathDir [pwd]

puts [lindex $argv 0]
cd /Scr/alutsky/scripts/Analysis/
set nameSim [lindex $argv 0]
set count [lindex $argv 1]
file mkdir "$nameSim"
cd "$nameSim"

#writes the Cla selection to a position file format which stores all positions

set fo [open "$nameSim-$count-ATP.csv" w ]

puts $fo "Frame Number,Index,X,Y,Z"
for { set f 0} {$f <= $nf} {incr f} {
	$ATP frame $f
	$ATP update

	set ATPPos [$ATP get {x y z segname} ]
	set ATPLength [llength $ATPPos]
	for {set i 0} {$i < $ATPLength} {incr i} {
		
		set ATPPosIndex [lindex $ATPPos $i]

		set ATPx [lindex $ATPPosIndex 0]
		set ATPy [lindex $ATPPosIndex 1]
		set ATPz [lindex $ATPPosIndex 2]
		set ATPseg [lindex $ATPPosIndex 3]
		puts $fo "$f,$i,$ATPx,$ATPy,$ATPz,$ATPseg" 	
	}
}	

close $fo

cd "$pathDir"
