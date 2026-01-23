from utils.vector import Vector
from typing import List, Tuple

class Camera:
    def __init__(self):
        self.Cw: int = 1200
        self.Ch: int = 800
        
        self.Vw: float = 1.0
        self.Vh: float = self.Vw*self.Ch/self.Cw
        self.d: float = 1.0
        
        self.pos: Vector = Vector(0, 0, 0)
        
        self.canvas: List[list] = [[(0, 0, 0) for _ in range(self.Cw)] for _ in range(self.Ch)]
    
    def __repr__(self) -> str:
        return f"Camera details :\n\tVw : {self.Vw} | Vh : {self.Vh}\n\tDistance d : {self.d}\n\tCw : {self.Cw} | Ch : {self.Ch}\n\tRatio : Canvas = {self.Cw/self.Ch} - viewport = {self.Vw/self.Vh}"
    
    def canvasToViewport(self, x: int, y: int) -> Vector:
        Px: float = (x - self.Cw // 2) * self.Vw / self.Cw
        Py: float = (y - self.Ch // 2) * self.Vh / self.Ch
        Pz: float = self.d
        return Vector(
            Px,
            Py,
            Pz
        ).normalize()