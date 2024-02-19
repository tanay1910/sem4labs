def water_jug_problem(jug1_cap, jug2_cap, target):
  """
  Solves the water jug problem using breadth-first search.

  Args:
      jug1_cap: The capacity of the first jug.
      jug2_cap: The capacity of the second jug.
      target: The target amount of water to reach.

  Returns:
      A list of states representing the solution path, or None if no solution exists.
  """

  # Initialize the queue with the starting state
  queue = [(0, jug2_cap)]  # (jug1, jug2)

  # Visited states to avoid revisiting
  visited = set()

  while queue:
    print('q: ',queue)
    # Get the next state from the queue
    current_jug1, current_jug2 = queue.pop(0)
    print('current ', current_jug1, current_jug2)
   

    # Check if the target is reached
    if current_jug1 == target:
      return [(current_jug1, current_jug2)]

    # Add the current state to visited
    visited.add((current_jug1, current_jug2))

    # Generate possible next states
    for new_jug1, new_jug2 in [
        # Fill jug1
        (jug1_cap, current_jug2),
        # Fill jug2
        (current_jug1, jug2_cap),
        # Empty jug1
        (0, current_jug2),
        # Empty jug2
        (current_jug1, 0),
        # Pour from jug1 to jug2 (up to jug2's capacity)
        (max(0, current_jug1 - (jug2_cap - current_jug2)), min(jug2_cap, current_jug1 + current_jug2)),
        # Pour from jug2 to jug1 (up to jug1's capacity)
        (min(jug1_cap, current_jug1 + current_jug2), max(0, current_jug2 - (jug1_cap - current_jug1))),
    ]:
      # Skip invalid states or visited states
      if 0 <= new_jug1 <= jug1_cap and 0 <= new_jug2 <= jug2_cap and (new_jug1, new_jug2) not in visited:
        queue.append((new_jug1, new_jug2))

  # No solution found
  return None

# Example usage
jug1_cap = 5
jug2_cap = 3
target = 4

solution = water_jug_problem(jug1_cap, jug2_cap, target)

if solution:
  print("Solution found:")
  for state in solution:
    print(f"Jug1: {state[0]}, Jug2: {state[1]}")
else:
  print("No solution found")
