import pytest
import allure
@allure.title("Test Authentication")
@allure.description("This test attempts to log into the website using a login and a password. Fails if any error happens.\n\nNote that this test does not test 2-Factor Authentication.")
@allure.tag("NewUI", "Essentials", "Authentication")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("owner", "Madhu Kan")
@allure.link("https://dev.example.com/", name="Website")
@allure.issue("AUTH-123")
@allure.testcase("TMS-456")

def test_authentication():
    ...
@pytest.mark.reg
def test_add():
    assert 1+1 == 2
@pytest.mark.reg
def test_sub():
    assert 1-1 == 0

@pytest.mark.smoke
def test_adding():
        assert 3 + 1 == 4


