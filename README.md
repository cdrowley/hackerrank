# Hacker Rank Solutions

My solutions to [Hacker Rank](https://www.hackerrank.com/) topics, covering: 
- **Python** (*great for practising the standard library and built-ins*)
-  **SQL** (MS-SQL: *great for learning or revising the essentials*)
- **Problem Solving** (Python: *work-in-progress*)
- **Functional Programming** (Scala: *work-in-progress*)
- ...


## Development Environment
Designed to work on MacOS / Linux / [WSL](https://learn.microsoft.com/en-us/windows/wsl/about)


### Python

Standard Python3 should suffice for most problems and won't require additional setup. 

For the `numpy` challenges and harder problem-solving challenges (where `more-itertools` and other third-party libraries may be used) [the makefile](https://opensource.com/article/18/8/what-how-makefile) can be used in a terminal:

- `make build` (*only required the first time*) will create a [Python virtual environment](https://docs.python.org/3/library/venv.html) and install our additional dependencies
- `make run` can be used to activate our virtual environment (*alt. `source venv/bin/activate`*)
- `make clean` will remove the `venv` folder

---
### SQL

All SQL solutions are targetted at MS-SQL, as sadly [PostgreSQL](https://www.postgresql.org/) is not an option.

---
### Scala
...