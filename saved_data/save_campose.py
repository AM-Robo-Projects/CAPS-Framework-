import numpy as np

transformation_matrix = np.array([
    [0.6927,  0.0172, -0.7210,  0.2674],
    [-0.0402, 0.9991, -0.0148,  0.4377],
    [0.7201,  0.0393,  0.6928,  0.2896],
    [0.0000,  0.0000,  0.0000,  1.0000]
])

np.savetxt("camera_pose.txt", transformation_matrix, fmt="%.4f")

