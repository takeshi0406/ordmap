import yaml
from typing import List

import networkx as nx


def read_tasks(filepath: str) -> nx.DiGraph:
    """Read config yaml file as Directed Acyclic Graph.

    Args:
        filepath: config yaml file path
    Returns:
        Directed Acyclic Graph

    """
    tasks = _read_yaml(filepath)
    return _create_dag(tasks)


class Task(object):
    """Task type"""
    def __init__(self, config: dict):
        self.name = config['name']
        self.dependents = config.get('deps', [])


def _read_yaml(filepath: str) -> List[Task]:
    """Read config yaml file as task list.

    Args:
        filepath: config yaml file path
    Returns:
        list of task

    """
    with open(filepath, encoding='utf-8') as f:
        confs = yaml.load(f)
    return [Task(c) for c in confs]


def _create_dag(tasks: List[Task]) -> nx.DiGraph:
    """Translate task list to Directed Acyclic Graph.

    Args:
        tasks: list of task
    Returns:
        Directed Acyclic Graph

    """
    G = nx.DiGraph()
    for task in tasks:
        for dep in task.dependents:
            G.add_edge(dep, task.name)
    assert nx.is_directed_acyclic_graph(G)
    return _transitive_reduction(G)


def _transitive_reduction(G: nx.DiGraph) -> nx.DiGraph:
    """Translate DiGraph to Directed Acyclic Graph.
    see also https://networkx.readthedocs.io/en/latest/reference/generated/networkx.algorithms.dag.transitive_reduction.html

    Args:
        G: Digraph
    Returns:
        Directed Acyclic Graph

    """
    TR = nx.DiGraph()
    TR.add_nodes_from(G.nodes())
    for u in G:
        u_edges = set(G[u])
        for v in G[u]:
            u_edges -= {y for x, y in nx.dfs_edges(G, v)}
        TR.add_edges_from((u,v) for v in u_edges)
    return TR
