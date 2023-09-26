from pydantic import BaseModel, Field
from pydantic.types import Literal
from datetime import datetime

class InputModel(BaseModel):
    name:str = Field(alias='name', description='Name of Passenger')
    sex:Literal['female', 'male'] = Field(alias='sex', description='Gender of passenger')  # noqa: F821
    age:int = Field(alias='age', ge=0, le=100)
    fare:float = Field(alias='fare', description='Passenger Fare', ge=0.0)
    cabin:str = Field(alias='cabin', description='cabin number of passenger')
    embarked:str = Field(alias='embarked', description='Place in which the passenger started their journey')
    pclass:int = Field(alias='pclass', description='Class of passenger ticket', ge=1, le=3 )
    sibsp:int = Field(alias='sibsp', description='Number of siblings on board', ge=0)
    parch:int = Field(alias='parch', description='Number of parents on board', ge=0)

    model_config = {
    "json_schema_extra": {
        "examples": [
            {
                "name": "Foo",
                "sex": "male",
                "age": 35,
                "fare": 302,
                "cabin": "C1",
                "embarked": "belfast",
                'pclass': 3,
                'sibsp':0,
                'parch':0
            }
        ]
    }
}
    
class OutputModel(BaseModel):
    titanic_model_version: str
    timestamp: datetime
    prediction: float