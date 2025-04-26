simple = [
    {
        "id": 1,
        "name": "'apply' function used",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-use-of-apply/",
        "code": """apply(function, args, keywords)""",
        "fix": """function(*args, **keywords)"""
    },
    {
        "id": 3,
        "name": "'import *' may pollute namespace",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-polluting-import/",
        "code": """# Example module - finance.py

__all__ = ['tax1', 'tax2']

tax1 = 5
tax2 = 10
def cost(): return 'cost'

# Imported into code using

from finance import *

print tax1
print tax2""",
        "fix": """"""
    },
    {
        "id": 5,
        "name": "'super' in old-style class",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-super-in-old-style/",
        "code": """class PythonModule(_ModuleIteratorHelper):

    # class definitions ....

    def walkModules(self, importPackages=False):
        if importPackages and self.isPackage():
            self.load()
        return super(PythonModule, self).walkModules(importPackages=importPackages)""",
        "fix": """
class PythonModule(_ModuleIteratorHelper):

    # class definitions ....

    def walkModules(self, importPackages=False):
        if importPackages and self.isPackage():
            self.load()
        return _ModuleIteratorHelper.__init__(PythonModule, self).walkModules(importPackages=importPackages)"""
    },
    {
        "id": 6,
        "name": "Accepting unknown SSH host keys when using Paramiko",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-paramiko-missing-host-key-validation/",
        "code": """from paramiko.client import SSHClient, AutoAddPolicy, RejectPolicy

def unsafe_connect():
    client = SSHClient()
    client.set_missing_host_key_policy(AutoAddPolicy)
    client.connect("example.com")

    # ... interaction with server

    client.close()""",
        "fix": """def safe_connect():
    client = SSHClient()
    client.set_missing_host_key_policy(RejectPolicy)
    client.connect("example.com")

    # ... interaction with server

    client.close()"""
    },
    {
        "id": 7,
        "name": "An assert statement has a side-effect",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-side-effect-in-assert/",
        "code": """assert subprocess.call(['run-backup']) == 0""",
        "fix": """"""
    },
    {
        "id": 8,
        "name": "Arbitrary file write during tarfile extraction",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-tarslip/",
        "code": """import sys
import tarfile

with tarfile.open(sys.argv[1]) as tar:
    for entry in tar:
        tar.extract(entry, "/tmp/unpack/")""",
        "fix": """import sys
import tarfile
import os.path"""
    },
    {
        "id": 11,
        "name": "Bad HTML filtering regexp",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-bad-tag-filter/",
        "code": """import re

def filterScriptTags(content): 
    oldContent = ""
    while oldContent != content:
        oldContent = content
        content = re.sub(r'<script.*?>.*?</script>', '', content, flags= re.DOTALL | re.IGNORECASE)
    return content""",
        "fix": """"""
    },
    {
        "id": 12,
        "name": "Binding a socket to all network interfaces",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-bind-socket-all-network-interfaces/",
        "code": """import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 31137))
""",
        "fix": """
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('84.68.10.12', 8080))"""
    },
    {
        "id": 13,
        "name": "CSRF protection weakened or disabled",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-csrf-protection-disabled/",
        "code": """MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]""",
        "fix": """"""
    },
    {
        "id": 14,
        "name": "Clear-text logging of sensitive information",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-clear-text-logging-sensitive-data/",
        "code": """
import os
print(f"[INFO] Environment: {os.environ}")""",
        "fix": """"""
    },
    {
        "id": 15,
        "name": "Clear-text storage of sensitive information",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-clear-text-storage-sensitive-data/",
        "code": """from flask import Flask, make_response, request

app = Flask("Leak password")

@app.route('/')
def index():
    password = request.args.get("password")
    resp = make_response(render_template(...))
    resp.set_cookie("password", password)
    return resp""",
        "fix": """"""
    },
    {
        "id": 16,
        "name": "Code injection",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-code-injection/",
        "code": """urlpatterns = [
    url(r'^code-ex1$', code_execution_bad, name='code-execution-bad'),
    url(r'^code-ex2$', code_execution_good, name='code-execution-good')
]

def code_execution(request):
    if request.method == 'POST':
        first_name = base64.decodestring(request.POST.get('first_name', ''))
        exec("setname('%s')" % first_name)""",
        "fix": """def code_execution(request):
    if request.method == 'POST':
        first_name = base64.decodestring(request.POST.get('first_name', ''))
        setname(first_name)"""
    },
    {
        "id": 17,
        "name": "Commented-out code",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-commented-out-code/",
        "code": """def area(r):
    #if DEBUG:
    #   print("Computing area of %r" % r)
    return r.length * r.width""",
        "fix": """"""
    },
    {
        "id": 18,
        "name": "Comparison of constants",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-comparison-of-constants/",
        "code": """
try:
    True
except NameError:
    __builtins__.True = 1==1""",
        "fix": """"""
    },
    {
        "id": 19,
        "name": "Comparison of identical values",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-comparison-of-identical-expressions/",
        "code": """
def is_normal(f):
    return not cmath.isinf(f) and f == f
""",
        "fix": """
def is_normal(f):
    return not cmath.isinf(f) and not cmath.isnan(f)"""
    },
    {
        "id": 20,
        "name": "Comparison using 'is' when operands support __eq__",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-comparison-using-is/",
        "code": """
DEFAULT = "default"

def get_color(name, fallback):
    if name in COLORS:
        return COLORS[name]
    elif fallback is DEFAULT:
        return DEFAULT_COLOR
    else:
        return fallback

print (get_color("spam", "default-spam"[:7]))""",
        "fix": """"""
    },
    {
        "id": 21,
        "name": "Conflicting attributes in base classes",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-conflicting-attributes/",
        "code": """class TCPServer(object):

    def process_request(self, request, client_address):
        self.do_work(request, client_address)
        self.shutdown_request(request)


class ThreadingMixIn:

    def process_request(self, request, client_address):
        t = threading.Thread(target = self.do_work, args = (request, client_address))
        t.daemon = self.daemon_threads
        t.start()

class ThreadingTCPServer(ThreadingMixIn, TCPServer): pass""",
        "fix": """
class ThreadingTCPServerOverriding(ThreadingMixIn, TCPServer):

    def process_request(self, request, client_address):
        ThreadingMixIn.process_request(self, request, client_address)


class ThreadingMixIn:
    def do_job_in_thread(self, job, args):
        #Start a new thread to do the job
        t = threading.Thread(target = job, args = args)
        t.start()

class ThreadingTCPServerChangedHierarchy(ThreadingMixIn, TCPServer):

    def process_request(self, request, client_address):
        self.do_job_in_thread(self.do_work,  (request, client_address))"""
    },
    {
        "id": 23,
        "name": "Constant in conditional expression or statement",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-constant-conditional-expression/",
        "code": """if True:
    print "True is true!"

def limit(l):
    if l < -100:
        l = -100
    if 1 > 100:
        l = 100
    return l""",
        "fix": """"""
    },
    {
        "id": 24,
        "name": "Cyclic import",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-cyclic-import/",
        "code": """
        # bar.py
        from foo import abc

        # foo.py
        from bar import dce
        """,
        "fix": """"""
    },
    {
        "id": 25,
        "name": "Default version of SSL/TLS may be insecure",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-insecure-default-protocol/",
        "code": """import ssl
import socket

ssl.wrap_socket(socket.socket())

context = ssl.SSLContext()""",
        "fix": """import ssl

context = ssl.SSLContext()
context.options |= ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1

context = ssl.create_default_context()
context.minimum_version = ssl.TLSVersion.TLSv1_2"""
    },
    {
        "id": 27,
        "name": "Deserialization of user-controlled data",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-unsafe-deserialization/",
        "code": """from django.conf.urls import url
import pickle

def unsafe(pickled):
    return pickle.loads(pickled)

urlpatterns = [
    url(r'^(?P<object>.*)$', unsafe)
]""",
        "fix": """
from django.conf.urls import url
import json

def safe(pickled):
    return json.loads(pickled)

urlpatterns = [
    url(r'^(?P<object>.*)$', safe)
]"""
    },
    {
        "id": 28,
        "name": "Duplicate key in dict literal",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-duplicate-key-dict-literal/",
        "code": """dictionary = {1:"a", 2:"b", 2:"c"}
print dictionary[2]""",
        "fix": """"""
    },
    {
        "id": 29,
        "name": "Duplication in regular expression character class",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-regex-duplicate-in-character-class/",
        "code": """import re
matcher = re.compile(r"[password|pwd]")

def find_password(data):
    if matcher.match(data):
        print("Found password!")""",
        "fix": """"""
    },
    {
        "id": 30,
        "name": "Empty except",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-empty-except/",
        "code": """try:
    security_manager.drop_privileges()
except SecurityError:
    pass""",
        "fix": """"""
    },
    {
        "id": 32,
        "name": "Except block handles 'BaseException'",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-catch-base-exception/",
        "code": """
def call_main_program_implicit_handle_base_exception():
    try:
        application.main()
    except Exception as ex:
        log(ex)
    except:
        pass

def call_main_program_explicit_handle_base_exception():
    try:
        application.main()
    except Exception as ex:
        log(ex)
    except BaseException:
        pass""",
        "fix": """def call_main_program_fixed():
    try:
        application.main()
    except Exception as ex:
        log(ex)
    except SystemExit:
        pass"""
    },
    {
        "id": 33,
        "name": "Explicit export is not defined",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-undefined-export/",
        "code": """__all__ = ['spamm', 'troll', 'paywall']

def spam(): return 'Spam'
def troll(): return 'Troll'
def paywall(): return 'Pay wall'""",
        "fix": """__all__ = ['spam', 'troll', 'paywall']

def spam(): return 'Spam'
def troll(): return 'Troll'
def paywall(): return 'Pay wall'"""
    },
    {
        "id": 34,
        "name": "Explicit returns mixed with implicit (fall through) returns",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-mixed-returns/",
        "code": """   def check_state1(state, interactive=True):
        if not state['good'] or not state['bad']:
            if (good or bad or skip or reset) and interactive:
                return
            if not state['good']:
                raise util.Abort(_('cannot bisect (no known good revisions)'))
            else:
                raise util.Abort(_('cannot bisect (no known bad revisions)')) 
        return True  		""",
        "fix": """    def check_state2(state, interactive=True):
        if not state['good'] or not state['bad']:
            if (good or bad or skip or reset) and interactive:
                return False
            if not state['good']:
                raise util.Abort(_('cannot bisect (no known good revisions)'))
            else:
                raise util.Abort(_('cannot bisect (no known bad revisions)'))
        return True"""
    },
    {
        "id": 35,
        "name": "File is not always closed",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-file-not-closed/",
        "code": """f = open("filename")
    ... # Actions to perform on file
f.close()
""",
        "fix": """with open("filename") as f:
    ...# Actions to perform on file
"""
    },
    {
        "id": 36,
        "name": "First argument to super() is not enclosing class",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-super-not-enclosing-class/",
        "code": """
class Vehicle(object):
    pass

class Car(Vehicle):

    def __init__(self):
        super(Vehicle, self).__init__()
        self.car_init()

class StatusSymbol(object):

    def __init__(self):
        super(StatusSymbol, self).__init__()
        self.show_off()

class SportsCar(Car, StatusSymbol):

    def __init__(self):
        super(SportsCar, self).__init__()
        self.sports_car_init()""",
        "fix": """"""
    },
    {
        "id": 37,
        "name": "First parameter of a class method is not named 'cls'",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-not-named-cls/",
        "code": """class Entry(object):
    @classmethod
    def make(klass):
        return Entry()""",
        "fix": """class Entry(object):
    @classmethod
    def make(cls):
        return Entry()"""
    },
    {
        "id": 38,
        "name": "First parameter of a method is not named 'self'",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-not-named-self/",
        "code": """class Point:
    def __init__(val, x, y):
        val._x = x
        val._y = y""",
        "fix": """class Point2:
    def __init__(self, x, y):
        self._x = x
        self._y = y"""
    },
    {
        "id": 39,
        "name": "Flask app is run in debug mode",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-flask-debug/",
        "code": """from flask import Flask

app = Flask(__name__)

@app.route('/crash')
def main():
    raise Exception()

app.run(debug=True)""",
        "fix": """"""
    },
    {
        "id": 40,
        "name": "Formatted object is not a mapping",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-percent-format-not-mapping/",
        "code": """def unsafe_format():
    if unlikely_condition():
        args = (1,2,3)
    else:
        args = {a:1,b:2,c:3}
    return "%(a)s %(b)s %(c)s" % args""",
        "fix": """"""
    },
    {
        "id": 42,
        "name": "Full server-side request forgery",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-full-ssrf/",
        "code": """import requests
from flask import Flask, request

app = Flask(__name__)

@app.route("/full_ssrf")
def full_ssrf():
    target = request.args["target"]

    resp = requests.get("https://" + target + ".example.com/data/")""",
        "fix": """
    subdomain = "europe" if target == "EU" else "world"
    resp = requests.get("https://" + subdomain + ".example.com/data/")"""
    },
    {
        "id": 43,
        "name": "Hard-coded credentials",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-hardcoded-credentials/",
        "code": """import hashlib
import binascii

def process_request(request):
    password = request.GET["password"]

    if password == "myPa55word":
        redirect("login")

    hashed_password = load_from_config('hashed_password', CONFIG_FILE)
    salt = load_from_config('salt', CONFIG_FILE)
""",
        "fix": """
    dk = hashlib.pbkdf2_hmac('sha256', password, salt, 100000)
    hashed_input = binascii.hexlify(dk)
    if hashed_input == hashed_password:
        redirect("login")
"""
    },
    {
        "id": 44,
        "name": "Illegal raise",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-illegal-raise/",
        "code": """
def raise_int():
    raise 4
""",
        "fix": """"""
    },
    {
        "id": 45,
        "name": "Implicit string concatenation in a list",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-implicit-string-concatenation-in-list/",
        "code": """def unclear():
    return [
        "first part of long string"
        " and the second part",
        "/usr/local"
        "/usr/bin"
    ]""",
        "fix": """"""
    },
    {
        "id": 47,
        "name": "Importing value of mutable attribute",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-import-of-mutable-attribute/",
        "code": """
# module 1
from sys import stdout

def main():
    stdout.write("Hello World!")

# module 2  
import sys

def redirect_to_file(function, args, kwargs, filename):
    with open(filename) as out:
        orig_stdout = sys.stdout
        sys.stdout = out
        try:
            function(*args, **kwargs)
        finally:
            sys.stdout = orig_stdout

    """,
        "fix": """
# module 1
import sys

def main():
    sys.stdout.write("Hello World!")
        """
    },
    {
        "id": 48,
        "name": "Imprecise assert",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-imprecise-assert/",
        "code": """from unittest import TestCase

class MyTest(TestCase):


    def testInts(self):
        self.assertTrue(1 == 1)
        self.assertFalse(1 > 2)
        self.assertTrue(1 in [])""",
        "fix": """"""
    },
    {
        "id": 49,
        "name": "Incomplete URL substring sanitization",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-incomplete-url-substring-sanitization/",
        "code": """from flask import Flask, request, redirect
from urllib.parse import urlparse

app = Flask(__name__)

@app.route('/some/path/bad1')
def unsafe1(request):
    target = request.args.get('target', '')
    if "example.com" in target:
        return redirect(target)""",
        "fix": """@app.route('/some/path/good1')
def safe1(request):
    allowlist = [
        "example.com/home",
        "example.com/login",
    ]
    target = request.args.get('target', '')
    if target in allowlist:
        return redirect(target)
"""
    },
    {
        "id": 50,
        "name": "Incomplete ordering",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-incomplete-ordering/",
        "code": """class IncompleteOrdering(object):
    def __init__(self, i):
        self.i = i

    def __lt__(self, other):
        return self.i < other.i""",
        "fix": """"""
    },
    {
        "id": 51,
        "name": "Incomplete regular expression for hostnames",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-incomplete-hostname-regexp/",
        "code": """from flask import Flask, request, redirect
import re

app = Flask(__name__)

UNSAFE_REGEX = re.compile("(www|beta).example.com/")

@app.route('/some/path/bad')
def unsafe(request):
    target = request.args.get('target', '')
    if UNSAFE_REGEX.match(target):
        return redirect(target)""",
        "fix": """SAFE_REGEX = re.compile(r"(www|beta)\.example\.com/")

@app.route('/some/path/good')
def safe(request):
    target = request.args.get('target', '')
    if SAFE_REGEX.match(target):
        return redirect(target)"""
    },
    {
        "id": 52,
        "name": "Inconsistent equality and hashing",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-equals-hash-mismatch/",
        "code": """
class Point(object):

    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __repr__(self):
        return 'Point(%r, %r)' % (self._x, self._y)

    def __eq__(self, other):
        if not isinstance(other, Point):
            return False
        return self._x == other._x and self._y == other._y
""",
        "fix": """
class UnhashablePoint(object):

    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __repr__(self):
        return 'Point(%r, %r)' % (self._x, self._y)

    def __eq__(self, other):
        if not isinstance(other, Point):
            return False
        return self._x == other._x and self._y == other._y

    __hash__ = None
"""
    },
    {
        "id": 53,
        "name": "Inconsistent equality and inequality",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-inconsistent-equality/",
        "code": """class PointOriginal(object):

    def __init__(self, x, y):
        self._x, x
        self._y = y

    def __repr__(self):
        return 'Point(%r, %r)' % (self._x, self._y)

    def __eq__(self, other):
        if not isinstance(other, Point):
            return False
        return self._x == other._x and self._y == other._y""",
        "fix": """class PointUpdated(object):

    def __init__(self, x, y):
        self._x, x
        self._y = y

    def __repr__(self):
        return 'Point(%r, %r)' % (self._x, self._y)

    def __eq__(self, other):
        if not isinstance(other, Point):
            return False
        return self._x == other._x and self._y == other._y

    def __ne__(self, other):
        return not self == other"""
    },
    {
        "id": 54,
        "name": "Inconsistent method resolution order",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-inconsistent-mro/",
        "code": """class X(object):
    def __init__(self):
        print("X")
class Y(object,X):
    def __init__(self):
        print("Y")""",
        "fix": """"""
    },
    {
        "id": 56,
        "name": "Information exposure through an exception",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-stack-trace-exposure/",
        "code": """from flask import Flask
app = Flask(__name__)

import traceback

def do_computation():
    raise Exception("Secret info")

@app.route('/bad')
def server_bad():
    try:
        do_computation()
    except Exception as e:
        return traceback.format_exc()""",
        "fix": """
@app.route('/good')
def server_good():
    try:
        do_computation()
    except Exception as e:
        log(traceback.format_exc())
        return "An internal error has occurred!" """
    },
    {
        "id": 57,
        "name": "Insecure temporary file",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-insecure-temporary-file/",
        "code": """from tempfile import mktemp

def write_results(results):
    filename = mktemp()
    with open(filename, "w+") as f:
        f.write(results)
    print("Results written to", filename)""",
        "fix": """from tempfile import NamedTemporaryFile

def write_results(results):
    with NamedTemporaryFile(mode="w+", delete=False) as f:
        f.write(results)
    print("Results written to", f.name)"""
    },
    {
        "id": 58,
        "name": "Iterable can be either a string or a sequence",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-iteration-string-and-sequence/",
        "code": """
def greeting():
    if is_global():
        greet = [ "Hello", "World" ]
    else:
        greet = "Hello"
    for word in greet:
        print(word)""",
        "fix": """
def fixed_greeting():
    if is_global():
        greet = [ "Hello", "World" ]
    else:
        greet = [ "Hello" ]
    for word in greet:
        print(word)"""
    },
    {
        "id": 59,
        "name": "Iterator does not return self from __iter__ method",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-iter-returns-non-self/",
        "code": """class MyRange(object):
    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self):
        return self.current

    def next(self):
        if self.current > self.high:
            raise StopIteration
        self.current += 1
        return self.current - 1""",
        "fix": """"""
    },
    {
        "id": 60,
        "name": "Jinja2 templating with autoescape=False",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-jinja2-autoescape-false/",
        "code": """from flask import Flask, request, make_response, escape
from jinja2 import Environment, select_autoescape, FileSystemLoader

app = Flask(__name__)
loader = FileSystemLoader( searchpath="templates/" )

unsafe_env = Environment(loader=loader)

def render_response_from_env(env):
    name = request.args.get('name', '')
    template = env.get_template('template.html')
    return make_response(template.render(name=name))

@app.route('/unsafe')
def unsafe():
    return render_response_from_env(unsafe_env)
""",
        "fix": """from flask import Flask, request, make_response, escape
from jinja2 import Environment, select_autoescape, FileSystemLoader

app = Flask(__name__)
loader = FileSystemLoader( searchpath="templates/" )

safe1_env = Environment(loader=loader, autoescape=True)
safe2_env = Environment(loader=loader, autoescape=select_autoescape())

def render_response_from_env(env):
    name = request.args.get('name', '')
    template = env.get_template('template.html')
    return make_response(template.render(name=name))

@app.route('/safe1')
def safe1():
    return render_response_from_env(safe1_env)

@app.route('/safe2')
def safe2():
    return render_response_from_env(safe2_env)"""
    },
    {
        "id": 61,
        "name": "LDAP query built from user-controlled sources",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-ldap-injection/",
        "code": """from flask import request, Flask
import ldap

@app.route("/normal")
def normal():
    unsafe_dc = request.args['dc']
    unsafe_filter = request.args['username']

    dn = "dc={}".format(unsafe_dc)
    search_filter = "(user={})".format(unsafe_filter)

    ldap_connection = ldap.initialize("ldap://127.0.0.1")
    user = ldap_connection.search_s(
        dn, ldap.SCOPE_SUBTREE, search_filter)""",
        "fix": """from flask import request, Flask
import ldap3
from ldap3.utils.dn import escape_rdn
from ldap3.utils.conv import escape_filter_chars


@app.route("/normal")
def normal():
    unsafe_dc = request.args['dc']
    unsafe_filter = request.args['username']

    safe_dc = escape_rdn(unsafe_dc)
    safe_filter = escape_filter_chars(unsafe_filter)

    dn = "dc={}".format(safe_dc)
    search_filter = "(user={})".format(safe_filter)

    srv = ldap3.Server('ldap://127.0.0.1')
    conn = ldap3.Connection(srv, user=dn, auto_bind=True)
    conn.search(dn, search_filter)"""
    },
    {
        "id": 62,
        "name": "List comprehension variable used in enclosing scope",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-leaking-list-comprehension/",
        "code": """def two_or_three():
    x = 3
    [0 for x in range(3)]
    return x

print(two_or_three())""",
        "fix": """def just_three():
    x = 3
    [0 for y in range(3)]
    return x

print(just_three())"""
    },
    {
        "id": 63,
        "name": "Log Injection",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-log-injection/",
        "code": """#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from flask import Flask
from flask import request
from django.utils.log import request_logger
import logging

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

@app.route('/bad1')
def bad1():
    name = request.args.get('name')
    app.logger.info('User name: ' + name)
    return 'bad1'

@app.route('/bad2')
def bad2():
    name = request.args.get('name')
    logging.info('User name: ' + name)
    return 'bad2'

@app.route('/bad3')
def bad3():
    name = request.args.get('name')
    request_logger.warn('User name: ' + name)
    return 'bad3'

@app.route('/bad4')
def bad4():
    name = request.args.get('name')
    logtest = logging.getLogger('test')
    logtest.debug('User name: ' + name)
    return 'bad4'

if __name__ == '__main__':
    app.debug = True
    handler = logging.FileHandler('log')
    app.logger.addHandler(handler)
    app.run()""",
        "fix": """#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from flask import Flask
from flask import request
import logging

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

@app.route('/good1')
def good1():
    name = request.args.get('name')
    name = name.replace('\r\n','').replace('\n','')
    logging.info('User name: ' + name)
    return 'good1'

if __name__ == '__main__':
    app.debug = True
    handler = logging.FileHandler('log')
    app.logger.addHandler(handler)
    app.run()"""
    },
    {
        "id": 64,
        "name": "Loop variable capture",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-loop-variable-capture/",
        "code": """
def make_incrementers():
    result = []
    for i in range(10):
        def incrementer(x):
            return x + i
        result.append(incrementer)
    return result

def test():
    incs = make_incrementers()
    for x in range(10):
        for y in range(10):
            assert incs[x](y) == x+y

test()""",
        "fix": """
def make_incrementers():
    result = []
    for i in range(10):
        def incrementer(x, i=i):
            return x + i
        result.append(incrementer)
    return result

def test():
    incs = make_incrementers()
    for x in range(10):
        for y in range(10):
            assert incs[x](y) == x+y

test()"""
    },
    {
        "id": 65,
        "name": "Maybe missing 'self' in comparison",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-comparison-missing-self/",
        "code": """
class Customer:

    def __init__(self, data):
        self.data = data

    def check_data(self, data):
        if data != data:
            raise Exception("Invalid data!")""",
        "fix": """class Customer:

    def __init__(self, data):
        self.data = data

    def check_data(self, data):
        if self.data != data:
            raise Exception("Invalid data!")"""
    },
    {
        "id": 66,
        "name": "Membership test with a non-container",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-member-test-non-container/",
        "code": """class NotAContainer(object):

    def __init__(self, *items):
        self.items = items

def main():
    cont = NotAContainer(1, 2, 3)
    if 2 in cont:
        print("2 in container")""",
        "fix": """"""
    },
    {
        "id": 67,
        "name": "Mismatch between signature and use of an overridden method",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-inheritance-incorrect-overridden-signature/",
        "code": """
class BaseClass(object):

    def run(self, source, filename, symbol="single"):
        ... # Definition

    def load_and_run(self, filename):
        source = self.load(filename)
        self.run(source)

class DerivedClass(BaseClass):

    def run(self, source):
        ... # Definition""",
        "fix": """"""
    },
    {
        "id": 68,
        "name": "Mismatch between signature and use of an overriding method",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-inheritance-incorrect-overriding-signature/",
        "code": """
class BaseClass(object):

    def run(self, source, filename, symbol="single"):
        ... # Definition

    def load_and_run(self, filename):
        source = self.load(filename)
        self.run(source, filename)

class DerivedClass(BaseClass):

    def run(self, source):
        ... # Definition""",
        "fix": """"""
    },
    {
        "id": 69,
        "name": "Mismatch in multiple assignment",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-mismatched-multiple-assignment/",
        "code": """
a, b = 0, 1, 1
while b < 10:
     print b
     a, b = b, a+b
""",
        "fix": """
a, b = 0, 1
while b < 10:
     print b
     a, b = b, a+b"""
    },
    {
        "id": 70,
        "name": "Missing call to __del__ during object destruction",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-missing-call-to-delete/",
        "code": """class Vehicle(object):

    def __del__(self):
        recycle(self.base_parts)

class Car(Vehicle):

    def __del__(self):
        recycle(self.car_parts)
        Vehicle.__del__(self)

class SportsCar(Car, Vehicle):

    def __del__(self):
        recycle(self.sports_car_parts)
        Vehicle.__del__(self)""",
        "fix": """"""
    },
    {
        "id": 71,
        "name": "Missing call to __init__ during object initialization",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-missing-call-to-init/",
        "code": """
class Vehicle(object):

    def __init__(self):
        self.mobile = True

class Car(Vehicle):

    def __init__(self):
        Vehicle.__init__(self)
        self.car_init()

class SportsCar(Car, Vehicle):

    def __init__(self):
        Vehicle.__init__(self)
        self.sports_car_init()""",
        "fix": """"""
    },
    {
        "id": 72,
        "name": "Missing named arguments in formatting call",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-str-format-missing-named-argument/",
        "code": """def unsafe_named_format():
    the_format = "{spam} {eggs}"
    if unlikely_condition():
        return the_format.format(spam="spam", completely_different="eggs")
    else:
        return the_format.format(spam="spam", eggs="eggs")""",
        "fix": """"""
    },
    {
        "id": 73,
        "name": "Missing part of special group in regular expression",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-regex-incomplete-special-group/",
        "code": """import re
matcher = re.compile(r'(P<name>[\w]+)')

def only_letters(text):
    m = matcher.match(text)
    if m:
        print("Letters are: " + m.group('name'))
""",
        "fix": """fixed_matcher = re.compile(r'(?P<name>[\w]+)')"""
    },
    {
        "id": 74,
        "name": "Modification of dictionary returned by locals()",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-modification-of-locals/",
        "code": """def modifies_locals_sum(x, y):
    locals()['z'] = x + y
    return z
""",
        "fix": """def fixed_sum(x, y):
    z = x + y
    return z"""
    },
    {
        "id": 75,
        "name": "Modification of parameter with default",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-modification-of-default-value/",
        "code": """    def __init__(self, name, choices=[], default=[], shortDesc=None,
                 longDesc=None, hints=None, allowNone=1):
        self.choices = choices
        if choices and not default:
            default.append(choices[0][1])
        Argument.__init__(self, name, default, shortDesc, longDesc, hints, allowNone=allowNone)""",
        "fix": """"""
    },
    {
        "id": 76,
        "name": "Module imports itself",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-import-own-module/",
        "code": """import ModuleImportsItself

def factorial(n):
    if n <= 0:
        return 1
    return n * ModuleImportsItself.factorial(n - 1)""",
        "fix": """def factorial(n):
    if n <= 0:
        return 1
    return n * factorial(n - 1)"""
    },
    {
        "id": 79,
        "name": "Module-level cyclic import",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-unsafe-cyclic-import/",
        "code": """# Module A
import module_b

def function_a():
    module_b.function_b()

# Module B
import module_a

def function_b():
    module_a.function_a()""",
        "fix": """"""
    },
    {
        "id": 80,
        "name": "Multiple calls to __del__ during object destruction",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-multiple-calls-to-delete/",
        "code": """
class Vehicle(object):

    def __del__(self):
        recycle(self.base_parts)


class Car(Vehicle):

    def __del__(self):
        recycle(self.car_parts)
        Vehicle.__del__(self)


class SportsCar(Car, Vehicle):

    def __del__(self):
        recycle(self.sports_car_parts)
        Car.__del__(self)
        Vehicle.__del__(self)""",
        "fix": """"""
    },
    {
        "id": 81,
        "name": "Multiple calls to __init__ during object initialization",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-multiple-calls-to-init/",
        "code": """
class Vehicle(object):

    def __init__(self):
        self.mobile = True

class Car(Vehicle):

    def __init__(self):
        Vehicle.__init__(self)
        self.car_init()

    def car_init(self):
        pass

class SportsCar(Car, Vehicle):

    def __init__(self):
        Vehicle.__init__(self)
        Car.__init__(self)
        self.sports_car_init()

    def sports_car_init(self):
        pass
""",
        "fix": """"""
    },
    {
        "id": 82,
        "name": "Mutation of descriptor in __get__ or __set__ method.",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-mutable-descriptor/",
        "code": """
class MutatingDescriptor(object):

    def __init__(self, func):
        self.my_func = func

    def __get__(self, obj, obj_type):
        self.my_obj = obj
        return self

    def __call__(self, *args):
        return self.my_func(self.my_obj, *args)

def show(obj):
    print (obj)

class C(object):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return ("C: " + str(self.value))

    show = MutatingDescriptor(show)

c1 = C(1)
c1.show()
c2 = C(2)
c2.show()
c1_show = c1.show
c2.show
c1_show()
""",
        "fix": """import types

class NonMutatingDescriptor(object):

    def __init__(self, func):
        self.my_func = func

    def __get__(self, obj, obj_type):
        return types.MethodType(self.my_func, obj)

def show(obj):
    print (obj)

class C(object):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return ("C: " + str(self.value))

    show = NonMutatingDescriptor(show)

c1 = C(1)
c1.show()
c2 = C(2)
c2.show()
c1_show = c1.show
c2.show
c1_show()
"""
    },
    {
        "id": 83,
        "name": "Nested loops with same variable",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-nested-loops-with-same-variable/",
        "code": """for var in range(3):
    for var in range(3):
        pass
    print (var)
""",
        "fix": """"""
    },
    {
        "id": 84,
        "name": "Nested loops with same variable reused after inner loop body",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-nested-loops-with-same-variable-reused/",
        "code": """def largest_elements(l):
    for x in l:
        maxnum = 0
        for x in x:
            maxnum = max(x, maxnum)
        print "The largest element in the list", x, "is", maxnum""",
        "fix": """def largest_elements_correct(l):
    for x in l:
        maxnum = 0
        for y in x:
            maxnum = max(y, maxnum)
        print "The largest element in the list", x, "is", maxnum"""
    },
    {
        "id": 85,
        "name": "NoSQL Injection",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-nosql-injection/",
        "code": """from flask import Flask, request
from flask_pymongo import PyMongo
import json

mongo = PyMongo(app)


@app.route("/")
def home_page():
    unsanitized_search = request.args['search']
    json_search = json.loads(unsanitized_search)

    result = mongo.db.user.find({'name': json_search})""",
        "fix": """from flask import Flask, request
from flask_pymongo import PyMongo
from mongosanitizer.sanitizer import sanitize
import json

mongo = PyMongo(app)


@app.route("/")
def home_page():
    unsafe_search = request.args['search']
    json_search = json.loads(unsafe_search)
    safe_search = sanitize(unsanitized_search)

    result = client.db.collection.find_one({'data': safe_search})"""
    },
    {
        "id": 87,
        "name": "Non-exception in 'except' clause",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-useless-except/",
        "code": """def handle_int():
    try:
        raise_int()
    except int:
        print("This will never be printed")
""",
        "fix": """"""
    },
    {
        "id": 88,
        "name": "Non-iterable used in for loop",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-non-iterable-in-for-loop/",
        "code": """
def illegal_for_loop(seq = None):
    for x in seq:
        print (x)""",
        "fix": """"""
    },
    {
        "id": 90,
        "name": "NotImplemented is not an Exception",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-raise-not-implemented/",
        "code": """class Abstract(object):

    def wrong(self):
        raise NotImplemented()

    def right(self):
        raise NotImplementedError()""",
        "fix": """"""
    },
    {
        "id": 91,
        "name": "Overly complex __del__ method",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-overly-complex-delete/",
        "code": """
class CachedPreferencesFile

    ...

    def __del__(self):
        for key, value in self.preferences.items():
            self.write_pair(key, value)
        self.backing.close()""",
        "fix": """
class CachedPreferencesFile

    ...

    def close(self):
        for key, value in self.preferences.items():
            self.write_pair(key, value)
        self.backing.close()

    def __del__(self):
        self.close()"""
    },
    {
        "id": 92,
        "name": "Overly permissive file permissions",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-overly-permissive-file/",
        "code": """import os

file_path = "sensitive_data.txt"
with open(file_path, "w") as file:
    file.write("This is sensitive information.")

os.chmod(file_path, 0o777)

permissions = oct(os.stat(file_path).st_mode & 0o777)
print("File Permissions:", permissions)""",
        "fix": """import os

file_path = "sensitive_data.txt"
with open(file_path, "w") as file:
    file.write("This is sensitive information.")

os.chmod(file_path, 0o600)

permissions = oct(os.stat(file_path).st_mode & 0o777)
print("File Permissions:", permissions)"""
    },
    {
        "id": 93,
        "name": "Overly permissive regular expression range",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-overly-large-range/",
        "code": """
import re
def is_valid_hex_color(color):
    return re.match(r'^#[0-9a-fA-f]{6}$', color) is not None""",
        "fix": """
import re
def is_valid_hex_color(color):
    return re.match(r'^#[0-9a-fA-F]{6}$', color) is not None"""
    },
    {
        "id": 94,
        "name": "Overwriting attribute in super-class or sub-class",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-overwritten-inherited-attribute/",
        "code": """
class C(object):

    def __init__(self):
        self.var = 0

class D(C):

    def __init__(self):
        self.var = 1
        C.__init__(self)

class E(object):

    def __init__(self):
        self.var = 0

class F(E):

    def __init__(self):
        E.__init__(self)
        self.var = 1""",
        "fix": """
class G(object):

    def __init__(self, var = 0):
        self.var = var

class H(G):

    def __init__(self):
        G.__init__(self, 1)"""
    },
    {
        "id": 96,
        "name": "Partial server-side request forgery",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-partial-ssrf/",
        "code": """import requests
from flask import Flask, request

app = Flask(__name__)

@app.route("/full_ssrf")
def full_ssrf():
    target = request.args["target"]

    resp = requests.get("https://" + target + ".example.com/data/")""",
        "fix": """"""
    },
    {
        "id": 99,
        "name": "Property in old-style class",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-property-in-old-style-class/",
        "code": """class OldStyle:

    def __init__(self, x):
        self._x = x

    @property
    def x(self):
        return self._x


class InheritOldStyle(OldStyle):

    def __init__(self, x):
        self._x = x

    @property
    def x(self):
        return self._x
""",
        "fix": """class NewStyle(object):

    def __init__(self, x):
        self._x = x

    @property
    def x(self):
        return self._x

class InheritNewStyle(NewStyle):

    def __init__(self, x):
        self._x = x

    @property
    def x(self):
        return self._x"""
    },
    {
        "id": 100,
        "name": "Pythagorean calculation with sub-optimal numerics",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-pythagorean/",
        "code": """from math import sqrt, hypot

a = 3e154
b = 4e154

def longSideDirect():
    return sqrt(a**2 + b**2)""",
        "fix": """
def longSideBuiltin():
    return hypot(a, b)"""
    },
    {
        "id": 101,
        "name": "Raising a tuple",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-raises-tuple/",
        "code": """def raise_tuple():
    ex = Exception, "Important diagnostic information"
    raise ex""",
        "fix": """def fixed_raise_tuple1():
    ex = Exception("Important diagnostic information")
    raise ex


def fixed_raise_tuple2():
    raise Exception, "Important diagnostic information" """
    },
    {
        "id": 102,
        "name": "Redundant assignment",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-redundant-assignment/",
        "code": """class Spam:

    def __init__(self, eggs):
        eggs = eggs""",
        "fix": """"""
    },
    {
        "id": 103,
        "name": "Redundant comparison",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-redundant-comparison/",
        "code": """  class KeySorter:

      def __init__(self, obj):
          self.obj = obj

      def __lt__(self, other):
          return self._compare(self.obj, other.obj) < 0

      def _compare(self, obj1, obj2):
          if obj1 < obj2:
              return -1
          elif obj1 < obj2:
              return 1
          else:
              return 0""",
        "fix": """"""
    },
    {
        "id": 104,
        "name": "Reflected server-side cross-site scripting",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-reflective-xss/",
        "code": """from flask import Flask, request, make_response, escape

app = Flask(__name__)

@app.route('/unsafe')
def unsafe():
    first_name = request.args.get('name', '')
    return make_response("Your name is " + first_name)""",
        "fix": """@app.route('/safe')
def safe():
    first_name = request.args.get('name', '')
    return make_response("Your name is " + escape(first_name))"""
    },
    {
        "id": 105,
        "name": "Regular expression injection",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-regex-injection/",
        "code": """from flask import request, Flask
import re


@app.route("/direct")
def direct():
    unsafe_pattern = request.args["pattern"]
    re.search(unsafe_pattern, "")


@app.route("/compile")
def compile():
    unsafe_pattern = request.args["pattern"]
    compiled_pattern = re.compile(unsafe_pattern)
    compiled_pattern.search("")""",
        "fix": """from flask import request, Flask
import re


@app.route("/direct")
def direct():
    unsafe_pattern = request.args['pattern']
    safe_pattern = re.escape(unsafe_pattern)
    re.search(safe_pattern, "")


@app.route("/compile")
def compile():
    unsafe_pattern = request.args['pattern']
    safe_pattern = re.escape(unsafe_pattern)
    compiled_pattern = re.compile(safe_pattern)
    compiled_pattern.search("")"""
    },
    {
        "id": 106,
        "name": "Request without certificate validation",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-request-without-cert-validation/",
        "code": """import requests

requests.get('https://semmle.com', verify=False)
requests.get('https://semmle.com', verify=0)""",
        "fix": """

requests.get('https://semmle.com', verify=True)
requests.get('https://semmle.com', verify="/path/to/cert/")
requests.get('https://semmle.com')

def make_safe_request(url, verify_cert):
    if not verify_cert:
        raise Exception("Trying to make unsafe request")
    return requests.get(url, verify_cert)"""
    },
    {
        "id": 107,
        "name": "Result of integer division may be truncated",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-truncated-division/",
        "code": """def average(l):
    return sum(l) / len(l)

print average([1.0, 2.0])".
print average([1, 2])""",
        "fix": """from __future__ import division

def average(l):
    return sum(l) / len(l)

print average([1.0, 2.0])
print average([1, 2])"""
    },
    {
        "id": 108,
        "name": "Returning tuples with varying lengths",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-mixed-tuple-returns/",
        "code": """def sum_length_product1(l):
    if l == []:
        return 0, 0
    else:
        val = l[0]
        restsum, restlength, restproduct = sum_length_product1(l[1:])
        return restsum + val, restlength + 1, restproduct * val""",
        "fix": """
def sum_length_product2(l):
    if l == []:
        return 0, 0, 1
    else:
        val = l[0]
        restsum, restlength, restproduct = sum_length_product2(l[1:])
        return restsum + val, restlength + 1, restproduct * val"""
    },
    {
        "id": 109,
        "name": "SQL query built from user-controlled sources",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-sql-injection/",
        "code": """from django.conf.urls import url
from django.db import connection


def show_user(request, username):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM users WHERE username = '%s'" % username)
        user = cursor.fetchone()

urlpatterns = [url(r'^users/(?P<username>[^/]+)$', show_user)]""",
        "fix": """"""
    },
    {
        "id": 110,
        "name": "Should use a 'with' statement",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-should-use-with/",
        "code": """
f = open("filename")
try:
    f.write(...)
finally:
    f.close()""",
        "fix": """with open("filename") as f:
    f.write(...)"""
    },
    {
        "id": 111,
        "name": "Signature mismatch in overriding method",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-inheritance-signature-mismatch/",
        "code": """
def runsource(self, source, filename="<input>", symbol="single"):
    ... # Definition

def runsource(self, source):
    ... # Definition""",
        "fix": """"""
    },
    {
        "id": 112,
        "name": "Special method has incorrect signature",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-special-method-wrong-signature/",
        "code": """class Point(object):

   def __init__(self, x, y):
       self.x
       self.y

   def __add__(self, other):
       if not isinstance(other, Point):
           return NotImplemented
       return Point(self.x + other.x, self.y + other.y)

   def __str__(self, style):
       if style == 'polar':
           u"%s @ %s\u00b0" % (abs(self), self.angle())
       else:
           return "[%s, %s]" % (self.x, self.y)""",
        "fix": """"""
    },
    {
        "id": 113,
        "name": "Statement has no effect",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-ineffectual-statement/",
        "code": """def increment_and_show(x):
    ++x
    x.show""",
        "fix": """"""
    },
    {
        "id": 114,
        "name": "Superclass attribute shadows subclass method",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-attribute-shadows-method/",
        "code": """class Mammal(object):

    def __init__(self, milk = 0):
        self.milk = milk


class Cow(Mammal):

    def __init__(self):
        Mammal.__init__(self)

    def milk(self):
        return "Milk"
""",
        "fix": """"""
    },
    {
        "id": 115,
        "name": "Suspicious unused loop iteration variable",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-unused-loop-variable/",
        "code": """def test():
    for t in [TypeA, TypeB]:
        x = TypeA()
        run_test(x)""",
        "fix": """def test():
    for t in [TypeA, TypeB]:
        x = t
        run_test(x)"""
    },
    {
        "id": 116,
        "name": "Syntax error",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-syntax-error/",
        "code": """def greet():
    print("Hello, World!")
    print("Welcome to Python!")

greet()()""",
        "fix": """"""
    },
    {
        "id": 117,
        "name": "Testing equality to None",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-test-equals-none/",
        "code": """def filter1(function, iterable=None)
    if iterable == None:
        return [item for item in iterable if item]
    else:
        return [item for item in iterable if function(item)]""",
        "fix": """def filter2(function, iterable=None)
    if iterable is None:
        return [item for item in iterable if item]
    else:
        return [item for item in iterable if function(item)]"""
    },
    {
        "id": 118,
        "name": "Too few arguments in formatting call",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-str-format-missing-argument/",
        "code": """def unsafe_format():
    the_format = "{} {} {}"
    if unlikely_condition():
        return the_format.format(1, 2)
    else:
        return the_format.format(1, 2, 3)""",
        "fix": """"""
    },
    {
        "id": 119,
        "name": "URL redirection from remote source",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-url-redirection/",
        "code": """from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/')
def hello():
    target = request.args.get('target', '')
    return redirect(target, code=302)""",
        "fix": """from flask import Flask, request, redirect

VALID_REDIRECT = "http://cwe.mitre.org/data/definitions/601.html"

app = Flask(__name__)

@app.route('/')
def hello():
    target = request.args.get('target', '')
    if target == VALID_REDIRECT:
        return redirect(target, code=302)
    else:
        return redirect('/', code=302)"""
    },
    {
        "id": 120,
        "name": "Uncontrolled command line",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-command-line-injection/",
        "code": """
urlpatterns = [
    url(r'^command-ex1$', command_execution_unsafe, name='command-execution-unsafe'),
    url(r'^command-ex2$', command_execution_safe, name='command-execution-safe')
]

COMMANDS = {
    "list" :"ls",
    "stat" : "stat"
}

def command_execution_unsafe(request):
    if request.method == 'POST':
        action = request.POST.get('action', '')
        subprocess.call(["application", action])""",
        "fix": """def command_execution_safe(request):
    if request.method == 'POST':
        action = request.POST.get('action', '')
        subprocess.call(["application", COMMANDS[action]])"""
    },
    {
        "id": 121,
        "name": "Uncontrolled data used in path expression",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-path-injection/",
        "code": """import os.path
from flask import Flask, request, abort

app = Flask(__name__)

@app.route("/user_picture1")
def user_picture1():
    filename = request.args.get('p')
    data = open(filename, 'rb').read()
    return data

@app.route("/user_picture2")
def user_picture2():
    base_path = '/server/static/images'
    filename = request.args.get('p')
    data = open(os.path.join(base_path, filename), 'rb').read()
    return data""",
        "fix": """@app.route("/user_picture3")
def user_picture3():
    base_path = '/server/static/images'
    filename = request.args.get('p')
    fullpath = os.path.normpath(os.path.join(base_path, filename))
    if not fullpath.startswith(base_path):
        raise Exception("not allowed")
    data = open(fullpath, 'rb').read()
    return data"""
    },
    {
        "id": 122,
        "name": "Unguarded next in generator",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-unguarded-next-in-generator/",
        "code": """test_files = [
    ["header1", "text10", "text11", "text12"],
    ["header2", "text20", "text21", "text22"],
    [],
    ["header4", "text40", "text41", "text42"],
]

def separate_headers(files):
    for file in files:
        lines = iter(file)
        header = next(lines)
        body = [ l for l in lines ]
        yield header, body

def process_files(files):
    for header, body in separate_headers(files):
        print(format_page(header, body))""",
        "fix": """def separate_headers(files):
    for file in files:
        lines = iter(file)
        try:
            header = next(lines)
        except StopIteration:
            continue
        body = [ l for l in lines ]
        yield header, body"""
    },
    {
        "id": 123,
        "name": "Unhashable object hashed",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-hash-unhashable-value/",
        "code": """def lookup_with_default_key(mapping, key=None):
    if key is None:
        key = []
    return mapping[key]""",
        "fix": """"""
    },
    {
        "id": 124,
        "name": "Unmatchable caret in regular expression",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-regex-unmatchable-caret/",
        "code": """import re
matcher = re.compile(r"\[^.]*\.css")

def find_css(filename):
    if matcher.match(filename):
        print("Found it!")
""",
        "fix": """"""
    },
    {
        "id": 125,
        "name": "Unmatchable dollar in regular expression",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-regex-unmatchable-dollar/",
        "code": """import re
matcher = re.compile(r"\.\(\w+$\)")

def find_it(filename):
    if matcher.match(filename):
        print("Found it!")""",
        "fix": """
fixed_matcher = re.compile(r"\.\(\w+\)$")"""
    },
    {
        "id": 126,
        "name": "Unnecessary 'else' clause in loop",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-redundant-else/",
        "code": """def pointless_else(container):
    for item in container:
        if of_interest(item):
            return item
    else:
        raise NotFoundException()""",
        "fix": """def no_else(container):
    for item in container:
        if of_interest(item):
            return item
    raise NotFoundException()"""
    },
    {
        "id": 127,
        "name": "Unnecessary delete statement in function",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-unnecessary-delete/",
        "code": """def unnecessary_delete():
    x = get_some_object()
    do_calculation(x)
    del x""",
        "fix": """"""
    },
    {
        "id": 128,
        "name": "Unnecessary lambda",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-unnecessary-lambda/",
        "code": """import math

def call_with_x_squared(x, function):
    x = x*x
    return function(x)

print call_with_x_squared(2, lambda x: math.factorial(x))""",
        "fix": """import math

def call_with_x_squared(x, function):
    x = x*x
    return function(x)

print call_with_x_squared(2, math.factorial)"""
    },
    {
        "id": 129,
        "name": "Unnecessary pass",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-unnecessary-pass/",
        "code": """def calculate_average(numbers):
    pass

number_list = [1, 2, 3, 4, 5]

average = calculate_average(number_list)
print("Average:", average)""",
        "fix": """def calculate_average(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return average

number_list = [1, 2, 3, 4, 5]

average = calculate_average(number_list)
print("Average:", average)"""
    },
    {
        "id": 130,
        "name": "Unreachable 'except' block",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-unreachable-except/",
        "code": """def incorrect_except_order(val):
    try:
        val.attr
    except Exception:
        print ("Exception")
    except AttributeError:
        print ("AttributeError")""",
        "fix": """"""
    },
    {
        "id": 131,
        "name": "Unreachable code",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-unreachable-statement/",
        "code": """import math

def my_div(x, y):
    return math.floor(x / y)
    remainder = x - math.floor(x / y) * y""",
        "fix": """"""
    },
    {
        "id": 132,
        "name": "Unsafe shell command constructed from library input",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-shell-command-constructed-from-input/",
        "code": """import os

def download(path): 
    os.system("wget " + path)""",
        "fix": """import subprocess

def download(path): 
    subprocess.run(["wget", path])"""
    },
    {
        "id": 133,
        "name": "Unsupported format character",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-percent-format-unsupported-character/",
        "code": """def format_as_tuple_incorrect(args):
    return "%t" % args""",
        "fix": """def format_as_tuple_correct(args):
    return "%r" % (args,)"""
    },
    {
        "id": 134,
        "name": "Unused argument in a formatting call",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-str-format-surplus-argument/",
        "code": """def surplus_argument():
    the_format = "{} {}"
    return the_format.format(1, 2, 3)""",
        "fix": """def surplus_argument():
    the_format = "{} {}"
    return the_format.format(1, 2)"""
    },
    {
        "id": 135,
        "name": "Unused exception object",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-unused-exception-object/",
        "code": """def do_action_forgotten_raise(action):
    if action == "go":
        start()
    elif action == "stop":
        stop()
    else:
        ValueError(action)""",
        "fix": """def do_action(action):
    if action == "go":
        start()
    elif action == "stop":
        stop()
    else:
        raise ValueError(action)"""
    },
    {
        "id": 136,
        "name": "Unused global variable",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-unused-global-variable/",
        "code": """import random

def write_random_to_file():
    no = random.randint(1, 10)
    with open("random.txt", "w") as file:
        file.write(str(no))
    return no

random_no = write_random_to_file()""",
        "fix": """import random

def write_random_to_file():
    no = random.randint(1, 10)
    with open("random.txt", "w") as file:
        file.write(str(no))
    return no

write_random_to_file()"""
    },
    {
        "id": 137,
        "name": "Unused import",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-unused-import/",
        "code": """import math

def calculate_square(x):
    return x * x

result = calculate_square(5)
print("Square:", result)""",
        "fix": """def calculate_square(x):
    return x * x

result = calculate_square(5)
print("Square:", result)"""
    },
    {
        "id": 138,
        "name": "Unused local variable",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-unused-local-variable/",
        "code": """import random

def write_random_to_file():
    no = random.randint(1, 10)
    with open("random.txt", "w") as file:
        file.write(str(no))
    return no

def write_random():
    random_no = write_random_to_file()
    print "A random number was written to random.txt" """,
        "fix": """import random

def write_random_to_file():
    no = random.randint(1, 10)
    with open("random.txt", "w") as file:
        file.write(str(no))
    return no

def write_random():
    write_random_to_file()
    print "A random number was written to random.txt" """
    },
    {
        "id": 139,
        "name": "Unused named argument in formatting call",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-str-format-surplus-named-argument/",
        "code": """def surplus_argument():
    the_format = "{spam} {eggs}"
    return the_format.format(spam = "spam", eggs="eggs", chips="chips")""",
        "fix": """"""
    },
    {
        "id": 141,
        "name": "Use of 'return' or 'yield' outside a function",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-return-or-yield-outside-function/",
        "code": """
class InvalidClass1(object):
    if [1, 2, 3]:
        return "Exists"

for i in [1, 2, 3]:
    yield i""",
        "fix": """"""
    },
    {
        "id": 142,
        "name": "Use of a broken or weak cryptographic algorithm",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-weak-cryptographic-algorithm/",
        "code": """from Crypto.Cipher import DES, AES

cipher = DES.new(SECRET_KEY)

def send_encrypted(channel, message):
    channel.send(cipher.encrypt(message))""",
        "fix": """cipher = AES.new(SECRET_KEY)

def send_encrypted(channel, message):
    channel.send(cipher.encrypt(message))"""
    },
    {
        "id": 144,
        "name": "Use of a print statement at module level",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-print-during-import/",
        "code": """try:
    import fast_system as system
except ImportError:
    print ("Cannot import fast system, falling back on slow system")
    import slow_system as system""",
        "fix": """import logging

try:
    import fast_system as system
except ImportError:
    logging.info("Cannot import fast system, falling back on slow system")
    import slow_system as system"""
    },
    {
        "id": 145,
        "name": "Use of an undefined placeholder variable",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-undefined-placeholder-variable/",
        "code": """d1= "a"
d2= "b"
print("I have {d1} and {d2} and {d3}". format(d1, d2, d3))""",
        "fix": """d1= "a"
d2= "b"
d3= "c"
print("I have {d1} and {d2} and {d3}". format(d1, d2, d3))"""
    },
    {
        "id": 146,
        "name": "Use of exit() or quit()",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-use-of-exit-or-quit/",
        "code": """def main():
    try:
        process()
    except Exception as ex:
        print(ex)
        exit(1)""",
        "fix": """import sys

def main():
    try:
        process()
    except Exception as ex:
        print(ex)
        sys.exit(1)"""
    },
    {
        "id": 147,
        "name": "Use of insecure SSL/TLS version",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-insecure-protocol/",
        "code": """import ssl
import socket

ssl.wrap_socket(socket.socket(), ssl_version=ssl.PROTOCOL_SSLv2)

context = ssl.SSLContext(ssl_version=ssl.PROTOCOL_SSLv3)

from pyOpenSSL import SSL

context = SSL.Context(SSL.TLSv1_METHOD)""",
        "fix": """import ssl

context = ssl.SSLContext()
context.options |= ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1

context = ssl.create_default_context()
context.minimum_version = ssl.TLSVersion.TLSv1_2"""
    },
    {
        "id": 148,
        "name": "Use of the return value of a procedure",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-procedure-return-value-used/",
        "code": """
import sys

def my_print(*args):
    print (args)

def main():
    err = my_print(sys.argv)
    if err:
        sys.exit(err)""",
        "fix": """
def main():
    my_print(sys.argv)
    #The rest of the code can be removed as None as always false"""
    },
    {
        "id": 151,
        "name": "Wrong name for an argument in a call",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-call-wrong-named-argument/",
        "code": """def calculate_area(length, width):
    return length * width

result = calculate_area(length=5, height=10)
print(result)""",
        "fix": """def calculate_area(length, width):
    return length * width

result = calculate_area(length=5, width=10)
print(result)"""
    },
    {
        "id": 152,
        "name": "Wrong name for an argument in a class instantiation",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-call-wrong-named-class-argument/",
        "code": """class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(x=1, yy=2)""",
        "fix": """"""
    },
    {
        "id": 153,
        "name": "Wrong number of arguments for format",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-percent-format-wrong-arguments/",
        "code": """def unsafe_format():
    if unlikely_condition():
        args = (1,2)
    else:
        args = (1, 2, 3)
    return "%s %s %s" % args""",
        "fix": """"""
    },
    {
        "id": 154,
        "name": "Wrong number of arguments in a call",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-call-wrong-arguments/",
        "code": """def greet(name):
    return f"Hello, {name}!"

result = greet("Alice", "Smith")
print(result)""",
        "fix": """def greet(name):
    return f"Hello, {name}!"

result = greet("Alice")
print(result)"""
    },
    {
        "id": 155,
        "name": "Wrong number of arguments in a class instantiation",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-call-wrong-number-class-arguments/",
        "code": """class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(1)
p = Point(1,2,3)""",
        "fix": """"""
    },
    {
        "id": 156,
        "name": "XML external entity expansion",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-xxe/",
        "code": """from flask import Flask, request
import lxml.etree

app = Flask(__name__)

@app.post("/upload")
def upload():
    xml_src = request.get_data()
    doc = lxml.etree.fromstring(xml_src)
    return lxml.etree.tostring(doc)""",
        "fix": """from flask import Flask, request
import lxml.etree

app = Flask(__name__)

@app.post("/upload")
def upload():
    xml_src = request.get_data()
    parser = lxml.etree.XMLParser(resolve_entities=False)
    doc = lxml.etree.fromstring(xml_src, parser=parser)
    return lxml.etree.tostring(doc)"""
    },
    {
        "id": 157,
        "name": "XML internal entity expansion",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-xml-bomb/",
        "code": """from flask import Flask, request
import xml.etree.ElementTree as ET

app = Flask(__name__)

@app.post("/upload")
def upload():
    xml_src = request.get_data()
    doc = ET.fromstring(xml_src)
    return ET.tostring(doc)""",
        "fix": """from flask import Flask, request
import defusedxml.ElementTree as ET

app = Flask(__name__)

@app.post("/upload")
def upload():
    xml_src = request.get_data()
    doc = ET.fromstring(xml_src)
    return ET.tostring(doc)"""
    },
    {
        "id": 158,
        "name": "XPath query built from user-controlled sources",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-xpath-injection/",
        "code": """from lxml import etree
from io import StringIO

from django.urls import path
from django.http import HttpResponse
from django.template import Template, Context, Engine, engines


def a(request):
    value = request.GET['xpath']
    f = StringIO('<foo><bar></bar></foo>')
    tree = etree.parse(f)
    r = tree.xpath("/tag[@id='%s']" % value)


urlpatterns = [
    path('a', a)
]""",
        "fix": """from lxml import etree
from io import StringIO

from django.urls import path
from django.http import HttpResponse
from django.template import Template, Context, Engine, engines


def a(request):
    value = request.GET['xpath']
    f = StringIO('<foo><bar></bar></foo>')
    tree = etree.parse(f)
    r = tree.xpath("/tag[@id=$tagid]", tagid=value)


urlpatterns = [
    path('a', a)
]"""
    },
    {
        "id": 159,
        "name": "__del__ is called explicitly",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-explicit-call-to-delete/",
        "code": """def extract_bad(zippath, dest):
    zipped = ZipFile(zippath)
    try:
        zipped.extractall(dest)
    finally:
        zipped.__del__()""",
        "fix": """def extract_good(zippath, dest):
    zipped = ZipFile(zippath)
    try:
        zipped.extractall(dest)
    finally:
        zipped.close()"""
    },
    {
        "id": 160,
        "name": "__eq__ not overridden when adding attributes",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-missing-equals/",
        "code": """class Point(object):

    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __repr__(self):
        return 'Point(%r, %r)' % (self._x, self._y)

    def __eq__(self, other):
        if not isinstance(other, Point):
            return False
        return self._x == other._x and self._y == other._y

class ColorPoint(Point):

    def __init__(self, x, y, color):
        Point.__init__(self, x, y)
        self._color = color

    def __repr__(self):
        return 'ColorPoint(%r, %r)' % (self._x, self._y, self._color)
""",
        "fix": """
class ColorPoint(Point):

    def __init__(self, x, y, color):
        Point.__init__(self, x, y)
        self._color = color

    def __repr__(self):
        return 'ColorPoint(%r, %r)' % (self._x, self._y, self._color)

    def __eq__(self, other):
        if not isinstance(other, ColorPoint):
            return False
        return Point.__eq__(self, other) and self._color = other._color"""
    },
    {
        "id": 161,
        "name": "__init__ method calls overridden method",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-init-calls-subclass/",
        "code": """
class Super(object):

    def __init__(self, arg):
        self._state = "Not OK"
        self.set_up(arg)
        self._state = "OK"

    def set_up(self, arg):
        "Do some set up"

class Sub(Super):

    def __init__(self, arg):
        Super.__init__(self, arg)
        self.important_state = "OK"

    def set_up(self, arg):
        Super.set_up(self, arg)
        #Do some more set up""",
        "fix": """
class Super(object):

    def __init__(self, arg):
        self._state = "Not OK"
        self.super_set_up(arg)
        self._state = "OK"

    def super_set_up(self, arg):
        #Do some set up


class Sub(Super):

    def __init__(self, arg):
        Super.__init__(self, arg)
        self.sub_set_up(self, arg)
        self.important_state = "OK"


    def sub_set_up(self, arg):
        #Do some more set up """
    },
    {
        "id": 162,
        "name": "__init__ method is a generator",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-init-method-is-generator/",
        "code": """class InitIsGenerator(object):
    def __init__(self, i):
        yield i""",
        "fix": """"""
    },
    {
        "id": 163,
        "name": "__init__ method returns a value",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-explicit-return-in-init/",
        "code": """class ExplicitReturnInInit(object):
    def __init__(self, i):
        self.i = i
        return self""",
        "fix": """"""
    },
    {
        "id": 164,
        "name": "__iter__ method returns a non-iterator",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-iter-returns-non-iterator/",
        "code": """class MyRange(object):
    def __init__(self, low, high):
        self.low = low
        self.high = high

    def __iter__(self):
        return MyRangeIterator(self.low, self.high)

    def skip(self, to_skip):
        return MyRangeIterator(self.low, self.high, to_skip)

class MyRangeIterator(object):
    def __init__(self, low, high, skip=None):
        self.current = low
        self.high = high
        self.skip = skip

    def __next__(self):
        if self.current >= self.high:
            raise StopIteration
        to_return = self.current
        self.current += 1
        if self.skip and to_return in self.skip:
            return self.__next__()
        return to_return

my_range = MyRange(0,10)
x = sum(my_range)
y = sum(my_range.skip({6,9}))""",
        "fix": """class MyRange(object):
    def __init__(self, low, high):
        self.low = low
        self.high = high

    def __iter__(self):
        return MyRangeIterator(self.low, self.high)

    def skip(self, to_skip):
        return MyRangeIterator(self.low, self.high, to_skip)

class MyRangeIterator(object):
    def __init__(self, low, high, skip=None):
        self.current = low
        self.high = high
        self.skip = skip

    def __next__(self):
        if self.current >= self.high:
            raise StopIteration
        to_return = self.current
        self.current += 1
        if self.skip and to_return in self.skip:
            return self.__next__()
        return to_return

    def __iter__(self):
        return self

my_range = MyRange(0,10)
x = sum(my_range)
y = sum(my_range.skip({6,9}))"""
    },
    {
        "id": 165,
        "name": "__slots__ in old-style class",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/python/py-slots-in-old-style-class/",
        "code": """class Point:

    __slots__ = [ '_x', '_y' ]

    def __init__(self, x, y):
        self._x = x
        self._y = y
""",
        "fix": """class Point2(object):

    __slots__ = [ '_x', '_y' ]

    def __init__(self, x, y):
        self._x = x
        self._y = y"""
    }
]