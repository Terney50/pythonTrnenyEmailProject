import os

from playwright.async_api import Page, expect

from models.base_page import BasePage


class EmailPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.avatar = page.locator("[id='badge']")
        self.logoutButton = page.get_by_role("link", name="Odhlásit se")
        self.emailLogo = page.locator("[id='logo']")
        self.newEmailButton = page.get_by_role("link", name="Napsat e-mail")
        self.emailList = page.locator("[id='list']")
        self.emailToField = page.get_by_placeholder("Komu…")
        self.emailSubjectField = page.get_by_placeholder("Předmět…")
        self.emailTextField = page.locator('//body[1]/section[1]/div[2]/div[2]/div[1]')
        self.emailSendButton = page.locator('//body[1]/section[1]/div[3]/button[3]')
        self.emailAttachButton = page.locator('//body[1]/section[1]/div[2]/dl[1]/div[5]/button[1]')

    async def click_avatar(self):
        expect(self.avatar).to_be_visible()
        await self.avatar.click()
        print("I clicked on the avatar")

    async def click_logout_button(self):
        expect(self.logoutButton).to_be_visible()
        await self.logoutButton.click()
        print("I clicked on the logout button")

    async def validate_email_page(self):
        expect(self.emailLogo).to_be_visible()
        expect(self.newEmailButton).to_be_visible()
        expect(self.emailList).to_be_visible()
        print("Validated email page")

    async def click_new_email(self):
        await self.newEmailButton.click()
        print("I clicked on a new email button")

    async def fill_email_to(self, emailto: str):
        expect(self.emailToField).to_be_editable()
        await self.emailToField.fill(emailto)
        print("I fill the email address field: " + emailto)

    async def fill_email_subject(self, subject: str):
        expect(self.emailSubjectField).to_be_editable()
        await self.emailSubjectField.fill(subject)
        print("I fill the email subject field: " + subject)

    async def fill_email_body(self, body: str):
        expect(self.emailTextField).to_be_editable()
        await self.emailTextField.fill(body)
        print("I fill the email body: " + body)

    async def click_send_email(self):
        expect(self.emailSendButton).to_be_visible()
        await self.emailSendButton.click()
        print("I clicked on send email button")

    async def select_file(self, page: Page):
        expect(self.emailAttachButton).to_be_visible()

        current_working_dir = os.getcwd()
        print("Working dir: " + current_working_dir)
        file_path = os.path.join(current_working_dir, "files\\customTextFile.txt")
        print("Current file_path: " + file_path)

        async with page.expect_file_chooser() as fc_info:
            await self.emailAttachButton.click()
        file_chooser = await fc_info.value
        await file_chooser.set_files(file_path)
        print("File was selected")

        await page.wait_for_timeout(2000)
