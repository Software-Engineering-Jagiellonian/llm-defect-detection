issues = [
    {"simple_id": 12, "description": "client.py is attempting to bind a socket to all network interfaces"},
    {"simple_id": 28, "description": "client.py - duplicate key in data dict"},
    {"simple_id": 30, "description": "client.py - empty except in run()"},
    {"simple_id": 36, "description": "server.py - QMainWindow is passed to super() instead of ServerWindow in method __init__, in ServerWindow class"},
    {"simple_id": 38, "description": "client.py - first parameter of method __init__ is not named 'self'"},
    {"simple_id": 50, "description": "client.py - PchatWindow is missing ordering operations"},
    {"simple_id": 56, "description": "client.py - information exposure through traceback.format_exc() in exception"},
    {"simple_id": 59, "description": "client.py - PchatWindow iterator does not return self in __iter__ method"},
    {"simple_id": 92, "description": "client.py - overly and unnecessarily permissive os.chmod(serverdb, 0o777)"},
]

files_included = [
    'tests/python/big_repo/original/pchat-master/client/add_server.ui'
    'tests/python/big_repo/original/pchat-master/client/chatroom.ui',
    'tests/python/big_repo/original/pchat-master/client/client.py',
    'tests/python/big_repo/original/pchat-master/client/pchat.ui',
    'tests/python/big_repo/original/pchat-master/client/servers.json',
    'tests/python/big_repo/original/pchat-master/server/server.py',
    'tests/python/big_repo/original/pchat-master/server/server.ui',
    'tests/python/big_repo/original/pchat-master/requirements.txt'
]