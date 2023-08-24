from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from chatbot import chat

# Initialize FastAPI app
app = FastAPI()

# Initialize Jinja2 templates
templates = Jinja2Templates(directory="templates")

# Placeholder function for the chat response (replace this with your actual chat function)

# Endpoint for rendering the initial HTML page
@app.get("/", response_class=HTMLResponse)
async def render(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Endpoint for handling form submissions
@app.post("/", response_class=HTMLResponse)
async def getinput(request: Request, message: str = Form(...)):
    response = chat(message)  # Call the chat function to get a response
    return templates.TemplateResponse("index.html", {"request": request, "response": response})
