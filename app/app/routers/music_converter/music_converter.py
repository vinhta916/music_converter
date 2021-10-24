from fastapi import Depends, APIRouter, File, UploadFile, HTTPException, Body

router = APIRouter()

@router.get('/music_files')
async def getFiles():
    print('getting files')