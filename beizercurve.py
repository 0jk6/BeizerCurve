import numpy as np
import matplotlib.pyplot as plt;

#class to represent a point
class Point:
	def __init__(self, x, y):
		self.x = x;
		self.y = y;

class BeizerCurve:
	def __init__(self, p0, p1, p2, p3):
		#4 control points
		self.p0 = p0
		self.p1 = p1
		self.p2 = p2
		self.p3 = p3

		#output
		self.X = []
		self.Y = []
		self.step = 0.05


	def beizer(self, step=0.05):
		self.step = step
		for t in np.arange(0, 1, self.step):
			x = np.power((1-t),3)*self.p0.x + 3*np.power((1-t),2)*t*self.p1.x + 3*(1-t)*t*t*self.p2.x + t*t*t*self.p3.x
			y = np.power((1-t),3)*self.p0.y + 3*np.power((1-t),2)*t*self.p1.y + 3*(1-t)*t*t*self.p2.y + t*t*t*self.p3.y

			self.X.append(x)
			self.Y.append(y)

	def plot(self):
		plt.scatter(self.X, self.Y, c='#2ca02c')
		plt.title(f"Beizer curve with steps = {self.step}")
		plt.show()


#define 4 control points
p0 = Point(0,10);
p1 = Point(1,-40);
p2 = Point(11,6);
p3 = Point(3,0);

#plot the curve
curve = BeizerCurve(p0, p1, p2, p3)
curve.beizer(step=0.01)
curve.plot()