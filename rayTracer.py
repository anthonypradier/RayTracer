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
        for i in range(-self.camera.Cw // 2, self.camera.Cw // 2):
            for j in range(-self.camera.Ch // 2, self.camera.Ch // 2):
                # image pixel : (i, j), get the corresponding viewport point, trace a ray, determine the collision
                direction: Vector = self.camera.canvasToViewport(i, j)
                color: tuple = self.scene.traceRay(self.camera.pos, direction)
                self.img.putpixel((i, j), (40, 40, 40))
        self.saveImg("output.png")
        
    def saveImg(self, fileName: str):
        self.img.save(fileName)