from pydantic import BaseModel, ConfigDict
from ..schemas.gallery_photo import ShowGalleryPhoto
from .helpers import CustomPagination


class GalleryBase(BaseModel):
    site_id: int
    name: str
    description: str
    sort: int
    private: bool
    edit_date: str
    photos_count: int

    model_config = ConfigDict(from_attributes=True)


class ShowGallery(GalleryBase):
    name: str
    description: str
    photos_count: int
    photos: list[ShowGalleryPhoto] = []

    model_config = ConfigDict(from_attributes=True)


class GalleryPagination(CustomPagination):
    records: list[ShowGallery] = []
