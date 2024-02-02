from playwright.async_api import Page, expect

from models.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.username = page.locator("[id='login-username']")
        self.password = page.locator("[id='login-password']")
        self.submit_continue_button = page.get_by_role("button", name="Pokračovat")
        self.submit_login_button = page.get_by_role("button", name="Přihlásit se")

    async def navigate(self):
        await self.page.goto("https://email.seznam.cz/", timeout=5000)

    async def fill_username(self, text):
        expect(self.username).to_be_visible()
        await self.username.fill(text)
        print("Username entered")

    async def fill_password(self, text):
        expect(self.password).to_be_visible()
        await self.password.fill(text)
        print("Password entered")

    async def submit_continue(self):
        expect(self.submit_continue_button).to_be_visible()
        await self.submit_continue_button.click()
        print("Clicked on continue button")

    async def submit_login(self):
        expect(self.submit_login_button).to_be_visible()
        await self.submit_login_button.click()
        print("Clicked on login button")

    async def is_error_message_displayed(self):
        return await self.page.wait_for_selector(".error-text", state="visible", timeout=5000)
