# Pytest-xlog

Pytest plugin to create YAML formatted reports where the root keys are decorators associated with test functions.  


## Install

```
pip install pytest-xlog
```

## Usage

Suppose you have a test file as below:

```python
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
```
Then you start pytest:
```
cd <your project>
pytest tests --xlog=./log.yaml --xopt product_version=1.5 --xopt environment.stand.type=virtual
```
YAML report file looks like following:
```yaml
case_1:
- call_path: C:/Users/user/AppData/Local/Temp/pytest-of-user/pytest-12/test_10/test_1.py::test_simple_case
  call_status: passed
  environment: &id001
    stand:
      type: virtual
  finished: 1589473975.4059443
  product_version: '1.5'
  session_id: 1589473975
  setup_status: passed
  started: 1589473975.4059443
  teardown_status: passed
case_10:
- call_path: C:/Users/user/AppData/Local/Temp/pytest-of-user/pytest-12/test_10/test_1.py::test_case_id_from_param[1-1]
  call_status: passed
  environment: *id001
  finished: 1589473975.449009
  product_version: '1.5'
  session_id: 1589473975
  setup_status: passed
  started: 1589473975.4480073
  teardown_status: passed
case_11:
- call_path: C:/Users/user/AppData/Local/Temp/pytest-of-user/pytest-12/test_10/test_1.py::test_case_id_from_param[2-3]
  call_status: failed
  environment: *id001
  finished: 1589473975.4520135
  product_version: '1.5'
  session_id: 1589473975
  setup_status: passed
  started: 1589473975.449009
  teardown_status: passed
case_2:
- call_path: C:/Users/user/AppData/Local/Temp/pytest-of-user/pytest-12/test_10/test_1.py::test_case_dynamic_options
  call_status: failed
  conf:
    initiator_platform: Windows-10-10.0.16299-SP0
  environment: *id001
  finished: 1589473975.441999
  product_version: '1.5'
  session_id: 1589473975
  setup_status: passed
  started: 1589473975.4069457
  teardown_status: passed
  test_type: sanity
case_3:
- call_path: C:/Users/user/AppData/Local/Temp/pytest-of-user/pytest-12/test_10/test_1.py::test_with_param[8-8]
  call_status: passed
  environment: *id001
  finished: 1589473975.4440014
  product_version: '1.5'
  session_id: 1589473975
  setup_status: passed
  started: 1589473975.4429998
  teardown_status: passed
- call_path: C:/Users/user/AppData/Local/Temp/pytest-of-user/pytest-12/test_10/test_1.py::test_with_param[5-6]
  call_status: failed
  environment: *id001
  finished: 1589473975.4470062
  product_version: '1.5'
  session_id: 1589473975
  setup_status: passed
  started: 1589473975.4440014
  teardown_status: passed
case_4:
- call_path: C:/Users/user/AppData/Local/Temp/pytest-of-user/pytest-12/test_10/test_1.py::test_skipped_case
  call_status: null
  environment: *id001
  finished: 1589473975.4480073
  product_version: '1.5'
  session_id: 1589473975
  setup_status: skipped
  skip: Issue BUG-123456
  started: 1589473975.4470062
  teardown_status: passed
no_case_C_Users_user_AppData_Local_Temp_pytest_of_user_pytest_12_test_10_test_1_py_test_no_decorator:
- call_path: C:/Users/user/AppData/Local/Temp/pytest-of-user/pytest-12/test_10/test_1.py::test_no_decorator
  call_status: passed
  environment: *id001
  finished: 1589473975.4429998
  product_version: '1.5'
  session_id: 1589473975
  setup_status: passed
  started: 1589473975.441999
  teardown_status: passed
```
As you can see the plugin create new key for every test run no matter the decorator exists or not.
Also if a test function has been parametrized then the runs stored as list items otherwise 
the case key has the list containing single element.    
You can pass the options to `--xopt name=value` or define dynamic options in the decorator arguments.
If name splitted by dots it will be converted to nested keys of dictionary. 
For instance you have `--xopt key1.key2.key3=value`. 
It will be reported as following:  
```yaml
case_1:
  -
    key1:
      key2:
        key3: value
```


## Run  Tests
```
cd pytest-xlog
pytest tests
```

## Development
Remove pytest-xlog from pytest plugins (if applicable)
```
pip uninstall pytest-xlog
```
Checkout the repository.

Install sources in developer mode
```
cd <root of repositoiry>
pip install -e .
``` 
