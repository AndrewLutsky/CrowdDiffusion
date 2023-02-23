


#This file takes a trajectory file, unwraps it, and rewraps using a
#a selection then performs fits of the protein over all frames and 
#uses the transformation matrix to transform all other coordinates

#read in pdb and psf files
#read in dcd files

set path [pwd]
puts $path
cd $path




package require qwrap
set psfname [lindex $argv 0]
set pdbname [lindex $argv 0]
set numberTraj [lindex $argv 1]
set trajfile [lindex $argv 2]

mol new /Scr/alutsky/scripts/DataTransform/ref3.pdb waitfor all
set reference [atomselect top all]
set residList [$reference get resid]
set uniqResList [lsort -unique $residList]

mol new $psfname.psf waitfor all
mol addfile $pdbname.pdb waitfor all
puts $trajfile
set segsel "segname AP1 and resid $uniqResList"
for {set i 1} {$i <= $numberTraj} {incr i} {
	mol addfile $trajfile$i.dcd waitfor all
}


#unwrap, write Ions positions unwrapped
package require qwrap
qunwrap

#detet if ion present
set magPresent [expr {[ [atomselect top "name MG"] num] > 0}]
set sodPresent [expr {[ [atomselect top "name SOD"] num] > 0}]
set claPresent [expr {[ [atomselect top "name CLA"] num] > 0}]

#sets arguments for Ion writeout
set argv [list $pdbname-unwrapped 0]
if {$magPresent == 1} {
	source /Scr/alutsky/scripts/Mag/getPosMag.tcl
}
if {$sodPresent == 1} {
	source /Scr/alutsky/scripts/Sod/getPosSod.tcl
}
if {$claPresent == 1} {
	source /Scr/alutsky/scripts/Cla/getPosCla.tcl
}
source /Scr/alutsky/scripts/ATP/getPosATP1N.tcl
qwrap sel "not segname AP1" center "segname AP1"
puts "setting numframes"



set numframes [molinfo top get numframes]
set sel [atomselect top $segsel]

puts "For Loop engage"
set all [atomselect top all]
for {set i 1} {$i < $numframes} {incr i} {
	$sel frame $i
	set transmat [measure fit $sel $reference]
	$all frame $i	
	$all move $transmat
}

set argv [list $pdbname-wrapped 0]

if {$magPresent == 1} {
	source /Scr/alutsky/scripts/Mag/getPosMag.tcl
}
if {$sodPresent == 1} {
	source /Scr/alutsky/scripts/Sod/getPosSod.tcl
}
if {$claPresent == 1} {
	source /Scr/alutsky/scripts/Cla/getPosCla.tcl
}
source /Scr/alutsky/scripts/ATP/getPosATP1N.tcl
