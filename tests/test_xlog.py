import json

import pytest
import platform
import yaml


def test_1(testdir, tmp_path):
    testdir.makepyfile(
        """
        import pytest
        import platform

       
        @pytest.mark.case('case_1')
        def test_simple_case():
            assert True
        
        
        @pytest.mark.case('case_2', conf={'initiator_platform': platform.platform()}, test_type='sanity')
        def test_case_dynamic_options():
            assert False

        def test_no_decorator():
            assert True
            
        @pytest.mark.case('case_3')
        @pytest.mark.parametrize("test_input,expected", [(8, 8), (5, 6)])
        def test_with_param(test_input, expected):
            assert test_input == expected

        @pytest.mark.case('case_4')
        @pytest.mark.skip('Issue BUG-123456')
        def test_skipped_case():
            assert True

        def params():
            return {
                'case_10': [1, 1],
                'case_11': [2, 3]
            }
        
        @pytest.mark.case(params())
        @pytest.mark.parametrize("test_input,expected", list(params().values()))
        def test_case_id_from_param(test_input,expected):
            assert test_input == expected
    """
    )

    result_file = "{}/log.yaml".format(tmp_path)

    result = testdir.runpytest(
        "-v",
        "--xlog", result_file,
        "--xopt", "product_version=1.5",
        "--xopt", "environment.stand.type=virtual"
    )

    assert result.ret == pytest.ExitCode.TESTS_FAILED

    yaml_data = yaml.load(open(result_file), Loader=yaml.BaseLoader)
    assert len(yaml_data.keys()) == 5
    assert yaml_data['case_2'][0]['conf']['initiator_platform'] == platform.platform()
