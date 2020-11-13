#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class AppUiBaseLib:
    def __init__(self, appium_port, **capabilities):
        remote_server_url = "http://127.0.0.1:" + str(appium_port) + "/wd/hub"
        self.driver = webdriver.Remote(remote_server_url, capabilities)

    def quit_driver(self):
        self.driver.quit()

    def find_element(self, element_by, element):
        if not self.is_element_present(element_by, element):
            return False
        if element_by == "id":
            element_obj = self.driver.find_element_by_id(element)
        elif element_by == "xpath":
            element_obj = self.driver.find_element_by_xpath(element)
        elif element_by == "class":
            element_obj = self.driver.find_element_by_class_name(element)
        elif element_by == "link_text":
            element_obj = self.driver.find_element_by_link_text(element)
        elif element_by == "partial_link_text":
            element_obj = self.driver.find_element_by_partial_link_text(element)
        elif element_by == "name":
            element_obj = self.driver.find_element_by_name(element)
        elif element_by == "tag_name":
            element_obj = self.driver.find_element_by_tag_name(element)
        elif element_by == "css_selector":
            element_obj = self.driver.find_element_by_css_selector(element)
        elif element_by == "accessibility_id":
            element_obj = self.driver.find_element_by_accessibility_id(element)
        elif element_by == "uiautomator":
            element_obj = self.driver.find_element_by_android_uiautomator(element)
        else:
            element_obj = False
        return element_obj

    def click_element(self, element_by, element):
        element_obj = self.find_element(element_by, element)
        if element_obj:
            element_obj.click()
            return True
        return False

    def get_element_attribute(self, element_by, element, attribute="text"):
        element_obj = self.find_element(element_by, element)
        if element_obj:
            return element_obj.get_attribute(attribute)
        return False

    def send_keys(self, element_by, element, command):
        element_obj = self.find_element(element_by, element)
        if element_obj:
            element_obj.send_keys(command)
            return True
        return False

    def is_element_present(self, element_by, element):
        try:
            self.driver.find_element(element_by, element)
        except Exception as e:
            print(e)
            return False
        else:
            return True

    def swipe(self):
        window_size = self.driver.get_window_size()
        width = window_size['width'] * 0.5
        original_height = window_size['height'] * 0.5
        target_height = window_size['height'] * 0.25
        self.driver.swipe(width, original_height, width, target_height, 500)

    def wait_element(self, element_by, element, timeout=10):
        msg = "Not Fond:" + element
        try:
            WebDriverWait(self.driver, timeout).\
                until(expected_conditions.presence_of_element_located((element_by, element)), msg)
        except Exception as e:
            print(e)
            return False
        else:
            return True

    def adb_shell(self, command, args, include_stderr=False):
        result = self.driver.execute_script('mobile: shell', {
            'command': command,
            'args': args,
            'includeStderr': include_stderr,
            'timeout': 5000
        })
        return result

