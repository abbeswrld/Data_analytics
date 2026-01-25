from dataclasses import dataclass

@dataclass
class Champion:
    id: int = None
    name: str = ""
    
    @staticmethod
    def generate_one(name: str):
        return Champion(name=name)
    
    def to_tuple(self) -> tuple:
        return (self.name,)