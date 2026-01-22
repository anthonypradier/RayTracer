from rayTracer import RayTracer
from core.scene import Scene

if __name__ == "__main__":
    scene = Scene()
    scene.loadScene("scene1.json")
    
    rayTracer = RayTracer(scene)
    rayTracer.renderScene()