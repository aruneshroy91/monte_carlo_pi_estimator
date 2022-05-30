# A Monte carlo pi estimator by Arunesh Roy
############################################
import numpy as np
# Initialize circle and sqaure points

num_points = 2000

#circle_points = 0
#square_points = 0

# random points

X = np.random.uniform(-1,1, num_points)
Y = np.random.uniform(-1,1, num_points)

# distance from the origin
origin_distance = [x**2 + y**2 for x in X for y in Y]

# points inside and outside the circle
circle_points_count = [dist<=1 for dist in origin_distance].count(True)
square_points_count = len(origin_distance)
# estimate of pi = 4*area of circle / area of square
estimate_of_pi = 4*circle_points_count/square_points_count

print("Estimatated pi is {} for {} number of points.".format(estimate_of_pi,num_points**2))



