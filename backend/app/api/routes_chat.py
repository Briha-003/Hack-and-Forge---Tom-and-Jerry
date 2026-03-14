from fastapi import APIRouter
from services.ambiguity_detector import detect_ambiguity
from services.llm_service import generate_response

router = APIRouter()

@router.post("/message")
async def chat(data:dict):

message = data["message"]

ambiguous = detect_ambiguity(message)

if ambiguous:

return{
"status":"clarification_needed",
"terms":ambiguous
}

response = generate_response(message)

return{
"status":"success",
"response":response
}
