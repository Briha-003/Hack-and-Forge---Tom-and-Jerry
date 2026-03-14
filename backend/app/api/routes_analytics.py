from fastapi import APIRouter

router = APIRouter()

@router.get("/summary")

def analytics():

return{
"queries":120,
"ambiguities":35,
"languages":["English","Hindi"]
}
