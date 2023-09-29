from pydantic import BaseModel, ConfigDict
from ..schemas.gallery_photo import ShowGalleryPhoto
from .helpers import CustomPagination

class GalleryBase(BaseModel):
    name: str
    description: str

    model_config = ConfigDict(from_attributes=True)

class CreateGallery(GalleryBase):
    site_id: int
    sort: int
    private: bool
    edit_date: str
    photos_count: int

    model_config = ConfigDict(from_attributes=True)


class ShowGallery(GalleryBase):
    photos_count: int
    photos: list[ShowGalleryPhoto] = []

    model_config = ConfigDict(from_attributes=True)


class GalleryPagination(CustomPagination):
    records: list[ShowGallery] = []
