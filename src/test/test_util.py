# File: test_util.py
import random

def mock_input_pre_flop(prompt):
    """Handles pre-flop round actions with no raises."""
    # Pre-flop round: everyone just calls or checks, no raises
    if "Alice" in prompt:
        return "check"
    elif "Bob" in prompt:
        return "check"
    elif "Charlie" in prompt:
        return "check"
    return "check"

def mock_input_other(prompt):
    """Handles flop, turn, and river rounds where Bob raises randomly between 20 to 50."""
    if "Bob" in prompt:
        return "raise"
    elif "Enter the raise amount:" in prompt:
        raise_amount = random.randint(20, 50)
        return str(raise_amount)
    elif "Alice" in prompt or "Charlie" in prompt:
        return "call"
    return "check"

def mock_input_for_all(prompt):
    # Track whether Bob has appeared for the first time
    if not hasattr(mock_input_for_all, 'bob_first_time'):
        mock_input_for_all.bob_first_time = True  # First time flag for Bob

    # Alice and Charlie: always check or call based on the situation
    if "Alice" in prompt or "Charlie" in prompt:
        if "call" in prompt:
            return "call"
        return "check"
    
    # Bob: first time check, after that raise between 20 and 50
    if "Bob" in prompt:
        if mock_input_for_all.bob_first_time:
            mock_input_for_all.bob_first_time = False  # Set to False after first check
            return "check"
        else:
            return "raise"
    
    # When the prompt asks for the raise amount (for Bob after the first time)
    if "Enter the raise amount" in prompt:
        return str(random.randint(20, 50))

    # Default behavior if prompt doesn't match
    return "check"
