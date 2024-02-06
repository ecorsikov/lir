#determine if three coordinates form a right angle. pt2 is the angle we are measuring
def right_angle(pt1,pt2,pt3):
	return (pt2[0]-pt1[0])*(pt2[0]-pt3[0])+(pt2[1]-pt1[1])*(pt2[1]-pt3[1])==0
#check to see if the points given form a rectangle by determining if the angles are orthoganal.
def is_rectangle(pt1,pt2,pt3,pt4):
	return right_angle(pt1,pt2,pt3)&&right_angle(pt2,pt3,pt4)&&right_angle(pt3,pt4,pt1)


