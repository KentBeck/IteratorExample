import unittest
from node import Node, NodeIterator


class TestNode(unittest.TestCase):

    def test_create_simple_node_with_single_entry(self):
        """Test: Create a simple node with a single entry"""
        node = Node(["first_entry"])
        self.assertEqual(node.entries, ["first_entry"])
        self.assertIsNone(node.next)

    def test_create_node_with_multiple_entries(self):
        """Test: Create a node with multiple entries"""
        node = Node(["entry1", "entry2", "entry3"])
        self.assertEqual(node.entries, ["entry1", "entry2", "entry3"])
        self.assertIsNone(node.next)

    def test_node_should_be_iterable(self):
        """Test: Node should be iterable (implement __iter__)"""
        node = Node(["entry1", "entry2", "entry3"])
        # Test that we can get an iterator
        iterator = iter(node)
        self.assertIsNotNone(iterator)

        # Test that we can iterate through entries
        entries = list(iterator)
        self.assertEqual(entries, ["entry1", "entry2", "entry3"])

    def test_iterator_works_across_linked_nodes(self):
        """Test: Iterator should work across linked nodes"""
        # Create a chain of nodes
        node1 = Node(["a", "b"])
        node2 = Node(["c", "d"])
        node3 = Node(["e"])

        # Link them together
        node1.next = node2
        node2.next = node3

        # Test iteration across the entire chain
        entries = list(node1)
        self.assertEqual(entries, ["a", "b", "c", "d", "e"])

    def test_for_loop_iteration_over_node_chain(self):
        """Test: Support for-loop iteration over node chain"""
        # Create a chain of nodes
        node1 = Node(["x", "y"])
        node2 = Node("z")
        node1.next = node2

        # Test for-loop iteration
        result = []
        for entry in node1:
            result.append(entry)

        self.assertEqual(result, ["x", "y", "z"])

    def test_iter_returns_iterator_object(self):
        """Test: __iter__ returns a separate NodeIterator object"""
        node = Node(["a", "b"])
        iterator = iter(node)

        # Should return a NodeIterator instance
        self.assertIsInstance(iterator, NodeIterator)

        # Iterator should implement iterator protocol
        self.assertEqual(iter(iterator), iterator)  # iterator.__iter__() returns self

        # Should be able to call next() on it
        self.assertEqual(next(iterator), "a")
        self.assertEqual(next(iterator), "b")

        # Should raise StopIteration when exhausted
        with self.assertRaises(StopIteration):
            next(iterator)

    def test_append_node_to_end_of_chain(self):
        """Test: append() should add a node to the end of the chain"""
        # Create initial chain
        node1 = Node(["a", "b"])
        node2 = Node(["c"])
        node1.next = node2

        # Create node to append
        node3 = Node(["d", "e"])

        # Append node3 to the chain starting at node1
        node1.append(node3)

        # Test that the chain now includes all entries
        entries = list(node1)
        self.assertEqual(entries, ["a", "b", "c", "d", "e"])

        # Test that node3 is properly linked at the end
        self.assertEqual(node2.next, node3)
        self.assertIsNone(node3.next)

    def test_append_node_to_single_node(self):
        """Test: append() should work on a single node"""
        node1 = Node(["first"])
        node2 = Node(["second", "third"])

        node1.append(node2)

        # Test the chain
        entries = list(node1)
        self.assertEqual(entries, ["first", "second", "third"])

        # Test the linking
        self.assertEqual(node1.next, node2)
        self.assertIsNone(node2.next)


if __name__ == "__main__":
    unittest.main()
