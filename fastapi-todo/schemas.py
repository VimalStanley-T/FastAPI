from pydantic import BaseModel
# Intha class enga iruinthu kedaikum na pydantic package la tha
# kedaikum Validation, JSON request ta python object ta matha, python objects sa JSON
# Response sa mathurathu intha marri services lam kedaikum. So install package (pip 
# install pydantic)
class TodoBase(BaseModel):
    # (title: str ) Intha marri kuduthuitta api request send panrapo kuripa POST request
    # send pannum bothu title field kandippa irukanum nu solrom. 
    title: str 
    description: str | None = None # Default value
    completed: bool = False # Default value
    
class TodoCreate(TodoBase):
    pass

class Todo(TodoBase): # Response send panna
    id: int # title, description, completed, la send pannuvom koodavea id yavum send panvom
    class Config: # Nested class
        # orm_mode = True # JSON data va convert panni response send pannrathuku.
        # todo apdingra ORM model la iruinthu eduthuittu vanthu koduka porom
        # models.py la irukula atha solrom athula kedaikarathu ellam python Objects ok.
        from_attributes = True # orm_mode = True as from_attributes = True reindum same than 