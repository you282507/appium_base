#!/usr/bin/env python3

import pytest

class TestE2ECase:
    def setup_class(self):
        pass

    def teardown_class(self):
        # self.check_all_results()
        pass

    def setup(self):
        pass

    def teardown(self):
        pass

    def test_case0_start_e2e(self, pad_ip, port):
        picking_controller = PickingController(pad_ip, port)
        get_battery_results = picking_controller.get_battery()
        if not get_battery_results:
            return False
        TestE2ECase.get_battery_results = get_battery_results
        start_localization_results = picking_controller.start_localization()
        if not start_localization_results:
            return False
        TestE2ECase.start_localization_results = start_localization_results
        to_binding_results = picking_controller.to_binding()
        if not to_binding_results:
            return False
        TestE2ECase.to_binding_results = to_binding_results
        picking_results = picking_controller.to_picking()
        if not picking_results:
            return False
        TestE2ECase.picking_results = picking_results
        re_to_picking_results = picking_controller.re_to_picking()
        if not re_to_picking_results:
            return False
        TestE2ECase.re_to_picking_results = re_to_picking_results
        to_packing_results = picking_controller.to_packing()
        if not to_packing_results:
            return False
        TestE2ECase.to_packing_results = to_packing_results
        re_to_standby_results = picking_controller.re_to_binding()
        if not re_to_standby_results:
            return False
        TestE2ECase.re_to_standby_results = re_to_standby_results
        cycle_test_results = picking_controller.cycle_test()
        if not cycle_test_results:
            return False
        TestE2ECase.cycle_test_results = cycle_test_results

    def test_case1_get_battery(self):
        assert TestE2ECase.get_battery_results

    def test_case2_start_localization(self):
        assert TestE2ECase.start_localization_results

    def test_case3_to_binding(self):
        assert TestE2ECase.to_binding_results

    def test_case4_to_picking(self):
        assert TestE2ECase.picking_results

    def test_case5_re_to_picking(self):
        assert TestE2ECase.re_to_picking_results

    def test_case6_to_packing(self):
        assert TestE2ECase.to_packing_results

    def test_case7_to_standby(self):
        assert TestE2ECase.re_to_standby_results

    def test_case8_cycle_test(self):
        assert TestE2ECase.cycle_test_results

    def test_check_all_results(self):
        if TestE2ECase.get_battery_results and \
                TestE2ECase.start_localization_results and \
                TestE2ECase.to_binding_results and \
                TestE2ECase.picking_results and \
                TestE2ECase.re_to_picking_results and \
                TestE2ECase.to_packing_results and \
                TestE2ECase.re_to_standby_results and \
                TestE2ECase.cycle_test_results:
            results = True
        else:
            results = False
        assert results


if __name__ == "__main__":
    pytest.main(["-s", "run_bronto_e2e_test.py", "--html=.report/bronto_e2e_test.html", "--self-contained-html"])
