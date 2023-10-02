from ..session import Base
from fastapi import HTTPException, status
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import Session


class Gallery(Base):
    __tablename__ = "gallery"
    id: int = Column(Integer, primary_key=True, autoincrement=True)
    site_id: int = Column(Integer)
    name: str = Column(String)
    description: str = Column(String)
    sort: int = Column(Integer)
    private: bool = Column(Boolean)
    edit_date: str = Column(String)
    photos_count: int = Column(Integer)

    @staticmethod
    def get_all(db: Session, site_id: int):
        galleries = db.query(Gallery).filter(Gallery.site_id == site_id).all()
        return galleries

    @staticmethod
    def get_gallery_by_id(db: Session, gallery_id: int):
        gallery = db.query(Gallery).filter(Gallery.id == gallery_id).first()
        if not gallery:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Gallery not found"
            )
        return gallery

    @staticmethod
    def create_gallery(request, db: Session):
        gallery = Gallery(**request.model_dump())
        db.add(gallery)
        db.commit()
        db.refresh(gallery)
        return gallery

    @staticmethod
    def update_gallery(db: Session, gallery_id: int, new_gallery):
        gallery = db.query(Gallery).filter(Gallery.id == gallery_id).first()
        if not gallery:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Gallery not found"
            )
        gallery.name = new_gallery.name
        gallery.description = new_gallery.description
        gallery.sort = new_gallery.sort
        gallery.private = new_gallery.private
        gallery.edit_date = new_gallery.edit_date
        db.commit()
        db.refresh(gallery)
        return gallery

    @staticmethod
    def delete_gallery(db: Session, gallery_id: int):
        gallery = db.query(Gallery).filter(Gallery.id == gallery_id).first()
        if not gallery:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Gallery not found"
            )
        db.delete(gallery)
        db.commit()
        return gallery
