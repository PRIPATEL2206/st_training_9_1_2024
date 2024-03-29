
class Point: 
	def __init__(self, x, y): 
		self.x = x 
		self.y = y 

def Left_index(points): 

	minn = 0
	for i in range(1,len(points)): 
		if points[i].x < points[minn].x: 
			minn = i 
		elif points[i].x == points[minn].x: 
			if points[i].y > points[minn].y: 
				minn = i 
	return minn 

def orientation(p, q, r): 

	val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y) 

	if val == 0: 
		return 0
	elif val > 0: 
		return 1
	else: 
		return 2

def convexHull(points, n): 
	
	if n < 3: 
		return

	l = Left_index(points) 

	hull = [] 
	
	p = l 
	q = 0
	while(True): 
		
		hull.append(p) 

		q = (p + 1) % n 

		for i in range(n): 
			
			if(orientation(points[p], 
						points[i], points[q]) == 2): 
				q = i 

		p = q 

		if(p == l): 
			break

	for each in hull: 
		print(points[each].x, points[each].y) 

points = [] 
points.append(Point(0, 3)) 
points.append(Point(2, 2)) 
points.append(Point(1, 1)) 
points.append(Point(2, 1)) 
points.append(Point(3, 0)) 
points.append(Point(0, 0)) 
points.append(Point(3, 3)) 

convexHull(points, len(points)) 
