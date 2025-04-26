flawed_introduced_issues = [
    {
        "id": 1,
        "name": "01 simple to-do list app",
        "issues": [
            {"simple_id": 0, "description": "changed name from inputEmpty to inputoEmpty"},
            {"simple_id": 5, "description": "reassigned listItem which is const"},
            {"simple_id": 0, "description": "process variable is meant for Nodejs, doesnt exist in this context"},
            {"simple_id": 16, "description": "attempt to log process.env"},
            {"simple_id": 0, "description": "in index.html typo in type='boton'"},
        ],
        "dirs": [
            'tests/js/js_apps/flawed/01 simple to-do list app/app.js',
            'tests/js/js_apps/flawed/01 simple to-do list app/index.html',
            'tests/js/js_apps/flawed/01 simple to-do list app/style.css'
        ]
    },
    {
        "id": 2,
        "name": "02 ajax requests",
        "issues": [
            {"simple_id": 1, "description": "xhttp accessed before initialization"},
            {"simple_id": 17, "description": "redir() function is an unvalidated redirect security issue"},
            {"simple_id": 0, "description": "redir() is unused"}
        ],
        "dirs": [
            'tests/js/js_apps/flawed/02 ajax requests/ajax-text.txt',
            'tests/js/js_apps/flawed/02 ajax requests/app.js',
            'tests/js/js_apps/flawed/02 ajax requests/index.html',
        ]
    },
    {
        "id": 3,
        "name": "03 ajax JSON request",
        "issues": [
            {"simple_id": 3, "description": "listItem initialized twice"},
            {"simple_id": 85, "description": "traerDatos has error var"},
            {"simple_id": 102, "description": "missing space in error logging"},
            {"simple_id": 0, "description": "error will be thrown instead of logged"},
        ],
        "dirs": [
            'tests/js/js_apps/flawed/03 ajax JSON request/app.js',
            'tests/js/js_apps/flawed/03 ajax JSON request/catalogo.json',
            'tests/js/js_apps/flawed/03 ajax JSON request/index.html',
        ]
    },
    {
        "id": 4,
        "name": "04 ajax external api",
        "issues": [
            {"simple_id": 18, "description": "setLanguageOptions() is an xss vulnerability"},
        ],
        "dirs": [
            'tests/js/js_apps/flawed/04 ajax external api/app.js',
            'tests/js/js_apps/flawed/04 ajax external api/index.html',
        ]
    },
    {
        "id": 5,
        "name": "05 event delegation",
        "issues": [
            {"simple_id": 21, "description": "ineffective comparison between typeof window and NaN"},
            {"simple_id": 22, "description": "typeof window === NaN instead of isNaN"},
            {"simple_id": 106, "description": "typo in switch case casebtn-info"},
        ],
        "dirs": [
            'tests/js/js_apps/flawed/05 event delegation/app.js',
            'tests/js/js_apps/flawed/05 event delegation/index.html'
        ]
    },
    {
        "id": 6,
        "name": "06 local storage",
        "issues": [
            {"simple_id": 47, "description": "duplicate condition for btn-primary"},
            {"simple_id": 89, "description": "removePathTraversal skips iterations"},
            {"simple_id": 0, "description": "removePathTraversal does nothing meaningful despite being used in the code"},
        ],
        "dirs": [
            'tests/js/js_apps/flawed/06 local storage/app.js',
            'tests/js/js_apps/flawed/06 local storage/index.html'
        ]
    },
    {
        "id": 7,
        "name": "07 crud con local storage",
        "issues": [
            {"simple_id": 42, "description": "duplicate name=description"},
            {"simple_id": 90, "description": "<form id='formulario orialumorf'> contains space, should either be a class or id without spaces"},
        ],
        "dirs": [
            'tests/js/js_apps/flawed/07 crud con local storage/app.js',
            'tests/js/js_apps/flawed/07 crud con local storage/index.html'
        ]
    },
    {
        "id": 8,
        "name": "08 buscador en tiempo real con indexOf",
        "issues": [
            {"simple_id": 54, "description": "introduced useless variable bouton2"},
            {"simple_id": 159, "description": "unreachable statement in filtrar function"},
        ],
        "dirs": [
            'tests/js/js_apps/flawed/08 buscador en tiempo real con indexOf/app.js',
            'tests/js/js_apps/flawed/08 buscador en tiempo real con indexOf/index.html'
        ]
    },
    {
        "id": 9,
        "name": "09 meditation app",
        "issues": [
            {"simple_id": 24, "description": "checkPlaying now returns useless converter function that is also of conflicting initialization"},
            {"simple_id": 104, "description": "misspelled currentTimi instead of currentTime"},
            {"simple_id": 197, "description": "idMaker is a non-generator function"},
        ],
        "dirs": [
            'tests/js/js_apps/flawed/09 meditation app/svg/beach.svg',
            'tests/js/js_apps/flawed/09 meditation app/svg/moving-outline.svg',
            'tests/js/js_apps/flawed/09 meditation app/svg/pause.svg',
            'tests/js/js_apps/flawed/09 meditation app/svg/play.svg',
            'tests/js/js_apps/flawed/09 meditation app/svg/rain.svg',
            'tests/js/js_apps/flawed/09 meditation app/svg/replay.svg',
            'tests/js/js_apps/flawed/09 meditation app/svg/track-outline.svg',
            'tests/js/js_apps/flawed/09 meditation app/app.js',
            'tests/js/js_apps/flawed/09 meditation app/index.html',
            'tests/js/js_apps/flawed/09 meditation app/style.css'
        ]
    },
    {
        "id": 10,
        "name": "10 task app con local storage",
        "issues": [
            {"simple_id": 45, "description": "duplicate parameters in saveTask"},
            {"simple_id": 108, "description": "off by 1 comparison in i <= tasks.length"},
            {"simple_id": 167, "description": "tasks[0].title instead of tasks[i].title"},
        ],
        "dirs": [
            'tests/js/js_apps/flawed/10 task app con local storage/app.js',
            'tests/js/js_apps/flawed/10 task app con local storage/index.html'
        ]
    },
    {
        "id": 11,
        "name": "11 weather  app",
        "issues": [
            {"simple_id": 46, "description": "duplicate height in .location"},
            {"simple_id": 103, "description": "missing variable declaration 'lat'"},
            {"simple_id": 129, "description": "color = color instead of this.color = color"},
            {"simple_id": 188, "description": "incorrect type test if(typeof el === 'array')"},
        ],
        "dirs": [
            'tests/js/js_apps/flawed/11 weather  app/app.js',
            'tests/js/js_apps/flawed/11 weather  app/index.html',
            'tests/js/js_apps/flawed/11 weather  app/skycons.js',
            'tests/js/js_apps/flawed/11 weather  app/style.css'
        ]
    },
    {
        "id": 12,
        "name": "12 rock paper sissors",
        "issues": [
            {"simple_id": 84, "description": "added score = Object.create(undefined)"},
            {"simple_id": 127, "description": "assignment in return winner.textContent = 'You failed';"}
        ],
        "dirs": [
            'tests/js/js_apps/flawed/12 rock paper sissors/app.js',
            'tests/js/js_apps/flawed/12 rock paper sissors/index.html',
            'tests/js/js_apps/flawed/12 rock paper sissors/style.css'
        ]
    },
    {
        "id": 13,
        "name": "13 password generator app",
        "issues": [
            {"simple_id": 48, "description": "duplicate app variable declaration"},
            {"simple_id": 170, "description": "unused function preGeneratePassword"},
            {"simple_id": 0, "description": "preGeneratePassword contains duplicate code"},
        ],
        "dirs": [
            'tests/js/js_apps/flawed/13 password generator app/app.js',
            'tests/js/js_apps/flawed/13 password generator app/index.html',
            'tests/js/js_apps/flawed/13 password generator app/style.css'
        ]
    },
    {
        "id": 14,
        "name": "14 wes bos javascript30",
        "issues": [
            {"simple_id": 12, "description": "later is given to setTimeout as string in 13-slide-in-onscroll"},
            {"simple_id": 61, "description": "double x in function avg in 02-clock"},
            {"simple_id": 124, "description": "replacing a substring in bandName with itself in 17-sort"},
            {"simple_id": 190, "description": "timeout variable not declared before use in 13-slide-in-onscroll"},
        ],
        "dirs": [
            'tests/js/js_apps/flawed/14 wes bos javascript30/02-clock.html',
            'tests/js/js_apps/flawed/14 wes bos javascript30/13-slide-in-onscroll.html',
            'tests/js/js_apps/flawed/14 wes bos javascript30/14-references-vs-copying.html',
            'tests/js/js_apps/flawed/14 wes bos javascript30/15-localstorage.html',
            'tests/js/js_apps/flawed/14 wes bos javascript30/16-mouse-move-shadow.html',
            'tests/js/js_apps/flawed/14 wes bos javascript30/17-sort.html,'
            'tests/js/js_apps/flawed/14 wes bos javascript30/18-reduce.html',
            'tests/js/js_apps/flawed/14 wes bos javascript30/19-webcam.html'
        ]
    },
    {
        "id": 15,
        "name": "15 todo - gray",
        "issues": [
            {"simple_id": 6, "description": "toDoList assigned to exports"},
            {"simple_id": 63, "description": "toDoList is missing new"},
            {"simple_id": 91, "description": "if statement in initApp() contains misleading indentations"},
            {"simple_id": 41, "description": "if statement in initApp() are duplicate"},
            {"simple_id": 0, "description": "cyclic imports in todolist and todoitem"},
        ],
        "dirs": [
            'tests/js/js_apps/flawed/15 todo - gray/js/main.js',
            'tests/js/js_apps/flawed/15 todo - gray/js/todoitem.js',
            'tests/js/js_apps/flawed/15 todo - gray/js/todolist.js',
            'tests/js/js_apps/flawed/15 todo - gray/styles/partial/_base.scss',
            'tests/js/js_apps/flawed/15 todo - gray/styles/partial/_listContainer.scss',
            'tests/js/js_apps/flawed/15 todo - gray/styles/partial/_newItemEntry.scss',
            'tests/js/js_apps/flawed/15 todo - gray/styles/partial/_sharedClasses.scss',
            'tests/js/js_apps/flawed/15 todo - gray/styles/style.css',
            'tests/js/js_apps/flawed/15 todo - gray/styles/style.css.map',
            'tests/js/js_apps/flawed/15 todo - gray/styles/style.scss',
            'tests/js/js_apps/flawed/15 todo - gray/index.html'
        ]
    },
    {
        "id": 16,
        "name": "16_search-app",
        "issues": [
            {"simple_id": 52, "description": "error written to dom"},
            {"simple_id": 96, "description": "missing await in processSearch"},
            {"simple_id": 184, "description": "useless comparisons in findValue"},
            {"simple_id": 0, "description": "some properties of findValue are never used"},
        ],
        "dirs": [
            'tests/js/js_apps/flawed/16_search-app/modules/data-functions.js',
            'tests/js/js_apps/flawed/16_search-app/modules/search-bar.js',
            'tests/js/js_apps/flawed/16_search-app/modules/search-results.js',
            'tests/js/js_apps/flawed/16_search-app/index.html',
            'tests/js/js_apps/flawed/16_search-app/main.js',
            'tests/js/js_apps/flawed/16_search-app/styles.css'
        ]
    },
    {
        "id": 17,
        "name": "17_type-ahead",
        "issues": [
            {"simple_id": 7, "description": "in displayMatches, trying to pad the title to be of length divisible by 8"},
            {"simple_id": 142, "description": "superfluous f function"},
            {"simple_id": 191, "description": "a variable declaration has misleading whitespaces"},
        ],
        "dirs": [
            'tests/js/js_apps/flawed/17_type-ahead/data.json',
            'tests/js/js_apps/flawed/17_type-ahead/index.htm',
            'tests/js/js_apps/flawed/17_type-ahead/script.js',
            'tests/js/js_apps/flawed/17_type-ahead/styles.css'
        ]
    }
]