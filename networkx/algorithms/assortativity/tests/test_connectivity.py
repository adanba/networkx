#!/usr/bin/env python
from nose.tools import *
import networkx as nx

class TestNeighborConnectivity(object):

    def test_degree_p4(self):
        G=nx.path_graph(4)
        answer={1:2.0,2:1.5}
        nd = nx.average_degree_connectivity(G)
        assert_equal(nd,answer)
        
        D=G.to_directed()
        answer={2:2.0,4:1.5}
        nd = nx.average_degree_connectivity(D)
        assert_equal(nd,answer)

        answer={1:2.0,2:1.5}
        D=G.to_directed()
        nd = nx.average_in_degree_connectivity(D)
        assert_equal(nd,answer)

        D=G.to_directed()
        nd = nx.average_out_degree_connectivity(D)
        assert_equal(nd,answer)

    def test_degree_p4_weighted(self):
        G=nx.path_graph(4)
        G[1][2]['weight']=4
        answer={1:2.0,2:1.8}
        nd = nx.average_degree_connectivity(G,weight='weight')
        assert_equal(nd,answer)
        answer={1:2.0,2:1.5}
        nd = nx.average_degree_connectivity(G)
        assert_equal(nd,answer)
        
        D=G.to_directed()
        answer={2:2.0,4:1.8}
        nd = nx.average_degree_connectivity(D,weight='weight')
        assert_equal(nd,answer)

        answer={1:2.0,2:1.8}
        D=G.to_directed()
        nd = nx.average_in_degree_connectivity(D,weight='weight')
        assert_equal(nd,answer)

        D=G.to_directed()
        nd = nx.average_out_degree_connectivity(D,weight='weight')
        assert_equal(nd,answer)

    def test_weight_keyword(self):
        G=nx.path_graph(4)
        G[1][2]['other']=4
        answer={1:2.0,2:1.8}
        nd = nx.average_degree_connectivity(G,weight='other')
        assert_equal(nd,answer)
        answer={1:2.0,2:1.5}
        nd = nx.average_degree_connectivity(G,weight=None)
        assert_equal(nd,answer)
        
        D=G.to_directed()
        answer={2:2.0,4:1.8}
        nd = nx.average_degree_connectivity(D,weight='other')
        assert_equal(nd,answer)

        answer={1:2.0,2:1.8}
        D=G.to_directed()
        nd = nx.average_in_degree_connectivity(D,weight='other')
        assert_equal(nd,answer)

        D=G.to_directed()
        nd = nx.average_out_degree_connectivity(D,weight='other')
        assert_equal(nd,answer)

    def test_degree_barrat(self):
        G=nx.star_graph(5)
        G.add_edges_from([(5,6),(5,7),(5,8),(5,9)])
        G[0][5]['weight']=5
        nd = nx.average_degree_connectivity(G)[5]
        assert_equal(nd,1.8)
        nd = nx.average_degree_connectivity(G,weight='weight')[5]
        assert_almost_equal(nd,3.222222,places=5)
        nd = nx.k_nearest_neighbors(G,weight='weight')[5]
        assert_almost_equal(nd,3.222222,places=5)
