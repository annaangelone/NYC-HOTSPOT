from dataclasses import dataclass
@dataclass
class Location:
    location: str
    latitude: float
    longitude: float


    def __str__(self):
        return self.location

    def __hash__(self):
        return hash(self.location)