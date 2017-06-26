import click
import networkx as nx

from . import ordmap

@click.command(help='save')
@click.argument('config', type=str, required=True)
@click.argument('export', type=str, required=True)
@click.option('--save_as', 'save_as', type=str, help='save file type', default='image')
def main(config: str, export: str, save_as: str):
    G = ordmap.read_tasks(config)
    _export(G, export, save_as)


def _export(G: nx.DiGraph, filepath: str, save_as: str):
    """Export network data as image or edge list.

    Args:
        G: Directed Acyclic Graph
        filepath: Export file path (*.png or *.yml)
        save_as: 'image' or 'yaml'

    """
    if save_as == 'image':
        g = nx.nx_agraph.to_agraph(G)
        g.draw(filepath, prog='dot')
    else:
        write_method = getattr(nx, 'write_{}'.format(save_as))
        write_method(G, filepath)
