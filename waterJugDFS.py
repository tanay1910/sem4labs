def water_jug_problem(jug1_capacity, jug2_capacity, target):
  """
  Solves the water jug problem using breadth-first search.

  Args:
      jug1_capacity: The capacity of the first jug.
      jug2_capacity: The capacity of the second jug.
      target: The target amount of water to reach.

  Returns:
      A list of states representing the solution path, or None if no solution exists.
  """

  # Initialize the queue with the starting state
  stack = [(0, jug2_capacity)]  # (jug1, jug2)

  # Visited states to avoid revisiting
  visited = set()

  while stack:
    print('stack: ',stack[::-1])
    # Get the next state from the stack
    current_jug1, current_jug2 = stack.pop()
    print('current ', current_jug1, current_jug2)
   

    # Check if the target is reached
    if current_jug1 == target:
      return [(current_jug1, current_jug2)]

    # Add the current state to visited
    visited.add((current_jug1, current_jug2))

    # Generate possible next states
    for new_jug1, new_jug2 in [
        # Fill jug1
        (jug1_capacity, current_jug2),
        # Fill jug2
        (current_jug1, jug2_capacity),
        # Empty jug1
        (0, current_jug2),
        # Empty jug2
        (current_jug1, 0),
        # Pour from jug1 to jug2 (up to jug2's capacity)
        (max(0, current_jug1 - (jug2_capacity - current_jug2)), min(jug2_capacity, current_jug1 + current_jug2)),
        # Pour from jug2 to jug1 (up to jug1's capacity)
        (min(jug1_capacity, current_jug1 + current_jug2), max(0, current_jug2 - (jug1_capacity - current_jug1))),
    ]:
      # Skip invalid states or visited states
      if 0 <= new_jug1 <= jug1_capacity and 0 <= new_jug2 <= jug2_capacity and (new_jug1, new_jug2) not in visited:
        stack.append((new_jug1, new_jug2))

  # No solution found
  return None

# Example usage
jug1_capacity = 5
jug2_capacity = 3
target = 2

solution = water_jug_problem(jug1_capacity, jug2_capacity, target)

if solution:
  print("Solution found:")
  for state in solution:
    print(f"Jug1: {state[0]}, Jug2: {state[1]}")
else:
  print("No solution found")
