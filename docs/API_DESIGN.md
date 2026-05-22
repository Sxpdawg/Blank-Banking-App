# API Design: Banking App REST Service

## Overview
Transforming the existing CLI logic into a production-ready REST API using **FastAPI**.

## API Endpoints (v1)

### Users
- `POST /users`: Register a new user.

### Accounts
- `POST /accounts`: Create a new account for an existing user.
- `GET /accounts/{id}/balance`: Get current balance.

### Transactions
- `POST /transfers`: Perform a fund transfer.
- `GET /accounts/{id}/history`: Get transaction history.

## Architectural Changes
- **Service Layer:** Refactor `ledger.py` into distinct functions that interact with the DB, ensuring they are independent of CLI logic.
- **API Layer:** New module `api/` that handles HTTP requests and calls the service layer.
- **Validation:** Use Pydantic models for request body validation.

## Next Steps
1. Create a new branch: `feat/rest-api-layer`.
2. Refactor `ledger.py` for cleaner separation of concerns.
3. Install `fastapi` and `uvicorn`.
4. Implement the first endpoint (`POST /users`).
