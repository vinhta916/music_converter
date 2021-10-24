from fastapi import APIRouter

from .music_converter import music_converter

router = APIRouter()

router.include_router(music_converter.router, tags=["music_converter"])