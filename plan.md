# Iterator Example - Code Generalization Plan

This project demonstrates how to generalize code using a linked list of nodes as an example. We'll start with specific, concrete implementations and gradually generalize them to show common patterns of abstraction.

## Development Approach

- Follow Test-Driven Development (TDD): Red → Green → Refactor
- Use "Tidy First" principles: separate structural changes from behavioral changes
- Write one test at a time, make it pass, then improve structure

## Test Plan - Pythonic Iterator Implementation

### Current Focus: Pythonic Iterator over Lists of Nodes

- [x] Test: Create a simple node with a single entry
- [x] Test: Node should be iterable (implement **iter**)
- [x] Test: Iterator should yield all entries from a single node
- [x] Test: Iterator should work across linked nodes
- [x] Test: Support for-loop iteration over node chain
- [x] Test: Support list() conversion of node chain
- [x] Test: Iterator should be lazy (not consume all at once)
- [x] Test: Support multiple iteration over same node chain

## Files to Create

- `node.py` - Basic node implementation
- `linked_list.py` - Linked list operations
- `iterator.py` - Iterator implementations
- `test_node.py` - Tests for node functionality
- `test_linked_list.py` - Tests for linked list operations
- `test_iterator.py` - Tests for iterator patterns
- `examples.py` - Usage examples showing generalization

## Key Generalization Concepts to Demonstrate

1. **Abstraction**: Moving from concrete to abstract implementations
2. **Polymorphism**: Different implementations of the same interface
3. **Composition**: Building complex behavior from simple components
4. **Strategy Pattern**: Pluggable algorithms for iteration
5. **Template Method**: Common structure with varying implementations
6. **Iterator Pattern**: Standardized way to traverse collections

## Notes

- Each test should be small and focused on one behavior
- Commit after each passing test
- Refactor only when tests are green
- Show evolution from simple to complex through git history
