from datetime import datetime

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root_endpoint():
    return {
        'message': 'App is working',
        'time': datetime.now()
    }


@app.get("/etc/mnt_info.csv")
async def download_csv():
    filename = "mnt_info.csv"
    file_path = f"./app/{filename}"
    return FileResponse(file_path, media_type="text/csv", filename=filename)


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=80,
        reload=True,
        workers=4
    )
