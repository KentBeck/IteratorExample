#!/usr/bin/env python3
"""
Demonstration of Extracted NodeIterator Object

This example shows how the iterator functionality has been extracted
into a separate NodeIterator class, following the iterator pattern
more explicitly.
"""

from node import Node, NodeIterator


def main():
    print("=== Extracted NodeIterator Object Demo ===\n")
    
    # Create a chain of nodes
    node1 = Node(["first", "second"])
    node2 = Node("third")
    node3 = Node(["fourth", "fifth"])
    node1.next = node2
    node2.next = node3
    
    print("1. Node chain created:")
    print("   node1: ['first', 'second'] -> node2: ['third'] -> node3: ['fourth', 'fifth']")
    
    # Show that iter() returns a NodeIterator object
    print("\n2. iter(node) returns a NodeIterator object:")
    iterator = iter(node1)
    print(f"   type(iter(node1)) = {type(iterator)}")
    print(f"   isinstance(iterator, NodeIterator) = {isinstance(iterator, NodeIterator)}")
    
    # Show iterator protocol implementation
    print("\n3. Iterator protocol implementation:")
    print(f"   iter(iterator) is iterator = {iter(iterator) is iterator}")
    print("   This means the iterator implements __iter__() returning self")
    
    # Show manual iteration using next()
    print("\n4. Manual iteration using next():")
    iterator = iter(node1)
    try:
        while True:
            entry = next(iterator)
            print(f"   next(iterator) = '{entry}'")
    except StopIteration:
        print("   StopIteration raised - iteration complete")
    
    # Show that each iter() call creates a new iterator
    print("\n5. Each iter() call creates a new iterator:")
    iter1 = iter(node1)
    iter2 = iter(node1)
    print(f"   iter1 is iter2 = {iter1 is iter2}")
    print(f"   id(iter1) = {id(iter1)}")
    print(f"   id(iter2) = {id(iter2)}")
    
    # Show independent iteration
    print("\n6. Independent iteration with multiple iterators:")
    iter1 = iter(node1)
    iter2 = iter(node1)
    
    print(f"   next(iter1) = '{next(iter1)}'")
    print(f"   next(iter1) = '{next(iter1)}'")
    print(f"   next(iter2) = '{next(iter2)}'")  # Should start from beginning
    print(f"   next(iter1) = '{next(iter1)}'")
    
    # Show iterator state
    print("\n7. Iterator maintains its own state:")
    iterator = iter(node1)
    print(f"   Initial state: current_node={iterator.current_node.entries}, index={iterator.current_entry_index}")
    
    next(iterator)  # Advance once
    print(f"   After next(): current_node={iterator.current_node.entries}, index={iterator.current_entry_index}")
    
    next(iterator)  # Advance again
    print(f"   After next(): current_node={iterator.current_node.entries}, index={iterator.current_entry_index}")
    
    next(iterator)  # Move to next node
    print(f"   After next(): current_node={iterator.current_node.entries}, index={iterator.current_entry_index}")
    
    # Show that the original Pythonic usage still works
    print("\n8. Original Pythonic usage still works:")
    print("   for entry in node1:")
    for entry in node1:
        print(f"     '{entry}'")
    
    print(f"\n   list(node1) = {list(node1)}")
    
    print("\n=== Iterator Object Demo Complete ===")


if __name__ == "__main__":
    main()
