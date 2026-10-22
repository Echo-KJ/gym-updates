Project Name : Gym Enquiry System.
Purpose      : In next 30 days we are going to understand how system works.
Features     : simple Lead Enquiry page, database note connected yet.
Techno       : HTML, CSS and JS
Usage(l)     : Download the files. Then
Howo we can start Backend:
Let's review exactly how we started the backend and frontend for your Gym Enquiry System on Linux Mint.

Remember, they are two separate programs running on your laptop. The frontend is what you see in the browser; the backend receives and processes the enquiries.

## 1. How we started the backend

We used FastAPI + Python + Uvicorn.

Backend — FastAPI

Folder: `gym-enquiry`

File: `main.py`

Step 1. Open the terminal and enter your project folder.

```
cd ~/Updates/gym-enquiry
```

Step 2. Activate your Python virtual environment.

```
source .venv/bin/activate
```

Step 3. Start the backend server.

```
python -m uvicorn main:app --reload
```

What the command means

- `python -m uvicorn` runs Uvicorn using Python.
- `main` refers to `main.py`.
- `app` refers to the FastAPI application inside that file.
- `--reload` restarts the development server when you change the code.

Step 4. The backend listens at:

`http://127.0.0.1:8000`

You can check that the backend is working by opening:

- Health check: `http://127.0.0.1:8000/health`
- API testing page: `http://127.0.0.1:8000/docs`

Keep this terminal open while testing.

## 2. How we started the frontend

Our frontend uses HTML + CSS + JavaScript.

Frontend — Gym enquiry form

Files: `index.html`, CSS, and JavaScript

Step 1. Open a second terminal. Don't stop the backend terminal.

Step 2. Navigate to the folder containing your `index.html` file. For example, if your frontend is in a folder named `frontend` inside the project:

```
cd ~/Updates/gym-enquiry/frontend
```

Use the actual folder path where your HTML file is saved.

Step 3. Start a simple frontend web server.

```
python3 -m http.server 5500
```

Step 4. Open Firefox and visit:

`http://127.0.0.1:5500/index.html`

Your gym enquiry form should appear.

## 3. How the two servers work together

Frontend server

Port 5500 · HTML, CSS, JavaScript

You fill the form and click Send Enquiry

JavaScript `fetch()`

POST `http://127.0.0.1:8000/leads`

Backend server

Port 8000 · FastAPI validates the enquiry

Response to the browser

“Enquiry received” or an error message

## 4. The commands to remember

| Purpose                      | Command                               |
| ---------------------------- | ------------------------------------- |
| Activate backend environment | `source .venv/bin/activate`           |
| Start backend                | `python -m uvicorn main:app --reload` |
| Start frontend server        | `python3 -m http.server 5500`         |
| Open frontend                | `http://127.0.0.1:5500/index.html`    |
| Check backend                | `http://127.0.0.1:8000/health`        |

Important: `127.0.0.1` means your own laptop. Both servers run locally, and you need two terminals because each server keeps running while you test.

### Quick understanding check

Why did we use two separate terminals?

A. Because the frontend and backend are separate servers, and both need to keep running.

B. Because Python cannot run two different files.

C. Because the frontend must be stored in RAM.

Check answer

               
