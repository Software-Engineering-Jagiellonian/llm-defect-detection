understanding = [
    {
        "id": 1,
        "name": "recursively computing the fibonacci sequence",
        "correct": True,
        "issues": [

        ],
        "link": "",
        "code": """def fibonacci(n):
  if n <= 1:
    return n
  else:
    return fibonacci(n-1) + fibonacci(n-2)"""
    },
    {
        "id": 2,
        "name": "recursively computing the fibonacci sequence",
        "correct": False,
        "issues": [
"Changed the condition to n <= 0"
        ],
        "link": "",
        "code": """def fibonacci(n):
  if n <= 0:
    return n
  else:
    return fibonacci(n-1) + fibonacci(n-2)"""
    },
    {
        "id": 3,
        "name": "quine function",
        "correct": True,
        "issues": [

        ],
        "link": "https://rosettacode.org/wiki/Quine#Python",
        "code": """exec(c:="print(f'exec(c:={chr(34)+c+chr(34)})')")"""
    },
    {
        "id": 4,
        "name": "quine function",
        "correct": False,
        "issues": [
"char(36) will print '$' instead of quotation marks"
        ],
        "link": "https://rosettacode.org/wiki/Quine#Python",
        "code": """exec(c:="print(f'exec(c:={chr(36)+c+chr(36)})')")"""
    },
    {
        "id": 5,
        "name": "currying and partial application",
        "correct": True,
        "issues": [

        ],
        "link": "",
        "code": """def curry(func, *args):
  def inner(*more_args):
    return func(*args, *more_args)
  return inner

def add(a, b):
  return a + b

doubled = curry(add, 2)"""
    },
    {
        "id": 6,
        "name": "currying and partial application",
        "correct": False,
        "issues": [
"Missing args and more_args destructuring"
        ],
        "link": "",
        "code": """def curry(func, *args):
  def inner(*more_args):
    return func(args, more_args)
  return inner

def add(a, b):
  return a + b

doubled = curry(add, 2)"""
    },
    {
        "id": 7,
        "name": "higher-order functions and function composition",
        "correct": True,
        "issues": [

        ],
        "link": "",
        "code": """def compose(*funcs):
  return lambda x: reduce(lambda acc, f: f(acc), funcs, x)

def square(x):
  return x * x

def increment(x):
  return x + 1

double_then_square = compose(increment, square)"""
    },
    {
        "id": 8,
        "name": "higher-order functions and function composition",
        "correct": False,
        "issues": [
"Switched the order of functions"
        ],
        "link": "",
        "code": """def compose(*funcs):
  return lambda x: reduce(lambda acc, f: f(acc), funcs, x)

def square(x):
  return x * x

def increment(x):
  return x + 1

double_then_square = compose(square, increment)"""
    },
    {
        "id": 9,
        "name": "memoization",
        "correct": True,
        "issues": [

        ],
        "link": "",
        "code": """def memoize(func):
    cache = {}
    def memoized_func(*args):
        if args in cache:
            return cache[args]
        else:
            result = func(*args)
            cache[args] = result
            return result
    return memoized_func

@memoize
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

result = fibonacci(10)"""
    },
    {
        "id": 10,
        "name": "memoization",
        "correct": False,
        "issues": [
"memoization only stores the topmost argument"
        ],
        "link": "",
        "code": """def memoize(func):
  cache = {}
  return lambda *args: cache.setdefault(args, func(*args))

@memoize
def fibonacci(n):
  if n <= 1:
    return n
  else:
    return fibonacci(n-1) + fibonacci(n-2)

result = fibonacci(10)"""
    },
    {
        "id": 11,
        "name": "higher-order function for filtering and mapping",
        "correct": True,
        "issues": [

        ],
        "link": "",
        "code": """def filter_and_map(predicate, mapper, iterable):
  return [mapper(item) for item in iterable if predicate(item)]

def is_even(n):
  return n % 2 == 0

double_even_numbers = filter_and_map(is_even, lambda x: x * 2, range(10))"""
    },
    {
        "id": 12,
        "name": "higher-order function for filtering and mapping",
        "correct": False,
        "issues": [
"Returning the original iterable instead of the modified list"
        ],
        "link": "",
        "code": """def filter_and_map(predicate, mapper, iterable):
  result = []
  for item in iterable:
    if predicate(item):
      result.append(mapper(item))
  return iterable

def is_even(n):
  return n % 2 == 0

double_even_numbers = filter_and_map(is_even, lambda x: x * 2, range(10))"""
    },
    {
        "id": 13,
        "name": "recursive tree reversal",
        "correct": True,
        "issues": [

        ],
        "link": "",
        "code": """def traverse_tree(node, action):
  action(node)
  if node.left:
    traverse_tree(node.left, action)
  if node.right:
    traverse_tree(node.right, action)

def print_node_values(node):
  print(node.value)

tree = get_binary_tree()
traverse_tree(tree.root, print_node_values)"""
    },
    {
        "id": 14,
        "name": "recursive tree reversal",
        "correct": False,
        "issues": [
"Switched left and right child traversal order"
        ],
        "link": "",
        "code": """def traverse_tree(node, action):
  action(node)
  if node.left:
    traverse_tree(node.right, action)
  if node.right:
    traverse_tree(node.left, action)

def print_node_values(node):
  print(node.value)

tree = get_binary_tree()
traverse_tree(tree.root, print_node_values)"""
    },
    {
        "id": 15,
        "name": "function composition with multiple arguments",
        "correct": True,
        "issues": [

        ],
        "link": "",
        "code": """def compose(*funcs):
  return lambda *args: reduce(lambda acc, f: f(acc), funcs, args)

def add(*args):
  return sum(*args)

def square(x):
  return x * x

add_then_square = compose(add, square)
result = add_then_square(2, 3)"""
    },
    {
        "id": 16,
        "name": "function composition with multiple arguments",
        "correct": False,
        "issues": [
"Removed args from the reduce function"
        ],
        "link": "",
        "code": """def compose(*funcs):
  return lambda *args: reduce(lambda acc, f: f(acc), funcs)

def add(*args):
  return sum(*args)

def square(x):
  return x * x

add_then_square = compose(add, square)
result = add_then_square(2, 3)"""
    },
    {
        "id": 17,
        "name": "memoization part 2",
        "correct": False,
        "issues": [
"memoization only remembers the topmost call",
"Removed function call (*args)"
        ],
        "link": "",
        "code": """def memoize(func):
  cache = {}
  return lambda *args: cache.setdefault(args, func)

@memoize
def fibonacci(n):
  if n <= 1:
    return n
  else:
    return fibonacci(n-1) + fibonacci(n-2)

result = fibonacci(10)"""
    },
    {
        "id": 18,
        "name": "currying with a variadic function",
        "correct": True,
        "issues": [

        ],
        "link": "",
        "code": """def curry(func, *args):
  def inner(*more_args):
    return func(*(args + more_args))

  return inner

def variadic_sum(*numbers):
  return sum(numbers)

curried_sum = curry(variadic_sum, 1, 2)
result = curried_sum(3, 4, 5)"""
    },
    {
        "id": 19,
        "name": "currying with a variadic function",
        "correct": False,
        "issues": [
"Passing args and more_args as separate arguments"
        ],
        "link": "",
        "code": """def curry(func, *args):
  def inner(*more_args):
    return func(args, more_args)

  return inner

def variadic_sum(*numbers):
  return sum(numbers)

curried_sum = curry(variadic_sum, 1, 2)
result = curried_sum(3, 4, 5)"""
    },
    {
        "id": 20,
        "name": "database query with incorrect filtering",
        "correct": True,
        "issues": [

        ],
        "link": "",
        "code": """# all_employees_bonus_calculator.py

import sqlite3

conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY,
        name TEXT,
        department TEXT,
        sales_target INTEGER,
        sales_achievement INTEGER
    )
''')
conn.commit()

employees = [
    ('1', 'John Smith', 'Sales', 10000, 12000),
    ('2', 'Jane Doe', 'Marketing', 8000, 9500),
    ('3', 'Bob Johnson', 'Sales', 12000, 14000),
    ('4', 'Rachelle Davis', 'Marketing', 9000, 11000),
    ('5', 'Mike Brown', 'Sales', 11000, 9800)
]

cursor.executemany('''
    INSERT INTO employees (id, name, department, sales_target, sales_achievement)
    VALUES (?, ?, ?, ?, ?)
''', employees)
conn.commit()

# calculate bonus for employees from all departments
query = '''
    SELECT
        name,
        department,
        sales_target,
        sales_achievement,
        CASE
            WHEN sales_achievement >= 1.1 * sales_target THEN sales_achievement * 0.1
            WHEN sales_achievement >= sales_target THEN sales_achievement * 0.05
            ELSE 0
    END AS bonus
    FROM employees
'''

cursor.execute(query)

results = cursor.fetchall()
for row in results:
    print(row)

conn.close()"""
    },
    {
        "id": 21,
        "name": "database query with incorrect filtering",
        "correct": False,
        "issues": [
"condition only includes employees from sales department"
        ],
        "link": "",
        "code": """# all_employees_bonus_calculator.py

import sqlite3

conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY,
        name TEXT,
        department TEXT,
        sales_target INTEGER,
        sales_achievement INTEGER
    )
''')
conn.commit()

employees = [
    ('1', 'John Smith', 'Sales', 10000, 12000),
    ('2', 'Jane Doe', 'Marketing', 8000, 9500),
    ('3', 'Bob Johnson', 'Sales', 12000, 14000),
    ('4', 'Rachelle Davis', 'Marketing', 9000, 11000),
    ('5', 'Mike Brown', 'Sales', 11000, 9800)
]

cursor.executemany('''
    INSERT INTO employees (id, name, department, sales_target, sales_achievement)
    VALUES (?, ?, ?, ?, ?)
''', employees)
conn.commit()

# calculate bonus for employees from all departments
query = '''
    SELECT
        name,
        department,
        sales_target,
        sales_achievement,
        CASE
            WHEN sales_achievement >= 1.1 * sales_target THEN sales_achievement * 0.1
            WHEN sales_achievement >= sales_target THEN sales_achievement * 0.05
            ELSE 0
        END AS bonus
    FROM employees
    WHERE department = 'Sales'
'''

cursor.execute(query)

results = cursor.fetchall()
for row in results:
    print(row)

conn.close()"""
    },
    {
        "id": 22,
        "name": "image processing with incorrect color conversion (ITU-R BT.709 standard)",
        "correct": True,
        "issues": [

        ],
        "link": "",
        "code": """#convert to grayscale using ITU-R BT.709 standard
def convert_to_grayscale(image):
  grayscale_image = []
  for pixel in image:
    red, green, blue = pixel
    grayscale = 0.2126 * red + 0.7152 * green + 0.0722 * blue
    grayscale_image.append(grayscale)
  return grayscale_image

grayscale_image = convert_to_grayscale(original_image)"""
    },
    {
        "id": 23,
        "name": "image processing with incorrect color conversion (ITU-R BT.709 standard)",
        "correct": False,
        "issues": [
"incorrect grayscale formula"
        ],
        "link": "",
        "code": """#convert to grayscale using ITU-R BT.709 standard
def convert_to_grayscale(image):
  grayscale_image = []
  for pixel in image:
    red, green, blue = pixel
    grayscale = 0.7152 * red + 0.2126 * green + 0.0722 * blue
    grayscale_image.append(grayscale)
  return grayscale_image

grayscale_image = convert_to_grayscale(original_image)"""
    },
    {
        "id": 24,
        "name": "machine learning model training with incorrect data",
        "correct": True,
        "issues": [

        ],
        "link": "",
        "code": """def train_model(data, labels):
  model = SomeModel()
  model.fit(data, labels)
  return model

data = load_data_from_file("training_data.csv")
labels = load_labels_from_file("training_labels.csv")
model = train_model(data, labels)"""
    },
    {
        "id": 25,
        "name": "machine learning model training with incorrect data",
        "correct": False,
        "issues": [
"data and labels switched around"
        ],
        "link": "",
        "code": """def train_model(data, labels):
  model = SomeModel()
  model.fit(data, labels)
  return model

data = load_data_from_file("training_labels.csv")
labels = load_labels_from_file("training_data.csv")
model = train_model(data, labels)"""
    },
    {
        "id": 26,
        "name": "web scraping with incorrect URL",
        "correct": True,
        "issues": [

        ],
        "link": "",
        "code": """def scrape_website(url):
  response = requests.get(url)
  content = response.content
  # ... rest of the scraping logic ...

url = "https://example.com/correct-page"
scraped_data = scrape_website(url)"""
    },
    {
        "id": 27,
        "name": "web scraping with incorrect URL",
        "correct": False,
        "issues": [
"wrong url"
        ],
        "link": "",
        "code": """def scrape_website(url):
  response = requests.get(url)
  content = response.content
  # ... rest of the scraping logic ...

url = "https://example.comcorrect-page"
scraped_data = scrape_website(url)"""
    },
    {
        "id": 28,
        "name": "data processing with incorrect sorting",
        "correct": True,
        "issues": [

        ],
        "link": "",
        "code": """sales_data = [
    ('Product A', 5000),
    ('Product B', 3500),
    ('Product C', 2800),
    ('Product D', 4200),
    ('Product E', 1500)
]

# Sort products by sales in descending order
sorted_sales = sorted(sales_data, key=lambda x: x[1], reverse=True)

top_products = [product for product, sales in sorted_sales[:3]]
print("Top-selling products:", top_products)"""
    },
    {
        "id": 29,
        "name": "data processing with incorrect sorting",
        "correct": False,
        "issues": [
"data is sorted ascending instead of descending"
        ],
        "link": "",
        "code": """sales_data = [
    ('Product A', 5000),
    ('Product B', 3500),
    ('Product C', 2800),
    ('Product D', 4200),
    ('Product E', 1500)
]

# Sort products by sales in descending order
sorted_sales = sorted(sales_data, key=lambda x: x[1])

top_products = [product for product, sales in sorted_sales[:3]]
print("Top-selling products:", top_products)"""
    },
    {
        "id": 30,
        "name": "database query with sql injection vulnerability",
        "correct": True,
        "issues": [

        ],
        "link": "",
        "code": """def get_users_by_age(db, min_age, max_age):
  query = "SELECT * FROM users WHERE age > %s AND age <= %s"
  params = (min_age, max_age)
  return db.execute(query, params)

users = get_users_by_age(db, 18, 25)"""
    },
    {
        "id": 31,
        "name": "database query with sql injection vulnerability",
        "correct": False,
        "issues": [
"user input is concatenated directly into query string, giving opportunity for SQL injection attacks"
        ],
        "link": "",
        "code": """def get_users_by_age(db, min_age, max_age):
  query = "SELECT * FROM users WHERE age > " + str(min_age) + " AND age <= " + str(max_age)
  return db.execute(query)

users = get_users_by_age(db, 18, 25)"""
    },
    {
        "id": 32,
        "name": "image processing with unsafe file handling",
        "correct": True,
        "issues": [

        ],
        "link": "",
        "code": """def save_image(image, filename):
  with open(filename, "wb") as file:
    file.write(image)

save_image(image_data, "image.png")"""
    },
    {
        "id": 33,
        "name": "image processing with unsafe file handling",
        "correct": False,
        "issues": [
"Forgot to use 'with' statement, potential resource leak",
"User-provided filename without validation"
        ],
        "link": "",
        "code": """def save_image(image, filename):
  file = open(filename, "wb")
  file.write(image)
  file.close()

save_image(image_data, user_provided_filename)"""
    },
    {
        "id": 34,
        "name": "machine learning model training with data leakage",
        "correct": True,
        "issues": [

        ],
        "link": "",
        "code": """def train_model(data, labels):
  model = SomeModel()
  model.fit(data, labels)
  return model

data = load_data_from_file("training_data.csv")
labels = load_labels_from_file("training_labels.csv")
model = train_model(data, labels)"""
    },
    {
        "id": 35,
        "name": "machine learning model training with data leakage",
        "correct": False,
        "issues": [
"Using data instead of labels, potential data leakage"
        ],
        "link": "",
        "code": """def train_model(data, labels):
  model = SomeModel()
  model.fit(data, labels)
  return model

data = load_data_from_file("training_data.csv")
labels = load_labels_from_file("training_labels.csv")
model = train_model(data, data)"""
    },
    {
        "id": 36,
        "name": "web scraping with with xss vulnerability",
        "correct": True,
        "issues": [

        ],
        "link": "",
        "code": """def scrape_website(url):
  response = requests.get(url)
  content = response.content
  # ... rest of the scraping logic ...

url = "https://example.com/correct-page"
scraped_data = scrape_website(url)"""
    },
    {
        "id": 37,
        "name": "web scraping with with xss vulnerability",
        "correct": False,
        "issues": [
"Directly including content in HTML, thus potential XSS vulnerability if content is not sanitized"
        ],
        "link": "",
        "code": """def scrape_website(url):
  response = requests.get(url)
  content = response.content
  # ... rest of the scraping logic ...
  return "<div>" + content + "</div>"

url = "https://example.com/wrong-page"
scraped_data = scrape_website(url)
display_data(scraped_data)"""
    }
]