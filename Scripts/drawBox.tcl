#function that given minimum and maximum coordinates creates an outline of a box
proc drawBox {min max} {
	#set min and max x y z values
	puts "$min $max"
	set minx [lindex $min 0]
	set miny [lindex $min 1]
	set minz [lindex $min 2]
	set maxx [lindex $max 0]
	set maxy [lindex $max 1]
	set maxz [lindex $max 2]
	
	#sets color
	
	draw color iceblue


	#draw line {x1 y1 z1} {x2 y2 z2}

	draw line "$minx $miny $minz" "$maxx $miny $minz"
	draw line "$minx $miny $minz" "$minx $maxy $minz"
	draw line "$minx $miny $minz" "$minx $miny $maxz"
	draw line "$maxx $miny $minz" "$maxx $maxy $minz"
	draw line "$maxx $miny $minz" "$maxx $miny $maxz"
	draw line "$minx $maxy $minz" "$maxx $maxy $minz"
	draw line "$minx $maxy $minz" "$minx $maxy $maxz"
	draw line "$minx $miny $maxz" "$maxx $miny $maxz"
	draw line "$minx $miny $maxz" "$minx $maxy $maxz"
	draw line "$maxx $maxy $maxz" "$maxx $maxy $minz"
	draw line "$maxx $maxy $maxz" "$minx $maxy $maxz"
	draw line "$maxx $maxy $maxz" "$maxx $miny $maxz"
}


#function that given minimum and maximum coordinate creates a drawn in box
proc drawBoxFill {min max} {

	set minx [lindex $min 0]
	set miny [lindex $min 1]
	set minz [lindex $min 2]
	set maxx [lindex $max 0]
	set maxy [lindex $max 1]
	set maxz [lindex $max 2]
	
	draw color iceblue
	draw materials on
	draw material Glass1

	draw triangle "$minx $miny $minz" "$minx $maxy $minz" "$minx $maxy $maxz"
	draw triangle "$minx $miny $minz" "$minx $miny $maxz" "$minx $maxy $maxz"

	draw triangle "$minx $miny $minz" "$maxx $miny $minz" "$maxx $maxy $minz"
	draw triangle "$minx $miny $minz" "$minx $maxy $minz" "$maxx $maxy $minz"

	draw triangle "$minx $miny $minz" "$maxx $miny $minz" "$maxx $miny $maxz"
	draw triangle "$minx $miny $minz" "$minx $miny $maxz" "$maxx $miny $maxz"


	draw triangle "$maxx $maxy $maxz" "$maxx $maxy $minz" "$maxx $miny $minz"
	draw triangle "$maxx $maxy $maxz" "$maxx $miny $maxz" "$maxx $miny $minz"
	
	draw triangle "$maxx $maxy $maxz" "$minx $maxy $maxz" "$minx $miny $maxz"
	draw triangle "$maxx $maxy $maxz" "$maxx $miny $maxz" "$minx $miny $maxz"
	
	draw triangle "$maxx $maxy $maxz" "$minx $maxy $maxz" "$minx $maxy $minz"
	draw triangle "$maxx $maxy $maxz" "$maxx $maxy $minz" "$minx $maxy $minz"


}
