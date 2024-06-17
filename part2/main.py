from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from PIL import Image
import io
import random

app = FastAPI()


@app.post("/image")
async def process_image(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        image = Image.open(io.BytesIO(contents))


        employee_id = ''.join([str(random.randint(0, 9)) for _ in range(3)])

        return {"employee_id": employee_id}
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

    

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=9000)
