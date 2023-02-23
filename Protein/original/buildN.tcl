package require pbctools
package require topotools

#set amount of dimensions here
set N 5
set num [ expr { $N ** 3} ]

#set distance between each protein
set dist 70


set tot 0
for {set i 0} {$i < $N} {incr i} {
	for {set j 0} {$j < $N} {incr j} {
		for {set k 0} {$k < $N} {incr k} {
			
			mol new 1wi8_autopsf.psf
			mol addfile 1wi8_autopsf.pdb
			mol rename top $tot
			set sel [atomselect top all]
			set x [ expr {rand() * 360 } ]
                        set y [ expr {rand() * 360 } ]
                        set z [ expr {rand() * 360 } ]
                        set matrix_x [transaxis x $x]
			set matrix_y [transaxis y $y]
			set matrix_z [transaxis z $z]
			$sel move $matrix_x
			$sel move $matrix_y
			$sel move $matrix_z

			set vec [list $i $j $k ]
			puts $vec
			set vec [vecscale $dist $vec]
			$sel moveby $vec
			incr tot
		
		}
		puts $j
	}
	puts $i
}
set sellist {}
for {set i 0} {$i < $num} {incr i} {
	set sel [atomselect $i all]
	lappend sellist $sel
	

}

set mol [::TopoTools::selections2mol $sellist]
animate write psf lattice.psf $mol
animate write pdb lattice.pdb $mol
