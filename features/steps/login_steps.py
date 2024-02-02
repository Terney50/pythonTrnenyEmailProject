from behave import *
from behave.api.async_step import async_run_until_complete

from models.login_page import LoginPage


@given('Open browser')
@async_run_until_complete
async def open_url(context):
    login_page = LoginPage(context.page)
    await login_page.navigate()
    print("STEP: Open browser")


@when('Log in to email')
@async_run_until_complete
async def fill_login_page_field(context):
    login_page = LoginPage(context.page)
    await login_page.fill_username("trneny.lukas.test@email.cz")
    await login_page.submit_continue()
    await login_page.fill_password("abcd1234@")
    await login_page.submit_login()
    print("STEP: Log in to email")
