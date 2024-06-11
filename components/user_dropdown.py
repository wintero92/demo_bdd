from playwright.sync_api import Page


class UserDropdownComponent:
    """A component class for the user dropdown menu in ProtonMail.

    Attributes
    ----------
    _page : Page
        The Playwright page object.
    _logout_button : Locator
        Locator for the logout button.

    """

    def __init__(self: "UserDropdownComponent", page: Page) -> None:
        """Initialize the UserDropdownComponent with the given Playwright page object.

        Parameters
        ----------
        page : Page
            The Playwright page object.

        """
        self._page = page
        self._logout_button = self._page.get_by_test_id("userdropdown:button:logout")

    def click_logout(self: "UserDropdownComponent") -> None:
        """Clicks the logout button in the user dropdown menu."""
        self._logout_button.click()
