from fastapi import APIRouter


router = APIRouter()

list_kons=[]

@router.get("/view_all/")
async def view_all():
    return list_kons

@router.post("/add_kons/")
async def add_kons():
    kons=input("Напишите конспект:")
    list_kons.append(kons)
    return kons

@router.get("/kons_ind/")
async def kons_ind():
    index=input("Введите индекс:")
    return list_kons[index]

@router.get("/delete_all/")
async def delete_all():
    list_kons.clear()
