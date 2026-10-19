from app.main import app


def test_health_returns_ok(client):
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_every_route_uses_the_api_v1_prefix():
    # ADR-025: all routes live under /api/v1.
    paths = list(app.openapi()["paths"])
    assert paths, "no API routes registered"
    assert all(p.startswith("/api/v1/") for p in paths), paths


def test_cors_allows_the_angular_dev_server(client):
    response = client.options(
        "/api/v1/health",
        headers={"Origin": "http://localhost:4200", "Access-Control-Request-Method": "GET"},
    )
    assert response.headers.get("access-control-allow-origin") == "http://localhost:4200"
