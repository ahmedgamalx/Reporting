from fastapi import APIRouter
from .api import userRouter, reportRouter

router = APIRouter()

router.include_router(userRouter)
router.include_router(reportRouter)

