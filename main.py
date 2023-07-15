from fastapi import FastAPI

from services import patient_services as ps

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World Ubuntu 22"}

@app.get("/patient/get-patient/{id}")
async def get_patient(id):
    return ps.get_patient(id)

