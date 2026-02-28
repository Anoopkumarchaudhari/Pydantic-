from pydantic import BaseModel,EmailStr,ValidationError,AnyUrl,Field,field_validator
from typing import List,Dict,Optional,Annotated
class Patient(BaseModel):
    # name:str=Field(min_length=3,max_length=50,description="Name of the patient")
    name:Annotated[str,Field(default=None,min_length=3,max_length=50,title="Name of the patient",description="Name length should be between 3 to 50 characters",examples=['Anoop','Kumar'])]
    age:int
    email:EmailStr
    weight:float
    married:bool 
    allergies:List[str]
    contact_details:Dict[str,str]

    @field_validator('email')
    @classmethod
    def email_validator(cls,value):
        valid_domain=['hdfc.com','icici.com']
        domain_name = value.split('@')[-1]
        if domain_name not in valid_domain:
            raise ValueError('Invalid email domain')
        return value
    @field_validator('name',mode='before')
    @classmethod
    def name_upper(cls,value):
        return value.upper()


def insert(patient:Patient):
        print(patient.name)
        print(patient.age)
        print(patient.weight)
        print(patient.married)
        print(patient.allergies)
        print(patient.contact_details)
        print(patient.email)
        print('insert into database')

patient_info={'name':'Anoop','age':'21','email':'abc@hdfc.com','weight':50.5,'married':False,'allergies':['pollen','dust'],
              'contact_details':{'phone':'1234567890'}}
patient=Patient(**patient_info)# validation-> type coercion-> field validation

insert(patient)