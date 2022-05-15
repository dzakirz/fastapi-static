from uuid import UUID
from fastapi import FastAPI, HTTPException
from models import User, UserUpdateRequest
from static_db import Database

app = FastAPI()

db = Database.static

@app.get('/')
async def root():
  return 'Welcome To static CRUD fastAPI by DzakiRZ'
  
@app.get('/api/users')
async def fetch_users():
  return db

@app.post('/api/users')
async def register_user(user: User):
  db.append(user)
  return {"id": user.id}

@app.put('/api/users/{user_id}')
async def update_user(user_update: UserUpdateRequest, user_id: UUID):
  for user in db:
    if user_update.first_name is not None:
      user.first_name = user_update.first_name
    if user_update.last_name is not None:
      user.last_name = user_update.last_name
    if user_update.middle_name is not None:
      user.middle_name = user_update.middle_name
    if user_update.roles is not None:
      user.roles = user_update.roles
    return f"userid: {user.id} updated"
  raise HTTPException(
    status_code = 404,
    detail = f"{user_id} does not exists"
  )

@app.delete('/api/users/{user_id}')
async def delete_user(user_id: UUID):
  for user in db:
    if user.id == user_id:
      db.remove(user)
      return f"{user.first_name} deleted"
  raise HTTPException(
    status_code = 404,
    detail = f"{user_id} does not exists"
  )