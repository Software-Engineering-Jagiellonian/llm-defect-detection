js_understanding = [
    {
        "id": 1,
        "name": "iterative fibonacci",
        "correct": True,
        "issues": [],
        "link": "https://rosettacode.org/wiki/Fibonacci_sequence#JavaScript",
        "code": """function fib(n) {
  var a = 0, b = 1, t;
  while (n-- > 0) {
    t = a;
    a = b;
    b += t;
    console.log(a);
  }
  return a;
}"""
    },
    {
        "id": 2,
        "name": "iterative fibonacci",
        "correct": False,
        "issues": [
            "t = b should be t = a",
            "b = 2 should be b = 1"
        ],
        "link": "https://rosettacode.org/wiki/Fibonacci_sequence#JavaScript",
        "code": """function fib(n) {
  var a = 0, b = 2, t;
  while (n-- > 0) {
    t = b;
    a = b;
    b += t;
    console.log(a);
  }
  return a;
}"""
    },
    {
        "id": 3,
        "name": "user input A+B",
        "correct": True,
        "issues": [],
        "link": "https://rosettacode.org/wiki/A%2BB#JavaScript",
        "code": """
        process.stdin.on("data", buffer => {
  console.log(
    (buffer + "").trim().split(" ").map(Number).reduce((a, v) => a + v, 0)
  );
});"""
    },
    {
        "id": 4,
        "name": "user input A+B",
        "correct": False,
        "issues": [
            "console.get doesn't exist"
        ],
        "link": "https://rosettacode.org/wiki/A%2BB#JavaScript",
        "code": """
        console.get.on("data", buffer => {
  console.log(
    (buffer + "").trim().split(" ").map(Number).reduce((a, v) => a + v, 0)
  );
});"""
    },
    {
        "id": 5,
        "name": "10035-maximum-area-of-longest-diagonal-rectangle",
        "correct": True,
        "issues": [],
        "link": "https://github.com/everthis/leetcode-js/blob/master/10035-maximum-area-of-longest-diagonal-rectangle.js",
        "code": """/**
 * @param {number[][]} dimensions
 * @return {number}
 */
var areaOfMaxDiagonal = function(dimensions) {
   let res = 0
   const n = dimensions
   const arr = dimensions.map(([l,w]) => [l ** 2 + w ** 2, l * w])
   arr.sort((a, b) => a[0] === b[0] ?  b[1] - a[1] : b[0] - a[0])
   return arr[0][1]
};"""
    },
    {
        "id": 6,
        "name": "10035-maximum-area-of-longest-diagonal-rectangle",
        "correct": False,
        "issues": [
            "l ** 3 is wrong (should be l ** 2)"
        ],
        "link": "https://github.com/everthis/leetcode-js/blob/master/10035-maximum-area-of-longest-diagonal-rectangle.js",
        "code": """/**
 * @param {number[][]} dimensions
 * @return {number}
 */
var areaOfMaxDiagonal = function(dimensions) {
   let res = 0
   const n = dimensions
   const arr = dimensions.map(([l,w]) => [l ** 3 + w ** 2, l * w])
   arr.sort((a, b) => a[0] === b[0] ?  b[1] - a[1] : b[0] - a[0])
   return arr[0][1]
};"""
    },
    {
        "id": 7,
        "name": "1022-smallest-integer-divisible-by-k",
        "correct": True,
        "issues": [],
        "link": "https://github.com/everthis/leetcode-js/blob/master/1022-smallest-integer-divisible-by-k.js",
        "code": """/**
 * @param {number} K
 * @return {number}
 */
const smallestRepunitDivByK = function(K) {
    if (K % 2 === 0 || K % 5 === 0) return -1;
    let r = 0;
    for (let N = 1; N <= K; ++N) {
        r = (r * 10 + 1) % K;
        if (r == 0) return N;
    }
    return -1;
};"""
    },
    {
        "id": 8,
        "name": "1022-smallest-integer-divisible-by-k",
        "correct": False,
        "issues": [
            "let N == 1 should be an assignment"
        ],
        "link": "https://github.com/everthis/leetcode-js/blob/master/1022-smallest-integer-divisible-by-k.js",
        "code": """/**
 * @param {number} K
 * @return {number}
 */
const smallestRepunitDivByK = function(K) {
    if (K % 2 === 0 || K % 5 === 0) return -1;
    let r = 0;
    for (let N === 1; N <= K; ++N) {
        r = (r * 10 + 1) % K;
        if (r == 0) return N;
    }
    return -1;
};"""
    },
    {
        "id": 13,
        "name": "Recursively Computing the Fibonacci Sequence",
        "correct": True,
        "issues": [
        ],
        "link": "",
        "code": """function fibonacci(n) {
      if (n <= 1) {
        return n;
      } else {
        return fibonacci(n - 1) + fibonacci(n - 2);
      }
    }"""
    },
    {
        "id": 9,
        "name": "Recursively Computing the Fibonacci Sequence",
        "correct": False,
        "issues": [
            "parameter n given and interpreted as a string"
        ],
        "link": "",
        "code": """function fibonacci("n") {
          if ("n" <= 1) {
            return "n";
          } else {
            return fibonacci("n" - 1) + fibonacci("n" - 2);
          }
        }"""
    },
    {
        "id": 10,
        "name": "Recursively Computing the Fibonacci Sequence",
        "correct": False,
        "issues": [
            "parameter n given and interpreted as a string",
            "Changed the condition to n <= 0"
        ],
        "link": "",
        "code": """function fibonacci("n") {
          if ("n" <= 0) {
            return "n";
          } else {
            return fibonacci("n" - 1) + fibonacci("n" - 2);
          }
        }"""
    },
    {
        "id": 11,
        "name": "Currying and Partial Application",
        "correct": True,
        "issues": [],
        "link": "",
        "code": """function curry(func, ...args) {
      return function inner(...moreArgs) {
        return func(...args, ...moreArgs);
      };
    }

    function add(a, b) {
      return a + b;
    }

    const doubled = curry(add, 2);"""
    },
    {
        "id": 12,
        "name": "Currying and Partial Application",
        "correct": False,
        "issues": [
            "Missing args destructuring"
        ],
        "link": "",
        "code": """function curry(func, ...args) {
      return function inner(...moreArgs) {
        return func(args, ...moreArgs);
      };
    }

    function add(a, b) {
      return a + b;
    }

    const doubled = curry(add, 2);"""
    },
    {
        "id": 15,
        "name": "Higher-Order Functions and Function Composition",
        "correct": True,
        "issues": [],
        "link": "",
        "code": """function compose(...funcs) {
      return function(x) {
        return funcs.reduce(function(acc, f) {
          return f(acc);
        }, x);
      };
    }
    
    function square(x) {
      return x * x;
    }
    
    function increment(x) {
      return x + 1;
    }
    
    const doubleThenSquare = compose(increment, square);"""
    },
    {
        "id": 16,
        "name": "Higher-Order Functions and Function Composition",
        "correct": False,
        "issues": [
    "Switched the order of functions"
        ],
        "link": "",
        "code": """function compose(...funcs) {
      return function(x) {
        return funcs.reduce(function(acc, f) {
          return f(acc);
        }, x);
      };
    }
    
    function square(x) {
      return x * x;
    }
    
    function increment(x) {
      return x + 1;
    }
    
    const doubleThenSquare = compose(square, increment);"""
    },
    {
        "id": 17,
        "name": "Recursive Tree Reversal",
        "correct": True,
        "issues": [],
        "link": "",
        "code": """function traverseTree(node, action) {
      action(node);
      if (node.left) {
        traverseTree(node.left, action);
      }
      if (node.right) {
        traverseTree(node.right, action);
      }
    }
    
    function printNodeValues(node) {
      console.log(node.value);
    }
    
    const tree = getBinaryTree();
    traverseTree(tree.root, printNodeValues);"""
    },
    {
        "id": 18,
        "name": "Recursive Tree Reversal",
        "correct": False,
        "issues": [
    "Switched left and right child traversal order"
        ],
        "link": "",
        "code": """function traverseTree(node, action) {
      action(node);
      if (node.left) {
        traverseTree(node.right, action);
      }
      if (node.right) {
        traverseTree(node.left, action);
      }
    }
    
    function printNodeValues(node) {
      console.log(node.value);
    }
    
    const tree = getBinaryTree();
    traverseTree(tree.root, printNodeValues);"""
    },
    {
        "id": 19,
        "name": "Higher-Order Function for Filtering and Mapping",
        "correct": True,
        "issues": [],
        "link": "",
        "code": """function filterAndMap(predicate, mapper, iterable) {
      return iterable.filter(predicate).map(mapper);
    }
    
    function isEven(n) {
      return n % 2 === 0;
    }
    
    const doubleEvenNumbers = filterAndMap(isEven, n => n * 2, [0,1,2,3,4,5,6,7]);"""
    },
    {
        "id": 20,
        "name": "Higher-Order Function for Filtering and Mapping",
        "correct": False,
       "issues": [
    "Returning the original iterable instead of the modified list"
        ],
        "link": "",
        "code": """function filterAndMap(predicate, mapper, iterable) {
      const result = [];
      for (const item of iterable) {
        if (predicate(item)) {
          result.push(mapper(item));
        }
      }
      return iterable;
    }
    
    function isEven(n) {
      return n % 2 === 0;
    }
    
    const doubleEvenNumbers = filterAndMap(isEven, n => n * 2, [0,1,2,3,4,5,6,7]);"""
    },
    {
        "id": 21,
        "name": "Currying with a Variadic Function",
        "correct": True,
        "issues": [],
        "link": "",
        "code": """function curry(func, ...args) {
      return function inner(...moreArgs) {
        return func(...args, ...moreArgs);
      };
    }
    
    function variadicSum(...numbers) {
      return numbers.reduce((a, b) => a + b, 0);
    }
    
    const curriedSum = curry(variadicSum, 1, 2);
    const result = curriedSum(3, 4, 5);"""
    },
    {
        "id": 22,
        "name": "Currying with a Variadic Function",
        "correct": False,
        "issues": [
    "Passing args and moreArgs as separate arguments"
        ],
        "link": "",
        "code": """function curry(func, ...args) {
      return function inner(...moreArgs) {
        return func(args, ...moreArgs);
      };
    }
    
    function variadicSum(...numbers) {
      return numbers.reduce((a, b) => a + b, 0);
    }
    
    const curriedSum = curry(variadicSum, 1, 2);
    const result = curriedSum(3, 4, 5);"""
    },
    {
        "id": 23,
        "name": "Image Processing with Incorrect Color Conversion (ITU-R BT.709 Standard)",
        "correct": True,
        "issues": [],
        "link": "",
        "code": """function convertToGrayscale(image) {
      const grayscaleImage = [];
      for (const pixel of image) {
        const [red, green, blue] = pixel;
        const grayscale = 0.2126 * red + 0.7152 * green + 0.0722 * blue;
        grayscaleImage.push(grayscale);
      }
      return grayscaleImage;
    }
    
    const grayscaleImage = convertToGrayscale(originalImage);"""
    },
    {
        "id": 24,
        "name": "Image Processing with Incorrect Color Conversion (ITU-R BT.709 Standard)",
        "correct": False,
        "issues": [
    "Incorrect grayscale formula"
        ],
        "link": "",
        "code": """function convertToGrayscale(image) {
      const grayscaleImage = [];
      for (const pixel of image) {
        const [red, green, blue] = pixel;
        const grayscale = 0.7152 * red + 0.2126 * green + 0.0722 * blue;
        grayscaleImage.push(grayscale);
      }
      return grayscaleImage;
    }
    
    const grayscaleImage = convertToGrayscale(originalImage);"""
    },
    {
        "id": 25,
        "name": "Data Processing with Incorrect Sorting",
        "correct": True,
        "issues": [],
        "link": "",
        "code": """const salesData = [
        ['Product A', 5000],
        ['Product B', 3500],
        ['Product C', 2800],
        ['Product D', 4200],
        ['Product E', 1500]
    ];
    
    // Sort products by sales in descending order 
    const sortedSales = salesData.sort((a, b) => b[1] - a[1]);
    
    const topProducts = sortedSales.slice(0, 3).map(product => product[0]);
    console.log('Top-selling products:', topProducts);"""
    },
    {
        "id": 26,
        "name": "Data Processing with Incorrect Sorting",
        "correct": False,
        "issues": [
    "Data is sorted ascending instead of descending"
        ],
        "link": "",
        "code": """const salesData = [
        ['Product A', 5000],
        ['Product B', 3500],
        ['Product C', 2800],
        ['Product D', 4200],
        ['Product E', 1500]
    ];
    
    // Sort products by sales in descending order
    const sortedSales = salesData.sort((a, b) => a[1] - b[1]);
    
    const topProducts = sortedSales.slice(0, 3).map(product => product[0]);
    console.log('Top-selling products:', topProducts);"""
    },
    {
        "id": 27,
        "name": "Finding Minimum Value in an Array",
        "correct": True,
        "issues": [],
        "link": "",
        "code": """function findMin(nums) {
      let min = Infinity;
      for (let i = 0; i < nums.length; i++) {
        if (typeof nums[i] === "number" && nums[i] < min) {
          min = nums[i];
        }
      }
      return min;
    }

    const numbers = [1, 2, 3, 4, 5, null];
    console.log(findMin(numbers));"""
    },
    {
        "id": 28,
        "name": "Finding Minimum Value in an Array",
        "correct": False,
        "issues": [
            "Incorrect comparison logic with null present in input array"
        ],
        "link": "",
        "code": """function findMin(nums) {
      let min = Infinity;
      for (let i = 0; i < nums.length; i++) {
        if (nums[i] < min) {
          min = nums[i];
        }
      }
      return min;
    }

    const numbers = [1, 2, 3, 4, 5, null];
    console.log(findMin(numbers));"""
    },
    {
        "id": 29,
        "name": "Event Handling: Click Counter",
        "correct": True,
        "issues": [],
        "link": "",
        "code": """const button = document.querySelector('button');
    let clickCount = 0;

    button.addEventListener('click', function() {
      clickCount++;
      button.textContent = `Clicked ${clickCount} times`;
    });"""
    },
    {
        "id": 30,
        "name": "Event Handling: Click Counter",
        "correct": False,
        "issues": [
            "Incorrect event target"
        ],
        "link": "",
        "code": """const button = document.querySelector('button');
    let clickCount = 0;
    
    button.addEventListener('click', function() {
      clickCount++;
      this.textContent = `Clicked ${clickCount} times`;
    });"""
    }
]


