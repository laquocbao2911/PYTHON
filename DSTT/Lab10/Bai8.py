import numpy as np
B1 = np.array([[-18,13,-4,4],
            [2,29,-4,12],
            [-14,11,-12,8],
            [-2,21,4,8]])
B2 = np.array([[6 ,-8 ,-4, 5, -4],
            [2, 7, -5, -6, 4],
            [0, -1,-8, 2,2],
            [-1, -2, 4, 4, -8]])

print("singular values of the matrices A1:",np.linalg.svd(B1,compute_uv=False))
print("singular values of the matrices A2:",np.linalg.svd(B2,compute_uv=False))