#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pysnooper
from time import sleep
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains


@pysnooper.snoop()
class WebUiBaseLib:
    """
    selenium test operation library
    """
    def __init__(self, url, down_path='.'):
        options = webdriver.ChromeOptions()
        prefs = {
            'profile.default_content_settings.popups': 0,
            'download.default_directory': down_path
        }
        options.add_experimental_option('prefs', prefs)
        options.add_argument("blink-settings=imagesEnabled=false")
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-extensions")
        self.driver = webdriver.Chrome(chrome_options=options)
        self.driver.get(url)

    def click(self, element_by, element):
        """
        Click the button
        :param element_by:Element type
        :param element:Element
        :return:Boolean value
        """
        if not self.wait_element(element_by, element):
            return False
        flag = None
        try:
            if element_by == "id":
                self.driver.find_element_by_id(element).click()
            elif element_by == "xpath":
                self.driver.find_element_by_xpath(element).click()
            elif element_by == "class":
                self.driver.find_element_by_class_name(element).click()
            elif element_by == "link_text":
                self.driver.find_element_by_link_text(element).click()
            elif element_by == "partial_link_text":
                self.driver.find_element_by_partial_link_text(element).click()
            elif element_by == "name":
                self.driver.find_element_by_name(element).click()
            elif element_by == "tag":
                self.driver.find_element_by_tag_name(element).click()
            elif element_by == "css":
                self.driver.find_element_by_css_selector(element).click()
            flag = True
            sleep(0.5)
        except NoSuchElementException:
            flag = False
        return flag

    def context_click(self, element_by, element):
        """
        Click the button
        :param element_by:Element type
        :param element:Element
        :return:Boolean value
        """
        if not self.wait_element(element_by, element):
            return False
        flag = None
        try:
            if element_by == "id":
                element_obj = self.driver.find_element_by_id(element)
                ActionChains(self.driver).context_click(element_obj).click().perform()
            elif element_by == "xpath":
                element_obj = self.driver.find_element_by_xpath(element)
                ActionChains(self.driver).context_click(element_obj).click().perform()
            elif element_by == "class":
                element_obj = self.driver.find_element_by_class_name(element)
                ActionChains(self.driver).context_click(element_obj).click().perform()
            elif element_by == "link_text":
                element_obj = self.driver.find_element_by_link_text(element)
                ActionChains(self.driver).context_click(element_obj).click().perform()
            elif element_by == "partial_link_text":
                element_obj = self.driver.find_element_by_partial_link_text(element)
                ActionChains(self.driver).context_click(element_obj).click().perform()
            elif element_by == "name":
                element_obj = self.driver.find_element_by_name(element)
                ActionChains(self.driver).context_click(element_obj).click().perform()
            elif element_by == "tag":
                element_obj = self.driver.find_element_by_tag_name(element)
                ActionChains(self.driver).context_click(element_obj).click().perform()
            elif element_by == "css":
                element_obj = self.driver.find_element_by_css_selector(element)
                ActionChains(self.driver).context_click(element_obj).click().perform()
            flag = True
            sleep(0.5)
        except NoSuchElementException:
            flag = False
        return flag

    def get_element_text(self, element_by, element):
        """
        Get component attribute
        :param element_by:Element type
        :param element:Element
        :param attribute:Get attributes
        :return:Get information
        """
        if not self.wait_element(element_by, element):
            return False
        flag = None
        try:
            if element_by == "id":
                flag = self.driver.find_element_by_id(element).text
            elif element_by == "xpath":
                flag = self.driver.find_element_by_xpath(element).text
            elif element_by == "class":
                flag = self.driver.find_element_by_class_name(element).text
            elif element_by == "link_text":
                flag = self.driver.find_element_by_link_text(element).text
            elif element_by == "partial_link_text":
                flag = self.driver.find_element_by_partial_link_text(
                    element).text
            elif element_by == "name":
                flag = self.driver.find_element_by_name(element).text
            elif element_by == "tag":
                flag = self.driver.find_element_by_tag_name(element).text
            elif element_by == "css":
                flag = self.driver.find_element_by_css_selector(element).text
        except NoSuchElementException:
            flag = False
        return flag

    def send_element_content(self, element_by, element, content):
        """
        Text into the specified element
        :param element_by:Element type
        :param element:Element
        :param content:Text content
        :return:Boolean value
        """
        if not self.wait_element(element_by, element):
            return False
        flag = None
        try:
            if element_by == "id":
                self.driver.find_element_by_id(element).send_keys(content)
            elif element_by == "xpath":
                self.driver.find_element_by_xpath(element).send_keys(content)
            elif element_by == "class":
                self.driver.find_element_by_class_name(element).send_keys(
                    content)
            elif element_by == "link_text":
                self.driver.find_element_by_link_text(element).send_keys(
                    content)
            elif element_by == "partial_link_text":
                self.driver.find_element_by_partial_link_text(
                    element).send_keys(content)
            elif element_by == "name":
                self.driver.find_element_by_name(element).send_keys(content)
            elif element_by == "tag":
                self.driver.find_element_by_tag_name(element).send_keys(
                    content)
            elif element_by == "css":
                self.driver.find_element_by_css_selector(element).send_keys(
                    content)
            flag = True
        except NoSuchElementException:
            flag = False
        return flag

    def is_element(self, identify_by, element):
        """
        Determine whether elements exist
        :param identify_by:Element type
        :param element:Element
        :return: Boolean value
        """
        flag = None
        try:
            if identify_by == "id":
                self.driver.find_element_by_id(element)
            elif identify_by == "xpath":
                self.driver.find_element_by_xpath(element)
            elif identify_by == "class":
                self.driver.find_element_by_class_name(element)
            elif identify_by == "link_text":
                self.driver.find_element_by_link_text(element)
            elif identify_by == "partial_link_text":
                self.driver.find_element_by_partial_link_text(element)
            elif identify_by == "name":
                self.driver.find_element_by_name(element)
            elif identify_by == "tag":
                self.driver.find_element_by_tag_name(element)
            elif identify_by == "css":
                self.driver.find_element_by_css_selector(element)
            flag = True
        except NoSuchElementException:
            flag = False
        return flag

    def wait_element(self, element_by, element, time=60):
        """
        Wait for element to appear
        :param element_by:Element type
        :param element:Element name
        :param time: Actual waiting time = time * 10
        :return:Boolean value
        """
        for order in range(int(time)):
            sleep(1)
            if self.is_element(element_by, element):
                return True
        return False

    def quit_driver(self):
        """
        quit driver
        @return:
        """
        self.driver.quit()