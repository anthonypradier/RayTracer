from utils.vector import Vector
from typing import List, Tuple

class Camera:
    def __init__(self):
        self.Vw: float = 4.0
        self.Vh: float = 3.0
        self.d: float = 1.0
        
        self.screenFactor: int = 300
        self.Cw: int = int(self.screenFactor * self.Vw)
        self.Ch: int = int(self.screenFactor * self.Vh)
        
        self.pos: Vector = Vector(0, 0, 0)
        
        self.canvas: List[list] = [[(0, 0, 0) for _ in range(self.Cw)] for _ in range(self.Ch)]
    
    def __repr__(self) -> str:
        return f"Camera details :\n\tVw : {self.Vw} | Vh : {self.Vh}\n\tDistance d : {self.d}\n\tCw : {self.Cw} | Ch : {self.Ch}"
    
    def canvasToViewport(self, x: int, y: int):
        return Vector(
            x * self.Vw / self.Cw,
            y * self.Vh / self.Ch,
            self.d
        )