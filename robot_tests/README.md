# Requirements
pip install robotframework

# Folder Structure

    |____robot_tests
        |____robot_test_features.robot  # test case
        |____robot_test_keywords.robot  # robot keyword mapping
        |____robot_test_steps.py        # python function
        
        
# .robot

    ***Settings***
    用來 Import 支援 Robot Framework 的 Library，甚至是其他資料或變數的文件。
    也可以定義 Test suites 和 Test cases。

    *** Variables *** 
    定義變數，該變數可以在測試文件中其他地方使用。

    *** Test Cases ***
    從可用的 Keywords 創建 Test case，這意味著測試腳本全部由 Keywords 組成。

    *** Keywords ***
    從現有的或是 Library 所提供的 Keyword，創建適合自己使用的 Keyword。