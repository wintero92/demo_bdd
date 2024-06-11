from playwright.sync_api import Page


class InboxPage:
    """A page object model class for the ProtonMail inbox page.

    Attributes
    ----------
        page (Page): The Playwright page object.
        _inbox_heading (Locator): Locator for the inbox heading element.
        _user_dropdown_menu (Locator): Locator for the user dropdown menu.
        _new_message_button (Locator): Locator for the new message button.

    """

    def __init__(self: "InboxPage", page: Page) -> None:
        """Initialize the InboxPage with the given Playwright page object.

        Args:
        ----
            page (Page): The Playwright page object.

        """
        self._page = page
        self._inbox_heading = self._page.get_by_role("heading", name="Inbox")
        self._user_dropdown_menu = self._page.get_by_test_id("heading:userdropdown")
        self._new_message_button = self._page.get_by_test_id("sidebar:compose")

    def inbox_heading_is_visible(self: "InboxPage") -> bool:
        """Check if the inbox heading is visible on the page.

        Returns
        -------
            bool: True if the inbox heading is visible, False otherwise.

        """
        self._inbox_heading.wait_for(state="visible")
        return self._inbox_heading.is_visible()

    def open_user_dropdown_menu(self: "InboxPage") -> None:
        """Clicks to open the user dropdown menu."""
        self._user_dropdown_menu.click()

    def open_new_message_component(self: "InboxPage") -> None:
        """Clicks to open the new message component."""
        self._new_message_button.click()
