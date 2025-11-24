from fastapi import FastAPI
from .routers import unit1, unit2, unit3, unit4, unit5

app = FastAPI(version="1.0.0")

app.include_router(unit1.router, prefix="/unit1", tags=["unit1"])
app.include_router(unit2.router, prefix="/unit2", tags=["unit2"])
app.include_router(unit3.router, prefix="/unit3", tags=["unit3"])
app.include_router(unit4.router, prefix="/unit4", tags=["unit4"])
app.include_router(unit5.router, prefix="/unit5", tags=["unit5"])

@app.get("/", tags=["root"])
def root():
    return {"message": "tari masi no piko"}