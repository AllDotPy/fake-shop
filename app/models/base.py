import datetime
from typing import Dict, Any, TypeVar, Type, Union
from dataclasses import dataclass, asdict, fields
import json

T = TypeVar('T', bound='BaseModel')


####
##      BASE MODEL CLASS
#####
@dataclass
class BaseModel:
    ''' Base class for all models. '''
    
    def to_json(self) -> Dict[str, Any]:
        """
        Converts model fields into a dictionary.
        """
        return {
            k: str(v) if isinstance(v, datetime.date) else v
            for k, v in asdict(self).items()
            if v is not None
        }
    
    def to_json_string(self) -> str:
        """
        Converts model fields into a JSON string.
        """
        return json.dumps(self.to_json())
    
    @classmethod
    def from_json(cls: Type[T], json_dict: Dict[str, Any]) -> T:
        """
        Loads model from a dictionary.
        """
        # Create a new instance
        instance = cls.__new__(cls)

        field_types = {f.name: f.type for f in fields(cls)}
        for k, v in json_dict.items():
            if k in field_types:
                field_type = field_types[k]
                if hasattr(field_type, '__origin__') and field_type.__origin__ is Union:
                    # Handle Optional types
                    field_type = field_type.__args__[0]

                if isinstance(v, field_type):
                    setattr(instance, k, v)

                elif field_type == datetime.date and isinstance(v, str):
                    setattr(instance, k, datetime.date.fromisoformat(v))

                else:
                    setattr(instance, k, field_type(v))
            
        # Ensure __init__ is called if there are any initialization steps
        # if hasattr(instance, '__init__'):
        #     instance.__init__()

        return instance
    
    @classmethod
    def from_json_string(cls: Type[T], json_str: str) -> T:
        """
        Loads model from a JSON string.
        """
        json_dict = json.loads(json_str)
        return cls.from_json(json_dict)
    
    def __str__(self):
        return f"{self.__class__.__name__} {self.to_json()}"
    
    def __repr__(self):
        return self.__str__()
