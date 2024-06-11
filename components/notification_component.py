from playwright.sync_api import Page


class NotificationComponent:
    """A class to interact with the notification component on a webpage using Playwright."""

    def __init__(self: "NotificationComponent", page: Page) -> None:
        """Initialize the NotificationComponent with a Playwright Page instance.

        Args:
        ----
            page (Page): The Playwright page object.

        """
        self._page = page
        self._message_sent_notification = self._page.get_by_text("Message sent.")

    def message_sent_notification_is_visible(self: "NotificationComponent") -> bool:
        """Check if the "Message sent" notification is visible.

        Returns
        -------
            bool: True if the "Message sent" notification is visible, False otherwise.

        """
        self._message_sent_notification.wait_for(state="visible")
        return self._message_sent_notification.is_visible()
