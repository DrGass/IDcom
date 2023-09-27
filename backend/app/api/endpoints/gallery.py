from fastapi import APIRouter, Depends

from backend.app.db.session import Session, get_db
from ..schemas import gallery as galery_schema
from ...db.models import gallery as gallery_model


gallery_router = APIRouter(prefix="/gallery", tags=["Gallery"])

@gallery_router.get("/",response_model=list[galery_schema.ShowGallery])
def get_all(
    db: Session = Depends(get_db),
):
    galleries = db.query(gallery_model.Gallery).all()
    return galleries

# @router.get("/", response_model=list[patient_schema.ShowPatient])
# def get_all(
#     db: Session = Depends(get_db),
# ):
#     patients = db.query(patient_model.Patient).all()
#     return patients


# @router.get(
#     "/{id}",
#     status_code=200,
#     response_model=patient_schema.ShowPatient,
# )
# def get_by_id(
#     id: int,
#     db: Session = Depends(get_db),
# ):
#     patient = patient_model.Patient.get_patient_by_id(id, db)
#     return patient


# @router.post("/", status_code=status.HTTP_201_CREATED)
# def create(
#     request: patient_schema.NewPatient,
#     db: Session = Depends(get_db),
# ):
#     new_patient = patient_model.Patient.create_patient(request, session=db)
#     return {"success": True, "created_id:": new_patient.id}


# @router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
# def destroy(
#     id: int,
#     db: Session = Depends(get_db),
# ):
#     patient_model.Patient.delete_patient(id, db)
#     return {"success": True, "deleted_id": id}


# @router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
# def update(
#     id,
#     request: patient_schema.NewPatient,
#     db: Session = Depends(get_db),
# ):
#     patient_model.Patient.update_patient(id, db, request)
#     return "updated"
