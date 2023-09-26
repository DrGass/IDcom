from pydantic import BaseModel, ConfigDict
from ..schemas.gallery_photo import ShowGalleryPhoto

class GalleryBase(BaseModel):
    site_id: int
    name: str
    description: str
    sort: int
    private: bool
    edit_date: str
    photos_count: int

    model_config = ConfigDict(orm_mode=True)

class ShowGallery(GalleryBase):
    name: str
    description : str
    photos_count : int
    photos: list[ShowGalleryPhoto] = []
    
    model_config = ConfigDict(orm_mode=True)
