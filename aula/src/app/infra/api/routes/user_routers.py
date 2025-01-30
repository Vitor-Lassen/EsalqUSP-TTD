from fastapi import APIRouter, HTTPException, status
from applicantion.user.create_user_use_case import CreateUserUseCase, CreateUserRequest, CreateUserResponse
from infra.user.in_memory_use_repositoy import InMemoryRepository

router = APIRouter(prefix="/users")

repository = InMemoryRepository()

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=CreateUserResponse)
def create_user( request: CreateUserRequest):
    try:
        usercase = CreateUserUseCase(repository=repository)
        response = usercase.execute(request)
        return response
    except Exception as e: 
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))