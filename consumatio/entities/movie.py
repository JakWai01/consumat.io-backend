import uuid
import dataclasses

@dataclasses.dataclass
class Movie():
   code: uuid.UUID
   title: str 
   year: int
   regisseur: str 
   rating: float 

   @classmethod 
   def from_dict(self, dict):
       return self(**dict)
 
   def to_dict(self):
       return dataclasses.asdict(self)