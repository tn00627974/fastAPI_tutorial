import pytest
from fastapi.testclient import TestClient
from main import app
from database import init_db, clear_db

client = TestClient(app)


@pytest.fixture(scope="module", autouse=True)
def setup_database():
    # 初始化資料庫
    init_db()
    yield
    # 清理資料庫（如果需要）
    # clear_db()


def test_create_product():
    response = client.post(
        "/products/",
        json={"name": "Test Product", "description": "Test Description", "price": 100},
    )
    assert response.status_code == 200
    assert response.json()["name"] == "Test Product"
    assert response.json()["description"] == "Test Description"
    assert response.json()["price"] == 100


def test_read_products():
    response = client.get("/products/")
    assert response.status_code == 200
    assert len(response.json()) > 0


def test_read_product():
    # 先創建一個產品
    response = client.post(
        "/products/",
        json={
            "name": "Another Product",
            "description": "Another Description",
            "price": 200,
        },
    )
    assert response.status_code == 200
    product_id = response.json()["id"]

    # 查詢該產品
    response = client.get(f"/products/{product_id}")
    assert response.status_code == 200
    assert response.json()["name"] == "Another Product"
    assert response.json()["description"] == "Another Description"
    assert response.json()["price"] == 200


def test_update_product():
    # 先創建一個產品
    response = client.post(
        "/products/",
        json={
            "name": "Update Product",
            "description": "Update Description",
            "price": 300,
        },
    )
    assert response.status_code == 200
    product_id = response.json()["id"]

    # 更新該產品
    response = client.put(
        f"/products/{product_id}",
        json={
            "name": "Updated Product",
            "description": "Updated Description",
            "price": 400,
        },
    )
    assert response.status_code == 200
    assert response.json()["name"] == "Updated Product"
    assert response.json()["description"] == "Updated Description"
    assert response.json()["price"] == 400


def test_delete_product():
    # 先創建一個產品
    response = client.post(
        "/products/",
        json={
            "name": "Delete Product",
            "description": "Delete Description",
            "price": 500,
        },
    )
    assert response.status_code == 200
    product_id = response.json()["id"]

    # 刪除該產品
    response = client.delete(f"/products/{product_id}")
    assert response.status_code == 200
    assert response.json()["message"] == f"刪除Delete Product"
