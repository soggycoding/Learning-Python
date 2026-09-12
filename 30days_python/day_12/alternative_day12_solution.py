# Day 12: Modules - Alternative Solutions (Pass 2)

# ==============================================================================
# Level 1 - Exercise 1: random_user_id (Pass 2: Alternative Exploration)
# ==============================================================================
# Exploration Objectives:
# 1. Implementation Alternatives:
#    - Alternative A (List Comprehension with random.choice):
#      Build the 6-character token using a list comprehension + join with
#      `random.choice(pool)` rather than `random.choices(pool, k=6)`.
#    - Alternative B (Cryptographically Secure via secrets module):
#      Explore Python's built-in `secrets` module (e.g. `secrets.choice`) and observe
#      why security tokens and user session IDs prefer `secrets` over `random`.
#
# 2. Mechanistic Analysis & Trade-offs:
#    - Contrast `random.choices` (sampling WITH replacement) vs `random.sample` (sampling WITHOUT replacement).
#    - Analyze Time & Space Complexity: Compare bulk `random.choices` vs comprehension loop.
# ==============================================================================

# Write your Pass 2 solution below:

