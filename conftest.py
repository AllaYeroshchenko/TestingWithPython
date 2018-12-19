from fixture.application import Application
import pytest

fixture = None

@pytest.fixture(scope="session")
def app(request):
    global fixture
    fixture=Application()
    fixture.session.login("Admin", "secret")
    def fin():
        fixture.session.logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture