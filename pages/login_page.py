from playwright.sync_api import Page


class LoginPage:
    """A page object model class for the ProtonMail login page.

    Attributes
    ----------
    _page : Page
        The Playwright page object.
    _url : str
        The URL of the ProtonMail login page.
    _email_input : Locator
        Locator for the email or username input field.
    _password_input : Locator
        Locator for the password input field.
    _login_button : Locator
        Locator for the login button.
    _sign_in_heading : Locator
        Locator for sign in heading.

    """

    def __init__(self: "LoginPage", page: Page) -> None:
        """Initialize the LoginPage with the given Playwright page object.

        Parameters
        ----------
        page : Page
            The Playwright page object.

        """
        self._page = page
        self._url = "https://mail.proton.me/"
        self._email_input = self._page.get_by_label("Email or username")
        self._password_input = self._page.get_by_label("Password")
        self._login_button = self._page.get_by_role("button", name="Sign in")
        self._sign_in_heading = self._page.get_by_role("heading", name="Sign in")

    def navigate(self: "LoginPage") -> None:
        """Navigates to the ProtonMail login page."""
        self._page.goto(self._url)

    def enter_credentials(self: "LoginPage", *, email: str, password: str) -> None:
        """Enters the given email and password into the login form.

        Args:
        ----
        email : str
            The email or username to enter.
        password : str
            The password to enter.

        """
        self._email_input.fill(email)
        self._password_input.fill(password)

    def click_login(self: "LoginPage") -> None:
        """Clicks the login button to submit the login form."""
        self._login_button.click()

    def sign_in_heading_is_visible(self: "LoginPage") -> bool:
        """Check if the sign in heading is visible on the page.

        Returns
        -------
        bool
            True if the sign in heading is visible, False otherwise.

        """
        self._sign_in_heading.wait_for(state="visible")
        return self._sign_in_heading.is_visible()
