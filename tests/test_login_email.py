from pytest_bdd import given, scenarios, then, when

from components.user_dropdown import UserDropdownComponent
from config.dynamic_test_data import DynamicTestData
from pages.inbox_page import InboxPage
from pages.login_page import LoginPage

TEST_DATA: DynamicTestData = DynamicTestData()


# S106 Possible hardcoded password assigned to argument

scenarios("features/email_login.feature")


@given("the user navigates to the email login page")
def navigate_to_login_page(fixture_login_page: LoginPage) -> None:
    """Navigates to the email login page.

    Parameters
    ----------
    fixture_login_page : LoginPage
        The LoginPage instance to interact with the login page.

    """
    fixture_login_page.navigate()


@when("the user enters valid credentials")
def enter_credentials(fixture_login_page: LoginPage) -> None:
    """Enters valid login credentials.

    Parameters
    ----------
    fixture_login_page : LoginPage
        The LoginPage instance to interact with the login form.

    """
    fixture_login_page.enter_credentials(
        email=TEST_DATA.email_login,
        password=TEST_DATA.email_password.get_secret_value(),
    )


@when("the user clicks on the login button")
def click_login_button(fixture_login_page: LoginPage) -> None:
    """Clicks the login button.

    Parameters
    ----------
    fixture_login_page : LoginPage
        The LoginPage instance to interact with the login form.

    """
    fixture_login_page.click_login()


@then("the user should see the inbox")
def verify_inbox(fixture_inbox_page: InboxPage) -> None:
    """Verify that the inbox is visible.

    Parameters
    ----------
    fixture_inbox_page : InboxPage
        The InboxPage instance to verify the inbox page.

    """
    assert fixture_inbox_page.inbox_heading_is_visible()


@when("the user opens the user dropdown menu")
def open_user_dropdown_menu(fixture_inbox_page: InboxPage) -> None:
    """Open the user dropdown menu.

    Parameters
    ----------
    fixture_inbox_page : InboxPage
        The InboxPage instance to interact with the user dropdown menu.

    """
    fixture_inbox_page.open_user_dropdown_menu()


@when("the user clicks on the logout button")
def click_on_logout_in_user_dropdown_menu(
    fixture_user_dropdown_component: UserDropdownComponent,
) -> None:
    """Clicks the logout button in the user dropdown menu.

    Parameters
    ----------
    fixture_user_dropdown_component : UserDropdownComponent
        The UserDropdownComponent instance to interact with the user dropdown menu.

    """
    fixture_user_dropdown_component.click_logout()


@then("the user should be redirected to the login page")
def verify_login_page(fixture_login_page: LoginPage) -> None:
    """Verify that the user is redirected to the login page.

    Parameters
    ----------
    fixture_login_page : LoginPage
        The LoginPage instance to verify the login page.

    """
    assert fixture_login_page.sign_in_heading_is_visible()
