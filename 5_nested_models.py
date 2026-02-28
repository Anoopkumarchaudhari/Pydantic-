from pydantic import BaseModel,EmailStr,computed_field
from typing import List,Dict,Optional,Annotated
class Address(BaseModel):
    
    city:str
    state:str
    pin:str
class Patient(BaseModel):
    # name:str=Field(min_length=3,max_length=50,description="Name of the patient")
    name:str  
    gender:str 
    age:int  
    address:Address

def insert(patient:Patient):
        print(patient.name)
        print(patient.age)
        print(patient.address.city)
        print(patient.address.state)
        print(patient.address.pin)
        print('insert into database')

adress = {'city':'Betiah','state':'Bihar','pin':'845438'}
adress1 = Address(**adress)
patient_info={'name':'Anoop','age':21,'gender':'M','address':adress1}

patient=Patient(**patient_info)# validation-> type coercion-> field validation

insert(patient)