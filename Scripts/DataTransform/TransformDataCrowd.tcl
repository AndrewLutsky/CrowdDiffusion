#This file takes a trajectory file, unwraps it, and rewraps using a
#a selection then performs fits of the protein over all frames and 
#uses the transformation matrix to transform all other coordinates
#loops through each sement
#
#
#
#
#

#gets working directory
set path [pwd]
puts $path
cd $path




package require qwrap
set psfname [lindex $argv 0]
set pdbname [lindex $argv 0]
set numberTraj [lindex $argv 1]
set trajfile [lindex $argv 2]

#Checks to see which ions are present

mol addfile $pdbname.pdb waitfor all
set magPresent [expr {[ [atomselect top "name MG"] num] > 0}]
set sodPresent [expr {[ [atomselect top "name SOD"] num] > 0}]
set claPresent [expr {[ [atomselect top "name CLA"] num] > 0}]
mol delete top


#creates unwrapped trajectory file
puts "adding files"
mol new $psfname.psf waitfor all
mol addfile $pdbname.pdb waitfor all
for {set i 1} {$i <= $numberTraj} {incr i} {
	mol addfile $trajfile$i.dcd waitfor all
}


puts "unwrapping"
set numframes [molinfo top get numframes]
qunwrap

puts "writing unwrapped trajectory"
animate write dcd unwrapped.dcd beg 1 end $numframes 

puts "writing unwrapped ions"
set argv [list $pdbname-unwrapped 0]
if {$magPresent == 1} {	
	source /Scr/alutsky/scripts/Mag/getPosMag.tcl
}
if {$claPresent == 1} {
	source /Scr/alutsky/scripts/Cla/getPosCla.tcl
}
if {$sodPresent == 1} {
	source /Scr/alutsky/scripts/Sod/getPosSod.tcl	
}
source /Scr/alutsky/scripts/ATP/getPosATP.tcl


mol delete top
mol new /Scr/alutsky/scripts/DataTransform/ref3.pdb waitfor all
set reference [atomselect top all]
set refRes [$reference get resid]
set uniqRefRes [lsort -unique $refRes]

#loops through each segment, rewraps, and finds ion locations
for {set count 1} {$count < 9} {incr count} {
	puts $count
	mol new $psfname.psf
	mol addfile $pdbname.pdb

	for {set i 1} {$i <= $numberTraj} {incr i} {
		mol addfile $trajfile$i.dcd waitfor all
	}
	set numframes [molinfo top get numframes]
	set segsel "segname AP$count and resid $uniqRefRes"


	qwrap sel "not segname AP$count" center "segname AP$count"
	
#	if {$count == 1} {
#		set reference [atomselect top $segsel frame $numframes/2]
#
#	}
	set sel [atomselect top $segsel]
	set all [atomselect top all]
	for {set i 1} {$i < $numframes } {incr i} {
		$sel frame $i
		set transmat [measure fit $sel $reference]
		$all frame $i
		$all move $transmat
	}
	
	
	set argv [list $pdbname-wrapped $count]	
	if {$magPresent == 1} {	
		source /Scr/alutsky/scripts/Mag/getPosMag.tcl
	}
	if {$claPresent == 1} {
		source /Scr/alutsky/scripts/Cla/getPosCla.tcl
	}
	if {$sodPresent == 1} {
		source /Scr/alutsky/scripts/Sod/getPosSod.tcl	
	}
	source /Scr/alutsky/scripts/ATP/getPosATP.tcl
	puts "created rewrapped $count"		
	unset numframes
	if {$count != 1} {
		mol delete top
	}
}

