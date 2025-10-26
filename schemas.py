from pydantic import BaseModel

class URLBase(BaseModel):
    original_url:str

class URLCreate(URLBase):
    pass

class URl(URLBase):
    id:int
    short_code:str

    class Config:
        from_attributes = True