import math
from utils.vector import Vector
from core.scene import Scene
from core.camera import Camera
from PIL import Image

class RayTracer:
    def __init__(self):
        self.camera: Camera = Camera()
        self.scene: Scene = Scene()
        self.img = Image.new(mode='RGB', size=(self.camera.Cw, self.camera.Ch))
    
    def renderScene(self):
        print(self.camera)
        self.scene.initScene()
        
        print("Rendering...")
        for j in range(self.camera.Ch):
            # x = i + self.camera.Cw // 2
            for i in range(self.camera.Cw):
                # y = j + self.camera.Ch // 2
                direction: Vector = self.camera.canvasToViewport(i, j).normalize()
                color: tuple = self.scene.traceRay(self.camera.pos, direction, t_min=1.0, t_max=math.inf)
                self.img.putpixel((i, j), color)
        self.saveImg("output.png")
        
    def saveImg(self, fileName: str):
        self.img.save(fileName)
        print("Render finished !")