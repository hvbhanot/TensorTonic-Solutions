import numpy as np

def rotate_around_z(points, theta):
    """
    Rotate 3D point(s) around the Z-axis by angle theta (radians).
    """ 

    points = np.asarray(points, dtype=float)

    c = np.cos(theta)
    s = np.sin(theta)

    if points.ndim == 1:
        x, y = points[0], points[1]

        points[0] = x*c - y*s
        points[1] = x*s + y*c

        return points

    elif points.ndim == 2:
        x = points[:,0].copy()
        y = points[:,1].copy()

        points[:,0] = x*c - y*s
        points[:,1] = x*s + y*c

        return points