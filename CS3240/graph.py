__author__ = 'rmb3yz'


class Graph:
    def __init__(self, nodeDict={}):
        self.nodeList = nodeDict
        self.length = len(self.nodeList)

    def get_adjlist(self, node):
        if node in self:
            return self.nodeList[node]
        return None

    def is_adjacent(self, node1, node2):
        if node1 in self:
            node1Adj = self.get_adjlist(node1)
            if node2 in node1Adj:
                return True
        return False

    def __str__(self):
        return str(self.nodeList)

    def __iter__(self):
        return iter(self.nodeList)

    def __contains__(self, node):
        if node in self.nodeList:
            return True
        return False

    def __len__(self):
        return self.length

    def add_node(self, node):
        if node not in self:
            self.nodeList.update({node: []})
            self.length += 1
            return True
        return False

    def link_nodes(self, node1, node2):
        if node1 in self:
            if node2 in self:
                if node1 != node2:
                    node1Adj = self.get_adjlist(node1)
                    node2Adj = self.get_adjlist(node2)
                    if not self.is_adjacent(node1, node2):
                        node2Adj.append(node1)
                        node1Adj.append(node2)
                        return True
        return False

    def unlink_nodes(self, node1, node2):
        if node1 in self:
            if node2 in self:
                if node1 != node2:
                    node1Adj = self.get_adjlist(node1)
                    node2Adj = self.get_adjlist(node2)
                    if self.is_adjacent(node1, node2):
                        node2Adj.remove(node1)
                        node1Adj.remove(node2)
                        return True
        return False

    def del_node(self, node):
        if node in self:
            nodeAdj = self.get_adjlist(node)
            while (len(nodeAdj) > 0):
                n = nodeAdj[0]
                self.unlink_nodes(node, n)
            self.nodeList.pop(node)
            self.length -= 1
            return True
        return False
