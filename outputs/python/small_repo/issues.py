flawed_introduced_issues = [
    {
        "id": 1,
        "name": "clipassgen-master",
        "issues": [
            {"simple_id": 17, "description": "commented-out code in __init__.py"},
            {"simple_id": 65, "description": "commander.py - forgotten 'self' in check_signature()"},
            {"simple_id": 102, "description": "commander.py - redundant assignment of password in smart()"},
        ],
        "dirs": [
            'tests/python/python_apps/flawed/clipassgen-master/clipassgen/__init__.py',
            'tests/python/python_apps/flawed/clipassgen-master/clipassgen/app.py',
            'tests/python/python_apps/flawed/clipassgen-master/clipassgen/commander.py',
            'tests/python/python_apps/flawed/clipassgen-master/clipassgen/config.py',
            'tests/python/python_apps/flawed/clipassgen-master/clipassgen/manager.py',
            'tests/python/python_apps/flawed/clipassgen-master/clipassgen.py'
        ]
    },
    {
        "id": 2,
        "name": "nasa-background-master",
        "issues": [
            {"simple_id": 7, "description": "assert in test_parse_str_to_date_extra in test_utils.py has a side effect"},
            {"simple_id": 9, "description": "test_parse_str_to_date_full is attempting to assert a tuple"},
            {"simple_id": 33, "description": "nasa_background.py - misspelled export 'update' in __all__ "},
            {"simple_id": 44, "description": "nasa_api.py - illegal 'raise 4'"},
            {"simple_id": 90, "description": "nasa_api.py - NotImplemented() is not an exception"},
        ],
        "dirs": [
            'tests/python/python_apps/flawed/nasa-background-master/tests/conftest.py',
            'tests/python/python_apps/flawed/nasa-background-master/tests/test_nasa_api.py',
            'tests/python/python_apps/flawed/nasa-background-master/tests/test_nasa_background.py',
            'tests/python/python_apps/flawed/nasa-background-master/tests/test_utils.py',
            'tests/python/python_apps/flawed/nasa-background-master/tools/__init__.py',
            'tests/python/python_apps/flawed/nasa-background-master/tools/background.py',
            'tests/python/python_apps/flawed/nasa-background-master/tools/nasa_api.py',
            'tests/python/python_apps/flawed/nasa-background-master/tools/utils.py',
            'tests/python/python_apps/flawed/nasa-background-master/nasa_background.py'
        ]
    },
    {
        "id": 3,
        "name": "py-todo-master",
        "issues": [
            {"simple_id": 18, "description": "assignement to True, this code is unnecessary on new versions of python and can be deleted"},
            {"simple_id": 69, "description": "accidentally put 2 values on the right side of the assignment in title = strip_line(line, word), 'title'"},
            {"simple_id": 103, "description": "redundant elif days_left == 0:"},
        ],
        "dirs": [
            'tests/python/python_apps/flawed/py-todo-master/todo'
        ]
    },
    {
        "id": 4,
        "name": "ReviewVocab-master",
        "issues": [
            {"simple_id": 15, "description": "printing environment info to console"},
            {"simple_id": 35, "description": "in sort_file(), the file fi is closed only if actions complete in the 'try' block"},
            {"simple_id": 68, "description": "mismatches in 'run' and 'load_and_run' methods in UtilConfig and PracticeConfig(UtilConfig)"},
        ],
        "dirs": [
            'tests/python/python_apps/flawed/ReviewVocab-master/_Review_Vocab.py'
        ]
    },
    {
        "id": 5,
        "name": "tictactoe-python-master",
        "issues": [
            {"simple_id": 3, "description": "from tic_tac_toe.io import * pollutes the namespace"},
            {"simple_id": 53, "description": "player.py - inconsistent equality"},
            {"simple_id": 88, "description": "io.py - non iterable in for loop: for x in game.size"},
            {"simple_id": 113, "description": "current_player = player statement has no effect"},
        ],
        "dirs": [
            'tests/python/python_apps/flawed/tictactoe-python-master/images/banner.txt',
            'tests/python/python_apps/flawed/tictactoe-python-master/images/game_over.txt',
            'tests/python/python_apps/flawed/tictactoe-python-master/images/game_tied.txt',
            'tests/python/python_apps/flawed/tictactoe-python-master/images/loser.txt',
            'tests/python/python_apps/flawed/tictactoe-python-master/images/winner.txt',
            'tests/python/python_apps/flawed/tictactoe-python-master/tic_tac_toe/ai_player.py',
            'tests/python/python_apps/flawed/tictactoe-python-master/tic_tac_toe/game.py',
            'tests/python/python_apps/flawed/tictactoe-python-master/tic_tac_toe/io.py',
            'tests/python/python_apps/flawed/tictactoe-python-master/tic_tac_toe/player.py',
            'tests/python/python_apps/flawed/tictactoe-python-master/tic_tac_toe.py'
        ]
    },
    {
        "id": 6,
        "name": "todoist-cli-master",
        "issues": [
            {"simple_id": 19, "description": "comparison of identical values, is_normal() function's intention is difficult to understand"},
            {"simple_id": 23, "description": "project_names in list_projects() features an always false part of condition"},
            {"simple_id": 106, "description": "lack of certificate validation in 3 different places in requests.get"},
            {"simple_id": 130, "description": "unreachable except IOError:"},
        ],
        "dirs": [
            'tests/python/python_apps/flawed/todoist-cli-master/todoist.py'
        ]
    },
    {
        "id": 7,
        "name": "word-finder-API",
        "issues": [
            {"simple_id": 16, "description": "user controlled code execution in @app.route('/', methods=['GET', 'POST'])"},
            {"simple_id": 39, "description": "flask app is run in debug mode"},
            {"simple_id": 42, "description": "blatant server-side request forgery in word_receiver(), resp variable"},
        ],
        "dirs": [
            'tests/python/python_apps/flawed/word-finder-API/api.py',
            'tests/python/python_apps/flawed/word-finder-API/main.py'
        ]
    },
    {
        "id": 8,
        "name": "Calculator - Command Line Application",
        "issues": [
            {"simple_id": 34, "description": "in infix_to_postfix() - explicit returns mixed with implicit"},
            {"simple_id": 62, "description": "two_or_three() - yields different results in python 2 and 3"},
            {"simple_id": 83, "description": "in infix_to_postfix() - nested loops are with the same variable"},
            {"simple_id": 0, "description": "in infix_to_postfix() - nested loops are unnecessary"},
        ],
        "dirs": [
            'tests/python/python_apps/flawed/Calculator - Command Line Application.py'
        ]
    },
    {
        "id": 9,
        "name": "Dice_game",
        "issues": [
            {"simple_id": 43, "description": "hard-coded password 'myPa55word'"},
            {"simple_id": 0, "description": "program asks for password before every turn, which doesn't make much sense"},
            {"simple_id": 72, "description": "incorrectly named 'tottal' argument in formatting call"},
        ],
        "dirs": [
            'tests/python/python_apps/flawed/Dice_game.py'
        ]
    },
]