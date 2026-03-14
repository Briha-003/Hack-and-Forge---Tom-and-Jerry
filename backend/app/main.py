from fastapi import FastAPI
from api.routes_chat import router as chat_router
from api.routes_vocab import router as vocab_router
from api.routes_analytics import router as analytics_router

app = FastAPI(
title="Context Sense AI",
description="Enterprise Context Aware AI"
)

app.include_router(chat_router,prefix="/chat")
app.include_router(vocab_router,prefix="/vocab")
app.include_router(analytics_router,prefix="/analytics")
