from utils.vector import Vector

def reflect_ray(R: Vector, N: Vector) -> Vector:
    return N * 2 * R.dot(N) - R