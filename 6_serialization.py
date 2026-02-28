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
        # print(patient.name)
        # print(patient.age)
        # print(patient.address.city)
        # print(patient.address.state)
        # print(patient.address.pin)
        print('insert into database')

adress = {'city':'Betiah','state':'Bihar','pin':'845438'}
adress1 = Address(**adress)
patient_info={'name':'Anoop','age':21,'gender':'M','address':adress1}

patient=Patient(**patient_info)# validation-> type coercion-> field validation

insert(patient)
print('-----------------------------------------------')
temp= patient.model_dump()
print(temp)
print(type(temp))

print('-----------------------------------------------')

temp2= patient.model_dump_json()
print(temp2)
print(type(temp2))
print('-----------------------------------------------')

temp3 = patient.model_dump(include=['name'])
print(temp3)
print(type(temp3))  
print('-----------------------------------------------')

temp4 = patient.model_dump(exclude=['age'])
print(temp4)    
print(type(temp4))

print('-----------------------------------------------')
temp5 = patient.model_dump(exclude={'address':{'city','state'}})
print(temp5) 
print(type(temp5))

print('-----------------------------------------------')
temp6 = patient.model_dump(exclude_unset=True)
print(temp6)