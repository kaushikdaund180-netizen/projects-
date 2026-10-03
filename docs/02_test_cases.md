# Test Case Matrix

| ID | Module | Scenario | Type | Expected Result | Test function |
|---|---|---|---|---|---|
| TC01 | Login | Valid credentials (admin, tester) | Positive | Redirect to dashboard, welcome shown | test_login.py::test_valid_login |
| TC02 | Login | Wrong password | Negative | "Invalid credentials" | test_invalid_login |
| TC03 | Login | Unknown user | Negative | "Invalid credentials" | test_invalid_login |
| TC04 | Login | Empty username & password | Boundary | "Username and password are required" | test_invalid_login |
| TC05 | Login | Empty password only | Boundary | Required-fields error | test_invalid_login |
| TC06 | Login | SQL injection string | Security | Login rejected | test_invalid_login |
| TC07 | Session | Access dashboard without login | Security | Redirect to /login | test_dashboard_requires_authentication |
| TC08 | Session | Logout then open dashboard | Security | Redirect to /login | test_logout_ends_session |
| TC09 | Tasks | Add item | Positive | Item listed | test_add_item |
| TC10 | Tasks | Add blank item | Negative | "Item cannot be empty" | test_add_empty_item_shows_message |
| TC11 | Tasks | Delete item | Positive | List shrinks by one | test_delete_item |
| TC12 | Tasks | Script tag as item | Security | Rendered as text, not executed | test_special_characters_are_escaped |
| TC13 | API | GET /api/health | Positive | 200 {"status":"ok"} | test_health |
| TC14 | API | POST /api/items valid | Positive | 201 + item | test_create_and_list_item |
| TC15 | API | POST invalid body (3 variants) | Negative | 400 + error | test_create_item_validation |
| TC16 | API | DELETE twice | Negative | 204 then 404 | test_delete_item_and_404_on_repeat |
