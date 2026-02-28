from pydantic import BaseModel,EmailStr,model_validator
from typing import List,Dict,Optional,Annotated
class Patient(BaseModel):
    # name:str=Field(min_length=3,max_length=50,description="Name of the patient")
    name:str   
    age:int
    email:EmailStr
    weight:float
    married:bool 
    allergies:List[str]
    contact_details:Dict[str,str]
    
    @model_validator(mode='after')
    def validate_emergency_contact(cls,model):
        if model.age > 60 and 'emergency' not in model.contact_details:
            raise ValueError('Emergency contact is required for age above 60')
        return model
def insert(patient:Patient):
        print(patient.name)
        print(patient.age)
        print(patient.weight)
        print(patient.married)
        print(patient.allergies)
        print(patient.contact_details)
        print(patient.email)
        print('insert into database')

patient_info={'name':'Anoop','age':50,'email':'abc@hdfc.com','weight':61.5,'married':False,'allergies':['pollen','dust'],
              'contact_details':{'phone':'1234567890','emergency':'9876543210'}}
patient=Patient(**patient_info)# validation-> type coercion-> field validation

insert(patient)