from behave import *
from behave.api.async_step import async_run_until_complete

from models.email_page import EmailPage


@then('Check that you are logged in')
@async_run_until_complete
async def check_email_page(context):
    email_page = EmailPage(context.page)
    await email_page.validate_email_page()
    print("STEP: Check that you are logged in")


@when('Logout from email')
@async_run_until_complete
async def email_logout(context):
    email_page = EmailPage(context.page)
    await email_page.click_avatar()
    await email_page.click_logout_button()
    print("STEP: Logout from email")


@when('Write a new email message')
@async_run_until_complete
async def create_email_message(context):
    email_page = EmailPage(context.page)
    await email_page.click_new_email()
    await email_page.fill_email_subject("Test Subject")
    await email_page.fill_email_body("The quick brown fox jumps over the lazy dog 1234567890 ´")
    print("STEP: Write a new email message")


@when('Send the message to {address}')
@async_run_until_complete
async def send_email(context, address: str):
    email_page = EmailPage(context.page)
    await email_page.fill_email_to(address)
    await email_page.click_send_email()
    print("STEP: Send the message to " + address)


@when('Add attachment to the email')
@async_run_until_complete
async def add_attachment_to_email(context):
    email_page = EmailPage(context.page)
    await email_page.select_file(context.page)
    print("STEP: Add attachment to the email")
