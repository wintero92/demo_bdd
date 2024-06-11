from playwright.sync_api import Page


class InsertContactsComponent:
    """A class to interact with the insert contacts component on a webpage using Playwright."""

    def __init__(self: "InsertContactsComponent", page: Page) -> None:
        """Initialize the InsertContactsComponent with a Playwright Page instance.

        Args:
        ----
            page (Page): The Playwright page object.

        """
        self._page = page
        self._insert_contacts_heading = self._page.get_by_role(
            "heading",
            name="Insert contacts",
        )
        self._insert_contacts_button = self._page.get_by_test_id(
            "modal:contactlist:submit",
        )

    def insert_heading_is_visible(self: "InsertContactsComponent") -> bool:
        """Check if the insert contacts heading is visible.

        Returns
        -------
            bool: True if the insert contacts heading is visible, False otherwise.

        """
        self._insert_contacts_heading.wait_for(state="visible")
        return self._insert_contacts_heading.is_visible()

    def check_contact(self: "InsertContactsComponent", *, contact: str) -> None:
        """Check the checkbox for a specified contact.

        Args:
        ----
            contact (str): The contact to check.

        """
        self._page.locator(
            f'//label[contains(@data-testid, "contact-checkbox-{contact}")]',
        ).check()

    def click_on_insert_contacts_button(self: "InsertContactsComponent") -> None:
        """Clicks the button to insert the selected contacts."""
        self._insert_contacts_button.click()
