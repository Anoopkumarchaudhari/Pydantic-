from pydantic import BaseModel,EmailStr,ValidationError,AnyUrl,Field
from typing import List,Dict,Optional,Annotated
class Patient(BaseModel):
    # name:str=Field(min_length=3,max_length=50,description="Name of the patient")
    name:Annotated[str,Field(default=None,min_length=3,max_length=50,title="Name of the patient",description="Name length should be between 3 to 50 characters",examples=['Anoop','Kumar'])]
    age:int
    email:EmailStr
    url:Optional[AnyUrl]=None
    weight:Annotated[float,Field(gt=0,strict=True,description="Weight should be greater than 0")]
    married:bool = False
    allergies:Optional[List[str]]=None
    contact_details:Dict[str,str]
def insert(patient:Patient):
        print(patient.name)
        print(patient.age)
        print(patient.weight)
        print(patient.married)
        print(patient.allergies)
        print(patient.contact_details)
        print(patient.email)
        print(patient.url)
        print('insert into database')

patient_info={'name':'Anoop','age':'21','email':'abc@gmail.com','weight':50.5,'url':'http://google.com','married':False,'allergies':['pollen','dust'],
              'contact_details':{'phone':'1234567890'}}
patient=Patient(**patient_info)

insert(patient)