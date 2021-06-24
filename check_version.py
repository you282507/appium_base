#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import argparse
from library import get_ota_version


class CheckVersion:
    def __init__(self, robot_ip, username="syrius", passwd="syrius"):
        self.current_version = int(get_ota_version(robot_ip, username, passwd))

    def compare_version(self, version):
        diff = int(version) - self.current_version
        if diff < 0:
            return False
        return True

    def check_version(self, version):
        if str(self.current_version) == str(version):
            return True
        return False


def run_check(robot_ip, version, mode):
    check_obj = CheckVersion(robot_ip)
    if mode == "compare":
        check_result = check_obj.compare_version(version)
    elif mode == "check":
        check_result = check_obj.check_version(version)
    else:
        check_result = False
    return check_result


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--ip', dest='robot_ip')
    parser.add_argument('--version', dest='version')
    parser.add_argument('--mode', dest='mode')
    remaining_args = sys.argv[:1]
    args = parser.parse_args()
    result = run_check(args.robot_ip, args.version, args.mode)
    if not result:
        sys.exit(1)
