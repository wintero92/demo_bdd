from collections.abc import Generator
from typing import Any

import pytest
from playwright.sync_api import Browser, BrowserContext, Page, sync_playwright

from components.compose_message import ComposeMessageComponent
from components.insert_contacts_component import InsertContactsComponent
from components.notification_component import NotificationComponent
from components.user_dropdown import UserDropdownComponent
from pages.inbox_page import InboxPage
from pages.login_page import LoginPage


@pytest.fixture(scope="session")
def fixture_browser() -> Generator[Browser, Any, Any]:
    """Pytest fixture to set up a Playwright Browser instance.

    This fixture runs once per test session.

    Yields
    ------
        Generator[Browser, Any, Any]: The Playwright Browser instance.

    """
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        yield browser
        browser.close()


@pytest.fixture()
def fixture_browser_context(
    fixture_browser: Browser,
) -> Generator[BrowserContext, Any, Any]:
    """Pytest fixture to set up a Playwright BrowserContext instance.

    This fixture runs once per test function.

    Args:
    ----
        fixture_browser (Browser): The Playwright Browser instance.

    Yields:
    ------
        Generator[BrowserContext, Any, Any]: The Playwright BrowserContext instance.

    """
    context = fixture_browser.new_context(
        device_scale_factor=1.0,
    )

    context.tracing.start(name="debug", screenshots=True, snapshots=True, sources=True)
    yield context
    context.tracing.stop(path="debug.zip")
    context.close()


@pytest.fixture()
def fixture_page(fixture_browser_context: BrowserContext) -> Generator[Page, Any, Any]:
    """Pytest fixture to set up a Playwright Page instance.

    This fixture runs once per test function.

    Args:
    ----
        fixture_browser_context (BrowserContext): The Playwright BrowserContext instance.

    Yields:
    ------
        Generator[Page, Any, Any]: The Playwright Page instance.

    """
    page = fixture_browser_context.new_page()
    yield page
    page.close()


@pytest.fixture()
def fixture_login_page(fixture_page: Page) -> LoginPage:
    """Pytest fixture to create a LoginPage instance.

    Args:
    ----
        fixture_page (Page): The Playwright Page instance.

    Returns:
    -------
        LoginPage: The LoginPage instance.

    """
    return LoginPage(fixture_page)


@pytest.fixture()
def fixture_inbox_page(fixture_page: Page) -> InboxPage:
    """Pytest fixture to create an InboxPage instance.

    Args:
    ----
        fixture_page (Page): The Playwright Page instance.

    Returns:
    -------
        InboxPage: The InboxPage instance.

    """
    return InboxPage(fixture_page)


@pytest.fixture()
def fixture_user_dropdown_component(fixture_page: Page) -> UserDropdownComponent:
    """Pytest fixture to create a UserDropdownComponent instance.

    Args:
    ----
        fixture_page (Page): The Playwright Page instance.

    Returns:
    -------
        UserDropdownComponent: The UserDropdownComponent instance.

    """
    return UserDropdownComponent(fixture_page)


@pytest.fixture()
def fixture_compose_message_component(fixture_page: Page) -> ComposeMessageComponent:
    """Pytest fixture to create a ComposeMessageComponent instance.

    Args:
    ----
        fixture_page (Page): The Playwright Page instance.

    Returns:
    -------
        ComposeMessageComponent: The ComposeMessageComponent instance.

    """
    return ComposeMessageComponent(fixture_page)


@pytest.fixture()
def fixture_insert_contacts_component(fixture_page: Page) -> InsertContactsComponent:
    """Pytest fixture to create an InsertContactsComponent instance.

    Args:
    ----
        fixture_page (Page): The Playwright Page instance.

    Returns:
    -------
        InsertContactsComponent: The InsertContactsComponent instance.

    """
    return InsertContactsComponent(fixture_page)


@pytest.fixture()
def fixture_notification_component(fixture_page: Page) -> NotificationComponent:
    """Pytest fixture to create a NotificationComponent instance.

    Args:
    ----
        fixture_page (Page): The Playwright Page instance.

    Returns:
    -------
        NotificationComponent: The NotificationComponent instance.

    """
    return NotificationComponent(fixture_page)
