from fastapi import APIRouter
from fastapi import status


router = APIRouter()


@router.get("", status_code=status.HTTP_200_OK)
def health_check():
    """
    Check service health status.

    Returns 'ok' if the server is running and ready to process requests.
    """
    return {"status": "ok"}
