import math
import json
from typing import List, Tuple
from utils.vector import Vector
from objects.sphere import Sphere
from objects.object3D import Object3D
from lights.abstractLight import AbstractLight
from lights.ambientLight import AmbientLight
from lights.dirLight import DirLight
from lights.pointLight import PointLight
from core.scene_parser import SceneParser

class Scene:
    def __init__(self):
        self.objects: List[Object3D] = []
        self.lights: List[AbstractLight | AmbientLight | PointLight | DirLight] = []
        self.animations: List = []
        self.bg: tuple = (0, 0, 0)
        self.scene_parser = SceneParser(self)
        
    def traceRay(self, O: Vector, D: Vector, t_min: float = 1.0, t_max: float = math.inf) -> Tuple[int]:
        closest_t: float = math.inf
        closest_obj: Object3D = None
        for obj in self.objects:
            t1, t2 = obj.intersect(O, D)
            if t_min <= t1 < t_max and t1 < closest_t:
                closest_t = t1
                closest_obj = obj
            if t_min <= t2 < t_max and t2 < closest_t:
                closest_t = t2
                closest_obj = obj
        if closest_obj == None:
            return self.bg
        P: Vector = O + D * closest_t # Compute intersection
        N: Vector = P - closest_obj.center  # Compute sphere normal at intersection
        N = N.normalize()
        i: float = self.compute_lighting(P, N, -D, closest_obj.specular) # D is from the cam to the point, -D from the point to the cam
        color: Tuple[int] = (int(closest_obj.color[0] * i), int(closest_obj.color[1] * i), int(closest_obj.color[2] * i))
        return color
    
    def compute_lighting(self, point: Vector, normal: Vector, V: Vector, s: int) -> float:
        i: float = 0.0
        for light in self.lights:
            i += light.get_intensity_at_point(point, normal, V, s)
        return i  
    
    def loadScene(self, filename: str):
        """Load a complete scene from a json file. The file name in parameter can be './dir/file.json', '/dir/file.json', 'dir/file.json', 'file.json', or the same ones without '.json'.

        Args:
            filename (str): the name of the json file
        """
        
        if(not filename.endswith(".json")):
            filename += ".json"
            
        name = filename
        if(filename.startswith("./scenes/") or filename.startswith("/scenes/") or filename.startswith("scenes/")):
            name = filename.split("scenes/")[1]
        
        scene = None
        try:
            print("Loading " + name + "...")
            with open("./scenes/" + name, 'r') as file:
                scene = json.load(file)
                
        except:
            raise FileNotFoundError("The specified file/path doesn't exists")
        
        self.scene_parser.parse_scene(scene)
        print(f"Scene loaded \n\tobjects : {self.objects}\n\tlights : {self.lights}\n\tanimations : {self.animations}")

    def add_object(self, obj):
        self.objects.append(obj)

    def add_light(self, light):
        self.lights.append(light)
    
    def add_animation(self, animation):
        self.animations.append(animation)