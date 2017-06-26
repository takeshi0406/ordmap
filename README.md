# ordmap

Visualise your task loadmap as Hasse Diagram.

## Installation

Install from Github.

```bash
pip install --upgrade git+https://github.com/takeshi0406/ordmap
```

## Usage

Create yaml file consisting of your tasks.

name: your task name.
deps: other task names you must complete before this task.

```yaml
# tasks.yml
- name: write product code
  deps:
    - fix design
    - choose programing language
    - request for budget(ringi)
    - make a mock-up
- name: choose programing language
- name: request for budget(ringi)
    - talk to legal department
- name: talk to legal department
- name: releace
  deps:
    - write product code
    - code review
- name: code review
    - write product code
- name: make a mock-up
  deps:
    - choose programming language
```

Run this command.

```bash
# save as NetworkX graph
ordmap tasks.yml tasks.png

# save as pajek format
# see also https://networkx.github.io/documentation/networkx-1.9/reference/readwrite.html
ordmap tasks.yml tasks.net --save_as pajek
```

![tasks.png](https://raw.github.com/wiki/takeshi0406/ordmap/images/tasks.png)

eg. pajek format

```
*vertices 8
1 "write product code" 0.0 0.0 ellipse
2 "fix design" 0.0 0.0 ellipse
3 "choose programing language" 0.0 0.0 ellipse
4 "request for budget(ringi)" 0.0 0.0 ellipse
5 "make a mock-up" 0.0 0.0 ellipse
6 releace 0.0 0.0 ellipse
7 "code review" 0.0 0.0 ellipse
8 "choose programming language" 0.0 0.0 ellipse
*arcs
1 2 1.0
1 3 1.0
1 4 1.0
1 5 1.0
5 8 1.0
6 1 1.0
6 7 1.0
```

## TODO

* plot node name as UTF-8 (plot 日本語).
* plot Hasse Diagram beautifully.
