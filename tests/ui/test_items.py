import pytest

pytestmark = pytest.mark.ui


def test_dashboard_starts_with_seeded_tasks(dashboard):
    items = dashboard.items()
    assert "Check login with wrong password" in items
    assert "Test add and delete task" in items


@pytest.mark.smoke
def test_add_item(dashboard):
    dashboard.add_item("Write test plan")
    assert "Write test plan" in dashboard.items()


def test_add_empty_item(dashboard):
    dashboard.add_item("   ")
    assert dashboard.message() == "Item cannot be empty"


def test_delete_item(dashboard):
    dashboard.add_item("Temp item")
    before = len(dashboard.items())
    dashboard.delete_first()
    assert len(dashboard.items()) == before - 1


def test_script_text_is_not_executed(dashboard):
    text = "<script>window.__xss=1</script>"
    dashboard.add_item(text)
    assert text in dashboard.items()                         # shown as plain text
    assert dashboard.page.evaluate("window.__xss") is None   # script did not run
