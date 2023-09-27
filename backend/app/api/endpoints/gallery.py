from fastapi import APIRouter, Depends, status

from db.session import Session, get_db
from ..schemas import gallery as galery_schema
from db.models.gallery import Gallery 

gallery_router = APIRouter(prefix="/gallery", tags=["Gallery"])


@gallery_router.get("/", response_model=list[galery_schema.ShowGallery])
def get_all(
    db: Session = Depends(get_db),
):
    galleries = db.query(Gallery).all()
    return galleries

@gallery_router.get(f"/{id}", response_model= galery_schema.ShowGallery)
def get_by_id(
    id: int,
    db: Session = Depends(get_db),
):
    gallery = Gallery.get_gallery_by_id(id, db)
    return gallery

@gallery_router.post("/create", status_code=status.HTTP_201_CREATED)  
def create(
    request: galery_schema.GalleryBase,
    db: Session = Depends(get_db),
):
    new_gallery = Gallery.create_gallery(request, session=db)
    return {"success": True, "created_id:": new_gallery.id}

@gallery_router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)  # noqa: F821
def destroy(
    id: int,
    db: Session = Depends(get_db),
):
    Gallery.delete_gallery(id, db)
    return {"success": True, "deleted_id": id}

@gallery_router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)  
def update(
    id,
    request: galery_schema.GalleryBase,
    db: Session = Depends(get_db),
):
    Gallery.update_gallery(id, db, request)
    return "updated"