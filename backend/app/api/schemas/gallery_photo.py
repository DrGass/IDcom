from pydantic import BaseModel, ConfigDict


class GalleryBase(BaseModel):
    filename: str
    description: str
    sort: int
    filesize: int
    edit_data: str

    model_config = ConfigDict(from_attributes=True)


class ShowGalleryPhoto(GalleryBase):
    filename: str
    description: str
    filesize: int

    model_config = ConfigDict(from_attributes=True)
