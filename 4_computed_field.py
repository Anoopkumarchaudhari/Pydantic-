from pydantic import BaseModel,EmailStr,computed_field
from typing import List,Dict,Optional,Annotated
class Patient(BaseModel):
    # name:str=Field(min_length=3,max_length=50,description="Name of the patient")
    name:str   
    age:int  
    email:EmailStr
    weight:float #kg
    height:float #meters
    married:bool 
    allergies:List[str]
    contact_details:Dict[str,str]
    
    @computed_field
    @property
    def bmi(self)->float:
        return round(self.weight/(self.height**2),2)

def insert(patient:Patient):
        print(patient.name)
        print(patient.age)
        print(patient.weight)
        print(patient.married)
        print(patient.allergies)
        print(patient.contact_details)
        print(patient.email)
        print(patient.bmi)
        print('insert into database')

patient_info={'name':'Anoop','age':50,'email':'abc@hdfc.com','weight':61.5,'height':1.63,'married':False,'allergies':['pollen','dust'],
              'contact_details':{'phone':'1234567890','emergency':'9876543210'}}
patient=Patient(**patient_info)# validation-> type coercion-> field validation

insert(patient)