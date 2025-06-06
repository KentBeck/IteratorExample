#!/usr/bin/env python3
"""
Demonstration of Pythonic Iterator over Lists of Nodes

This example shows how a simple Node class can be made iterable
using Python's iterator protocol, allowing for clean, Pythonic
iteration over linked data structures.
"""

from node import Node


def main():
    print("=== Pythonic Iterator over Lists of Nodes Demo ===\n")
    
    # Create individual nodes with different entry types
    print("1. Creating nodes with different entry patterns:")
    node1 = Node(["apple", "banana"])
    node2 = Node("cherry")
    node3 = Node(["date", "elderberry", "fig"])
    
    print(f"   Node 1 entries: {node1.entries}")
    print(f"   Node 2 entries: {node2.entries}")
    print(f"   Node 3 entries: {node3.entries}")
    
    # Link the nodes together
    print("\n2. Linking nodes together:")
    node1.next = node2
    node2.next = node3
    print("   node1 -> node2 -> node3")
    
    # Demonstrate Pythonic iteration
    print("\n3. Pythonic iteration using for-loop:")
    print("   for entry in node1:")
    for entry in node1:
        print(f"     {entry}")
    
    # Demonstrate list conversion
    print("\n4. Converting to list:")
    all_entries = list(node1)
    print(f"   list(node1) = {all_entries}")
    
    # Demonstrate multiple iterations (iterator is lazy)
    print("\n5. Multiple iterations over same chain:")
    print("   First iteration:", [entry for entry in node1])
    print("   Second iteration:", [entry for entry in node1])
    
    # Demonstrate iterator protocol
    print("\n6. Using iterator protocol directly:")
    iterator = iter(node1)
    print(f"   next(iterator) = {next(iterator)}")
    print(f"   next(iterator) = {next(iterator)}")
    print(f"   Remaining entries: {list(iterator)}")
    
    # Demonstrate with different data types
    print("\n7. Working with different data types:")
    numeric_node1 = Node([1, 2, 3])
    numeric_node2 = Node(4)
    numeric_node1.next = numeric_node2
    
    print(f"   Numbers: {list(numeric_node1)}")
    print(f"   Sum: {sum(numeric_node1)}")
    print(f"   Max: {max(numeric_node1)}")
    
    # Demonstrate empty chain
    print("\n8. Edge case - single node:")
    single_node = Node("lonely")
    print(f"   Single node iteration: {list(single_node)}")
    
    print("\n=== Demo Complete ===")


if __name__ == "__main__":
    main()
