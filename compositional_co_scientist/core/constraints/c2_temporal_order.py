"""C2 constraint: Temporal Order enforcement via state machine.

This constraint enforces the correct temporal ordering of workflow phases:
GENERATE -> EVALUATE -> SELECT -> SYNTHESIZE

Invalid transitions (e.g., skipping evaluation) are blocked to maintain
workflow integrity and prevent premature conclusions.
"""
from compositional_co_scientist.core.errors import InvalidTransitionError


class WorkflowStateMachine:
    """State machine for enforcing C2 temporal order constraint.

    The state machine tracks workflow progression through valid states
    and enforces that transitions follow the prescribed order:

    IDLE -> GENERATING -> EVALUATING -> SELECTING -> SYNTHESIZING -> COMPLETE -> IDLE

    Special transitions:
    - SELECTING -> GENERATING: Allowed for regeneration when diversity quota not met
    - Any state -> ERROR: On constraint violation (handled externally)
    - ERROR -> IDLE: After resolution or user abort
    """

    VALID_TRANSITIONS = {
        "IDLE": ["GENERATING"],
        "GENERATING": ["EVALUATING"],
        "EVALUATING": ["SELECTING"],
        "SELECTING": ["SYNTHESIZING", "GENERATING"],  # GENERATING for regeneration
        "SYNTHESIZING": ["COMPLETE"],
        "COMPLETE": ["IDLE"],
        "ERROR": ["IDLE"],
    }

    def __init__(self):
        """Initialize the state machine in IDLE state."""
        self.current_state = "IDLE"

    def transition(self, from_state: str, to_state: str) -> bool:
        """Attempt a state transition.

        Args:
            from_state: The expected current state (must match actual current state).
            to_state: The desired next state.

        Returns:
            True if transition is successful.

        Raises:
            InvalidTransitionError: If from_state doesn't match current state,
                                    or if to_state is not a valid transition from from_state.
        """
        # Check state mismatch
        if from_state != self.current_state:
            raise InvalidTransitionError(
                f"State mismatch: expected {from_state}, but current state is {self.current_state}"
            )

        # Check valid transition
        valid_targets = self.VALID_TRANSITIONS.get(from_state, [])
        if to_state not in valid_targets:
            raise InvalidTransitionError(
                f"C2 violated: Invalid transition {from_state} -> {to_state}. "
                f"Valid transitions from {from_state}: {valid_targets}"
            )

        # Perform transition
        self.current_state = to_state
        return True

    def is_valid_transition(self, from_state: str, to_state: str) -> bool:
        """Check if a transition would be valid without actually transitioning.

        Args:
            from_state: The starting state to check.
            to_state: The target state to check.

        Returns:
            True if the transition is valid, False otherwise.
        """
        valid_targets = self.VALID_TRANSITIONS.get(from_state, [])
        return to_state in valid_targets

    def reset(self):
        """Reset the state machine to IDLE state."""
        self.current_state = "IDLE"

    def __str__(self):
        """Return string representation of current state."""
        return f"WorkflowStateMachine(state={self.current_state})"
