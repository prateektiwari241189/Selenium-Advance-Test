import pytest
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException
import platform

class TestClass:

    @pytest.mark.parametrize("driver", ['test1', 'test2'], indirect=True)
    def test_assignment(self, driver):
        driver.get("https://www.lambdatest.com/")
        if platform.system() == "Darwin":
            try:
                allow_cookies = WebDriverWait(driver, 20).until(ec.visibility_of_element_located((By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll")))
                allow_cookies.click()
            except NoSuchElementException as e:
                pass
        explore_all_integrations = WebDriverWait(driver, 20).until(ec.visibility_of_element_located((By.LINK_TEXT, "Explore all Integrations")))
        driver.execute_script("arguments[0].scrollIntoView(false);", explore_all_integrations)
        actions = ActionChains(driver)
        actions.move_to_element(explore_all_integrations)
        if platform.system() == "Darwin":
            actions.key_down(Keys.COMMAND).click(explore_all_integrations).key_up(Keys.COMMAND).perform()
        else:
            actions.key_down(Keys.CONTROL).click(explore_all_integrations).key_up(Keys.CONTROL).perform()
        original_window = driver.current_window_handle
        assert WebDriverWait(driver, 20).until(ec.number_of_windows_to_be(2))
        all_windows = driver.window_handles
        print(all_windows)
        for window in all_windows:
            if window != original_window:
                driver.switch_to.window(window)

        assert driver.current_url == "https://www.lambdatest.com/integrations"

        codeless_automation = driver.find_element(By.XPATH,"(//a[text()='Codeless Automation'])[1]")
        codeless_automation.click()
        testing_link = WebDriverWait(driver, 20).until(ec.visibility_of_element_located((By.LINK_TEXT, "INTEGRATE TESTING WHIZ WITH LAMBDATEST")))
        driver.execute_script("arguments[0].scrollIntoView(false);", testing_link)
        testing_link.click()
        assert driver.title != "TestingWhiz Integration WithLambdaTest", "Title matched"

        driver.close()
        print(f"Total windows: {len(driver.window_handles)}")
        driver.switch_to.window(original_window)
        driver.get("https://www.lambdatest.com/blog/")
        community_link = WebDriverWait(driver, 20).until(ec.element_to_be_clickable((By.LINK_TEXT, "Community")))
        community_link.click()
        assert driver.current_url == "https://community.lambdatest.com/", "Title did not match"
