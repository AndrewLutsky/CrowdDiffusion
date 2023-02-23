package require pbctools
package require qwrap


set cla [atomselect top "name CLA" ]
set nf [molinfo top get numframes]



#writes the Cla selection to a position file format which stores all positions

set fo [open "PosClaUnwrapped.csv" w ]

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


