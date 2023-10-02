from fastapi import APIRouter, Depends, status
from fastapi_pagination import Page, paginate
# from ..schemas.helpers import paginate
# from fastapi_pagination.ext.sqlalchemy import paginate

from ..schemas import gallery as gallery_schema
from db.session import Session, get_db
from db.models.gallery import Gallery

gallery_router = APIRouter(prefix="/gallery", tags=["Gallery"])



@gallery_router.get(
    "/", status_code=status.HTTP_200_OK, response_model=Page[gallery_schema.ShowGallery]
)
def get_all(
    db: Session = Depends(get_db),
    
) -> Page[gallery_schema.ShowGallery]:

    all_galleries = db.query(Gallery).all()

    return paginate(all_galleries)
 


@gallery_router.get("/{id}", response_model=gallery_schema.ShowGallery)
def get_by_id(
    id: int,
    db: Session = Depends(get_db),
):
    gallery = Gallery.get_gallery_by_id(id, db)

    return gallery


@gallery_router.post("/create", status_code=status.HTTP_201_CREATED)
def create(
    request: gallery_schema.CreateGallery,
    db: Session = Depends(get_db),
):
    new_gallery = Gallery.create_gallery(request, db)
    return {"success": True, "created_id:": new_gallery.id}


@gallery_router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def destroy(
    id: int,
    db: Session = Depends(get_db),
):
    Gallery.delete_gallery(id, db)
    return {"success": True, "deleted_id": id}


@gallery_router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update(
    id,
    request: gallery_schema.CreateGallery,
    db: Session = Depends(get_db),
):
    Gallery.update_gallery(id, db, request)
    return "updated"
