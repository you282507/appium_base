from subprocess import Popen, PIPE
from os import system
from time import sleep


def is_chinese(uchar):
    """
    Determine if a unicode is a Chinese character
    :param uchar: unicode
    :return: Boolean value
    """
    if u'\u4e00' <= uchar <= u'\u9fa5':
        return True
    return False


def start_activity(package_activity, devices):
    """
    Start the program manually
    :param package_activity:Package name + activity
    :return:None
    """
    command = 'adb -s ' + devices + ' shell am start ' + package_activity
    system(command)


def force_stop(package, devices):
    """
    Forced stop procedure
    :param package: Package Name
    :return:None
    """
    for package_name in package:
        command = 'adb -s ' + devices + ' shell am force-stop ' + package_name
        system(command)


def adb_input(text, devices):
    """
    Call adb to enter text
    :param text:String
    :return:None
    """
    command = 'adb -s ' + devices + ' shell input text \"%s\"' % text
    system(command)
