from ..session import Base
from fastapi import HTTPException, status
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import Session


class GalleryPhoto(Base):
    __tablename__ = ("gallery_photo",)
    id: int = Column(Integer, primary_key=True, autoincrement=True)
    filename: str = Column(String)
    description: str = Column(String)
    sort: int = Column(Integer)
    filesize: int = Column(Integer)
    edit_data: str = Column(String)

    @staticmethod
    def get_all(db: Session, gallery_id: int):
        gallery_photos = db.query(GalleryPhoto).filter(GalleryPhoto.gallery_id == gallery_id).all()
        return gallery_photos

    @staticmethod
    def get_one(db: Session, photo_id: int):
        photo = db.query(GalleryPhoto).filter(GalleryPhoto.id == photo_id).first()
        if not photo:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Photo not found")
        return photo

    @staticmethod
    def create_photo(photo, db: Session):
        db.add(photo)
        db.commit()
        db.refresh(photo)
        return photo

    @staticmethod
    def update_photo(db: Session, photo_id: int, photo):
        photo = db.query(GalleryPhoto).filter(GalleryPhoto.id == photo_id).first()
        if not photo:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Photo not found")
        photo.filename = photo.filename
        photo.description = photo.description
        photo.sort = photo.sort
        photo.filesize = photo.filesize
        photo.edit_data = photo.edit_data
        db.commit()
        db.refresh(photo)
        return photo

    @staticmethod
    def delete_photo(db: Session, photo_id: int):
        photo = db.query(GalleryPhoto).filter(GalleryPhoto.id == photo_id).first()
        if not photo:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Photo not found")
        db.delete(photo)
        db.commit()
        return photo
    
    #write hello world with this class properties