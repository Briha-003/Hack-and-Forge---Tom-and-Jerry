from fastapi import APIRouter

router = APIRouter()

vocabulary=[]

@router.post("/add")

def add_vocab(data:dict):

vocabulary.append(data)

return{"status":"added"}
