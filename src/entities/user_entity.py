from dataclasses import dataclass


@dataclass
class UserEntity:
    id: int
    first_name: str
    last_name: str
    age: int

    def __repr__(self):
        return f"User [id={self.id}, first_name={self.first_name}]"
