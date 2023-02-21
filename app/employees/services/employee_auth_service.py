import time
from typing import Dict

import jwt

from app.config import settings

EMPLOYEE_SECRET = settings.EMPLOYEE_SECRET
JWT_ALGORITHM = settings.ALGORITHM


def signJWT(employee_id: str, role: str) -> Dict[str, str]:
    payload = {
        "employee_id": employee_id,
        "role": role,
        "expires": time.time() + 1200
    }
    token = jwt.encode(payload, EMPLOYEE_SECRET, algorithm=JWT_ALGORITHM)

    return {"access_token": token}


def decodeJWT(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, EMPLOYEE_SECRET, algorithms=[JWT_ALGORITHM])
        return decoded_token if decoded_token["expires"] >= time.time() else None
    except:
        return {}
