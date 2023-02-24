


#This file takes a trajectory file, unwraps it, and rewraps using a
#a selection then performs fits of the protein over all frames and 
#uses the transformation matrix to transform all other coordinates


#gets the current path
set path [pwd]
puts $path
cd $path



#imports qwrap package
package require qwrap
#gets the psfname, pdbname, number of runs, and the name of the trajectory file from arguments
set psfname [lindex $argv 0]
set pdbname [lindex $argv 0]
set numberTraj [lindex $argv 1]
set trajfile [lindex $argv 2]

#file to align to 
mol new ~/Desktop/CrowdDiffusion/ref3.pdb waitfor all
#sets the reference and the list of unique residues in this pdb
set reference [atomselect top all]
set residList [$reference get resid]
set uniqResList [lsort -unique $residList]

#gets the selection of unique residues to align to the reference pdb
set segsel "segname AP1 and resid $uniqResList"

#adds a new copy of the psf and pdb and outputs the run number
mol new $psfname.psf waitfor all
mol addfile $pdbname.pdb waitfor all
puts $trajfile
#adds each trajectory file and waits for them all to load in
for {set i 1} {$i <= $numberTraj} {incr i} {
	mol addfile $trajfile$i.dcd waitfor all
}


#unwrap, write Ions positions unwrapped
package require qwrap
qunwrap

#detect if the ion is present or not(which position getFile to call)
set magPresent [expr {[ [atomselect top "name MG"] num] > 0}]
set sodPresent [expr {[ [atomselect top "name SOD"] num] > 0}]
set claPresent [expr {[ [atomselect top "name CLA"] num] > 0}]

#sets arguments for Ion writeout
set argv [list $pdbname-unwrapped 0]
#ion writeout
if {$magPresent == 1} {
	source ~/Desktop/CrowdDiffusion/Scripts/getFiles/Mag/getPosMag.tcl
}
if {$sodPresent == 1} {
	source ~/Desktop/CrowdDiffusion/Scripts/getFiles/Sod/getPosSod.tcl
}
if {$claPresent == 1} {
	source ~/Desktop/CrowdDiffusion/Scripts/getFiles/Cla/getPosCla.tcl
}

#call the ATP get file
source ~/Desktop/CrowdDiffusion/Scripts/ATP/getPosATP1N.tcl
#rewrap the file so that the protein is centered
qwrap sel "not segname AP1" center "segname AP1"
puts "setting numframes"


#set the number of frames
set numframes [molinfo top get numframes]
#create the selection using the previous list of unique reference residues
set sel [atomselect top $segsel]


puts "For Loop engage"
#creates a selection of all atoms using name all
set all [atomselect top all]
#loops through each frame
for {set i 1} {$i < $numframes} {incr i} {
	#updated segname AP1(protein selections) to frame i
	$sel frame $i
	#create a rotation and translation matrix using the reference and the protein selection
	set transmat [measure fit $sel $reference]
	#update all
	$all frame $i
	#move all atoms using the transformation matrix(rotates and translates)
	$all move $transmat
}

#sets the argument to be the name of the pdb file
set argv [list $pdbname-wrapped 0]

#writes wrapped positions of ions
if {$magPresent == 1} {
	source ~/Desktop/CrowdDiffusion/Scripts/getFiles/Mag/getPosMag.tcl
}
if {$sodPresent == 1} {
	source ~/Desktop/CrowdDiffusion/Scripts/getFiles/Sod/getPosSod.tcl
}
if {$claPresent == 1} {
	source ~/Desktop/CrowdDiffusion/Scripts/getFiles/Cla/getPosCla.tcl
}

#call the ATP get file
source ~/Desktop/CrowdDiffusion/Scripts/ATP/getPosATP1N.tcl
