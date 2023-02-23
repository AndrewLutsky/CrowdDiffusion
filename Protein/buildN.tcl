package require pbctools
package require topotools

#set amount of dimensions here
set N 7
set num [ expr { $N ** 3} ]

#set distance between each protein
set dist 70

#counter for number of proteins
set tot 0

#loops through x, y, and z dimensions
for {set i 0} {$i < $N} {incr i} {
	for {set j 0} {$j < $N} {incr j} {
		for {set k 0} {$k < $N} {incr k} {
			#adds a new mol object
			mol new 1wi8_autopsf.psf
			mol addfile 1wi8_autopsf.pdb
			#renames it to the number counter
			mol rename top $tot

			#selects everything from the top molid(current)
			set sel [atomselect top all]

			#randomly generates a number between 0 and 1 and multiplies by 360
			set x [ expr {rand() * 360 } ]
                        set y [ expr {rand() * 360 } ]
                        set z [ expr {rand() * 360 } ]

			#creates a matrix to move/rotate the protein by that amount
                        set matrix_x [transaxis x $x]
			set matrix_y [transaxis y $y]
			set matrix_z [transaxis z $z]
			$sel move $matrix_x
			$sel move $matrix_y
			$sel move $matrix_z

			#creates a list of what number of protein it is in X,Y, and Z
			set vec [list $i $j $k ]
			#outputs this list
			puts $vec

			#uses vector multiplication to multiply each integer by the distance
			set vec [vecscale $dist $vec]

			#moves the selection using that list
			$sel moveby $vec

			#increases counter
			incr tot
		
		}

		puts $j
	}
	puts $i
}

puts "TEST0"
#appends a selection for each molid to a list
set sellist {}
for {set i 0} {$i < $num} {incr i} {
	set sel [atomselect $i all]
	lappend sellist $sel
	

}

#uses topotools to merge a selection to a pdb and psf file
set mol [::TopoTools::selections2mol $sellist]
animate write psf lattice.psf $mol
animate write pdb lattice.pdb $mol
