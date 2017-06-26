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

![tasks.png](https://raw.githubusercontent.com/takeshi0406/ordmap/master/images/tasks.png)


## TODO

* plot node name as UTF-8 (plot 日本語).
* plot Hasse Diagram beautifully.
