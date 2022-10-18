import numpy as np

s1 = np.array([1, 2, 3]).T
s2 = np.array([7, 4, 3]).T
s3 = np.array([2, 1, 9]).T

dis_s12 = np.linalg.norm(s2 - s1)
print(dis_s12)

dis_s13 = np.linalg.norm(s3 - s1)
print(dis_s13)

dis_s23 = np.linalg.norm(s3 - s2)
print(dis_s23)