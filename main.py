from rayTracer import RayTracer
from core.scene import Scene

if __name__ == "__main__":
    scene = Scene()
    scene.loadScene("scene1.json")
    
    recursion_depth: int = 2
    rayTracer = RayTracer(scene, recursion_depth)
    rayTracer.renderScene()