from pathlib import Path

from playwright.sync_api import Page


class ComposeMessageComponent:
    """A class to interact with the message composer component on a webpage using Playwright."""

    def __init__(self: "ComposeMessageComponent", page: Page) -> None:
        """Initialize the ComposeMessageComponent with a Playwright Page instance.

        Args:
        ----
            page (Page): The Playwright page object.

        """
        self._page = page

        self._composer_header = self._page.get_by_test_id("composer:header")
        self._to_button = self._page.get_by_test_id("composer:to-button")
        self._send_button = self._page.get_by_test_id("composer:send-button")
        self._add_recipients_button = self._page.get_by_test_id("composer:to-button")
        self._subject_input = self._page.get_by_test_id("composer:subject")
        self._body_input = self._page.frame_locator(
            '[data-testid="rooster-iframe"]',
        ).locator("#rooster-editor")
        self._attachments_input = self._page.locator(
            '//*[@data-testid="composer-attachments-button"]',
        )
        self._attachments_saved_label = self._page.get_by_test_id(
            "composer:footer",
        ).locator('//span[contains(text(), "Saved")]')

    def click_on_send_button(self: "ComposeMessageComponent") -> None:
        """Clicks the send button in the message composer."""
        self._send_button.click()

    def send_button_is_visible(self: "ComposeMessageComponent") -> bool:
        """Check if the send button is visible.

        Returns
        -------
            bool: True if the send button is visible, False otherwise.

        """
        self._send_button.wait_for(state="visible")
        return self._send_button.is_visible()

    def click_on_add_recipients(self: "ComposeMessageComponent") -> None:
        """Clicks the button to add recipients in the message composer."""
        self._add_recipients_button.click()

    def find_recipient(self: "ComposeMessageComponent", *, contact: str) -> bool:
        """Check if a recipient is in the recipient list.

        Args:
        ----
            contact (str): The contact to search for.

        Returns:
        -------
            bool: True if the recipient is found, False otherwise.

        """
        locator = self._page.locator(
            f'//*[@data-testid="composer-addresses-item-label" and contains(text(), "{contact}")]',
        )
        locator.wait_for(state="visible")
        return locator.is_visible()

    def set_subject(self: "ComposeMessageComponent", *, subject: str) -> None:
        """Set the subject of the message.

        Args:
        ----
            subject (str): The subject text.

        """
        self._subject_input.fill(subject)

    def set_body(self: "ComposeMessageComponent", *, body: str) -> None:
        """Set the body of the message.

        Args:
        ----
            body (str): The body text.

        """
        self._body_input.fill(body)

    def add_attachment(self: "ComposeMessageComponent", *, path_to_file: Path) -> None:
        """Add an attachment to the message.

        Args:
        ----
            path_to_file (Path): The path to the file to attach.

        """
        self._attachments_input.set_input_files(path_to_file)

    def attachments_saved_label_is_visible(self: "ComposeMessageComponent") -> bool:
        """Check if the attachments saved label is visible.

        Returns
        -------
            bool: True if the attachments saved label is visible, False otherwise.

        """
        self._attachments_saved_label.wait_for(state="visible")
        return self._attachments_saved_label.is_visible()
