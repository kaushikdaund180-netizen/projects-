import pytest
import requests

pytestmark = pytest.mark.api


@pytest.fixture
def api(base_url):
    return base_url + "/api"


@pytest.mark.smoke
def test_health(api):
    r = requests.get(api + "/health", timeout=5)
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}


def test_create_and_list_item(api):
    r = requests.post(api + "/items", json={"name": "api-item"}, timeout=5)
    assert r.status_code == 201
    assert r.json()["name"] == "api-item"

    names = [i["name"] for i in requests.get(api + "/items", timeout=5).json()]
    assert "api-item" in names


@pytest.mark.negative
@pytest.mark.parametrize("body", [{}, {"name": ""}, {"name": "   "}])
def test_create_item_wrong_input(api, body):
    r = requests.post(api + "/items", json=body, timeout=5)
    assert r.status_code == 400
    assert "error" in r.json()


def test_delete_item_twice(api):
    item = requests.post(api + "/items", json={"name": "to-delete"}, timeout=5).json()
    assert requests.delete(api + "/items/%d" % item["id"], timeout=5).status_code == 204
    # second time the item is already gone
    assert requests.delete(api + "/items/%d" % item["id"], timeout=5).status_code == 404
