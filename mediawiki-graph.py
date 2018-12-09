from bs4 import BeautifulSoup
import os
import json
import requests
import graph-tool as gt
from concurrent.futures import ThreadPoolExecutor
from threading import Lock



class MediaWikiGraph(gt.Graph):
    def __init__(self, api_url, namespace=0):
        super().__init__()
        self.api_url = api_url
        self.namespace = 0
        self.lock = Lock()
        self.vp["is_redirect"] = self.new_edge("bool")
        self.vp["pageid"] = self.new_edge("int")

    def _add_pages(self, pageids):
        '''Adds a list of vertices

        Args:
            pageids ([int]) : list of pageids from the wiki page

        '''
        with self.lock:
            new_vertices = self.add_vertex(len(pageids))
            for vertex, pageid in zip(new_vertices, pageids):
                self.vp["pageid"][vertex] = pageid
    
    def _add_page(self, pageid):
        '''Adds a vertex

        Args:
            pageid (int) : pageid from the wiki page

        '''
        with self.lock:
            new_vertex = self.add_vertex()
            self.vp["pageid"][new_vertex] = pageid

    def _add_links(self, edge_list):
        '''Adds a directed edge from u to v

        Args:
            edge_list ( [(graph-tool.Vertex, graph-tool.Vertex)] ) : list of
                tuples (u,v) representing directed edges from u to v

        '''
        with self.lock:
            self.add_edge_list(edge_list)
    
    def _add_link(self, u, v):
        '''Adds a directed edge from u to v

        Args:
            u (graph-tool.Vertex) : source node
            v (graph-tool.Vertex) : target node

        '''
        with self.lock:
            self.add_edge(u, v)
        
    
    def _get_all_pages(max_workers, **kwargs):
        '''Gets all pages from the api destination
        
        Args:
            max_workers (int): number of threads to use
            **kwargs (): key word argument constraints on the mediawiki allpages query

        '''
        with ThreadPoolExecutor(max_workers=max_workers) as thread_pool:
            #TODO use a generator to iterator over all the pages on the wiki
            #     for every page on the wiki make a vertex
            pass
    
    def _get_all_links(max_workers, **kwargs):
        '''Gets all pages from the api destination
        
        Args:
            max_workers (int): number of threads to use
            **kwargs (): key word argument constraints on the mediawiki allpages query

        '''
        with ThreadPoolExecutor(max_workers=max_workers) as thread_pool:
            #TODO for every vertex in the graph get all the links from the vertex and add to graph
            pass

    def build(max_workers=None, **kwargs):
        _get_all_pages(max_workers, **kwargs)
        _get_all_links(max_workers, **kwargs)

