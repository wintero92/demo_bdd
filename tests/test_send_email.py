from pathlib import Path

from pytest_bdd import given, scenarios, then, when

from components.compose_message import ComposeMessageComponent
from components.insert_contacts_component import InsertContactsComponent
from components.notification_component import NotificationComponent
from config.dynamic_test_data import DynamicTestData
from pages.inbox_page import InboxPage
from pages.login_page import LoginPage

TEST_DATA: DynamicTestData = DynamicTestData()

scenarios("features/send_email.feature")


@given("the user is logged into the email")
def log_in_to_email(fixture_login_page: LoginPage) -> None:
    """Log in to the email account."""
    fixture_login_page.navigate()
    fixture_login_page.enter_credentials(
        email=TEST_DATA.email_login,
        password=TEST_DATA.email_password.get_secret_value(),
    )
    fixture_login_page.click_login()


@when("the user clicks on the new message button")
def open_new_message(fixture_inbox_page: InboxPage) -> None:
    """Open the new message component."""
    fixture_inbox_page.open_new_message_component()


@then("the user should see new message component")
def verify_new_message_component(
    fixture_compose_message_component: ComposeMessageComponent,
) -> None:
    """Verify the new message component is visible."""
    assert fixture_compose_message_component.send_button_is_visible()


@when("the user clicks on insert contacts button")
def open_insert_contacts(
    fixture_compose_message_component: ComposeMessageComponent,
) -> None:
    """Open the insert contacts component."""
    fixture_compose_message_component.click_on_add_recipients()


@then("the user should see the insert contacts component")
def verify_insert_contacts_component(
    fixture_insert_contacts_component: InsertContactsComponent,
) -> None:
    """Verify the insert contacts component is visible."""
    assert fixture_insert_contacts_component.insert_heading_is_visible()


@when("the user selects a contact from the contact list")
def select_contact(
    fixture_insert_contacts_component: InsertContactsComponent,
) -> None:
    """Select a contact from the contact list."""
    fixture_insert_contacts_component.check_contact(contact=TEST_DATA.contant_name)


@when("the user clicks on insert contacts")
def insert_contacts(
    fixture_insert_contacts_component: InsertContactsComponent,
) -> None:
    """Insert the selected contacts."""
    fixture_insert_contacts_component.click_on_insert_contacts_button()


@then("the user should see the selected contact in the recipients input")
def verify_recipients(
    fixture_compose_message_component: ComposeMessageComponent,
) -> None:
    """Verify the selected contact appears in the recipients input."""
    assert fixture_compose_message_component.find_recipient(
        contact=TEST_DATA.contant_name,
    )


@when("the user enters the email subject and body")
def enter_email_subject_and_body(
    fixture_compose_message_component: ComposeMessageComponent,
) -> None:
    """Enter the email subject and body."""
    fixture_compose_message_component.set_subject(subject="demo subject")
    fixture_compose_message_component.set_body(body="demo body")


@when("the user clicks on the send button")
def send_email(fixture_compose_message_component: ComposeMessageComponent) -> None:
    """Send the email."""
    fixture_compose_message_component.click_on_send_button()


@then("the email should be sent successfully")
def verify_send_notification(
    fixture_notification_component: NotificationComponent,
) -> None:
    """Verify the send notification is visible."""
    assert fixture_notification_component.message_sent_notification_is_visible()


@when("the user attaches the attachment")
def attach_attachment(
    fixture_compose_message_component: ComposeMessageComponent,
) -> None:
    """Attach a file to the email."""
    fixture_compose_message_component.add_attachment(
        path_to_file=Path("data/attachment.txt"),
    )


@then("the user should see the saved label in the footer")
def verify_attachments_are_saved(
    fixture_compose_message_component: ComposeMessageComponent,
) -> None:
    """Verify the attachments saved label is visible."""
    assert fixture_compose_message_component.attachments_saved_label_is_visible()
