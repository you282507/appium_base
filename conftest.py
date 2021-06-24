# -*- coding:utf-8 -*-
import pytest


def pytest_addoption(parser):
    parser.addoption("--pad_ip",
                     action="store",
                     default="None",
                     help="Pad ip!")
    parser.addoption("--port",
                     action="store",
                     default="None",
                     help="Appium port")
    parser.addoption("--job_no",
                     action="store",
                     default="None",
                     help="Jenkins build number")
    parser.addoption("--tag",
                     action="store",
                     default="False",
                     help="Tagging Manager")
    parser.addoption("--is_test",
                     action="store",
                     default="True",
                     help="Debug mode")
    parser.addoption("--version_no",
                     action="store",
                     default="None",
                     help="Syrius_all version number")


@pytest.fixture
def pad_ip(request):
    return request.config.getoption("--pad_ip")


@pytest.fixture
def port(request):
    return request.config.getoption("--port")


@pytest.fixture
def job_no(request):
    return request.config.getoption("--job_no")


@pytest.fixture
def tag(request):
    return request.config.getoption("--tag")


@pytest.fixture
def is_test(request):
    return request.config.getoption("--is_test")


@pytest.fixture
def ver_no(request):
    return request.config.getoption("--version_no")
