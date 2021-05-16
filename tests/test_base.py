import pytest


@pytest.mark.usefixtures("init_driver")
class TestBase:
    def test_title(self):
        assert "Verify Title" in self.driver.title
