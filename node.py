class NodeIterator:
    """Iterator object for traversing a chain of nodes"""

    def __init__(self, start_node):
        self.current_node = start_node
        self.current_entry_index = 0

    def __iter__(self):
        """Return self to implement iterator protocol"""
        return self

    def __next__(self):
        """Return the next entry in the node chain"""
        while self.current_node is not None:
            if self.current_entry_index < len(self.current_node.entries):
                # Get the current entry and advance the index
                entry = self.current_node.entries[self.current_entry_index]
                self.current_entry_index += 1
                return entry
            else:
                # Move to the next node and reset entry index
                self.current_node = self.current_node.next
                self.current_entry_index = 0

        # No more nodes or entries
        raise StopIteration


class Node:
    def __init__(self, entries):
        self.entries = entries
        self.next = None

    def __iter__(self):
        """Return a new NodeIterator for this node chain"""
        return NodeIterator(self)
