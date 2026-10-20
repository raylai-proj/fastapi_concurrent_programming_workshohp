import pytest
from httpx import ASGITransport, AsyncClient

from app.main import create_app

@pytest.mark.asyncio
async def test_health() -> None:
    """Verify the health enpoint returns a successful status response."""
    app = create_app()

    # Declare an httpx asynchronous client to send async web request. 
    async with AsyncClient(
        transport= ASGITransport(app=app),
        base_url= "http://test",
    ) as client:
        response = await client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}