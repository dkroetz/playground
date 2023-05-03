from fastapi import APIRouter
from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel

router = APIRouter()


class Authentication(BaseModel):
    username: str = None
    password: str = None
    token: str = None


class Play(BaseModel):
    message: str = None


def check_token(token):
    if token == "token":
        return True
    else:
        return False


def check_user_pass(username, password):
    if username == "user" and password == "pass":
        return True
    else:
        return False


def check_if_logged_in(auth: Authentication):
    # if token is set, then user is logged in
    # else check if username and password are correct
    if auth.token:
        if check_token(auth.token):
            return True
        else:
            # if token is invalid, check if username and password are correct
            if auth.username and auth.password:
                if check_user_pass(auth.username, auth.password):
                    return True
                else:
                    raise HTTPException(
                        status_code=status.HTTP_401_UNAUTHORIZED,
                        detail="Invalid credentials",
                        headers={"WWW-Authenticate": "Bearer"},
                    )
            else:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Token Invalid and no valid credentials provided, either username and password or token must be set",
                    headers={"WWW-Authenticate": "Bearer"},
                )
    else:
        # if token is not set, check if username and password are correct
        if auth.username and auth.password:
            if check_user_pass(auth.username, auth.password):
                return True
            else:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Invalid credentials",
                    headers={"WWW-Authenticate": "Bearer"},
                )
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="No credentials provided, either username and password or token must be set",
                headers={"WWW-Authenticate": "Bearer"},
            )


@router.post("/play/one")
async def play_one(play: Play, logged_in: bool = Depends(check_if_logged_in)):
    return {"message": play.message, "logged_in": logged_in}
