from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from ledger import register_user, transfer_funds, get_balance

app = FastAPI()

class UserCreate(BaseModel):
    username: str
    password_hash: str
    email: str

class TransferRequest(BaseModel):
    from_account_id: int
    to_account_id: int
    amount: float
    memo: str = None

@app.post("/users")
async def create_user(user: UserCreate):
    try:
        user_id = register_user(user.username, user.password_hash, user.email)
        return {"user_id": user_id, "message": "User registered successfully"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")

@app.post("/transfers")
async def perform_transfer(transfer: TransferRequest):
    try:
        success = transfer_funds(
            transfer.from_account_id, 
            transfer.to_account_id, 
            transfer.amount, 
            transfer.memo
        )
        return {"message": "Transfer successful"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except RuntimeError as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/accounts/{account_id}/balance")
async def get_account_balance(account_id: int):
    try:
        balance = get_balance(account_id)
        return {"account_id": account_id, "balance": balance}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal server error")
