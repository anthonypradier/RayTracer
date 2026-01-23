import math, time
from utils.vector import Vector
from core.scene import Scene
from core.camera import Camera
from PIL import Image

class RayTracer:
    def __init__(self, scene: Scene, recursion_depth: int = 0):
        self.recursion_depth: int = recursion_depth
        self.camera: Camera = Camera()
        self.scene: Scene = scene
        self.img = Image.new(mode='RGB', size=(self.camera.Cw, self.camera.Ch))
    
    def renderScene(self):
        print(self.camera)
        
        print("Rendering...")
        t1 = time.time_ns()
        for j in range(self.camera.Ch):
            # x = i + self.camera.Cw // 2
            for i in range(self.camera.Cw):
                # y = j + self.camera.Ch // 2
                direction: Vector = self.camera.canvasToViewport(i, j).normalize()
                color: tuple = self.scene.traceRay(self.camera.pos, direction, 1.0, math.inf, self.recursion_depth)
                self.img.putpixel((i, j), color)
        self.saveImg("output.png")
        t2 = time.time_ns()
        print("Render finished :", round((t2-t1)*1e-9, 2), "s")
        
    def saveImg(self, fileName: str):
        self.img.save(fileName)