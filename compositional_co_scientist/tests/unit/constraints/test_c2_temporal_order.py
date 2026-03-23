"""Tests for the C2 temporal order constraint."""
import pytest
from compositional_co_scientist.core.constraints.c2_temporal_order import WorkflowStateMachine
from compositional_co_scientist.core.errors import InvalidTransitionError


def test_c2_valid_transition_generating_to_evaluating():
    """Test that C2 allows valid transition from GENERATING to EVALUATING."""
    fsm = WorkflowStateMachine()
    fsm.transition("IDLE", "GENERATING")
    fsm.transition("GENERATING", "EVALUATING")
    assert fsm.current_state == "EVALUATING"


def test_c2_valid_transition_evaluating_to_selecting():
    """Test that C2 allows valid transition from EVALUATING to SELECTING."""
    fsm = WorkflowStateMachine()
    fsm.transition("IDLE", "GENERATING")
    fsm.transition("GENERATING", "EVALUATING")
    fsm.transition("EVALUATING", "SELECTING")
    assert fsm.current_state == "SELECTING"


def test_c2_invalid_transition_generating_to_selecting():
    """Test that C2 blocks invalid transition from GENERATING to SELECTING (skip evaluation)."""
    fsm = WorkflowStateMachine()
    fsm.transition("IDLE", "GENERATING")
    with pytest.raises(InvalidTransitionError):
        fsm.transition("GENERATING", "SELECTING")


def test_c2_invalid_transition_evaluating_to_generating():
    """Test that C2 blocks invalid transition from EVALUATING to GENERATING (skip selection)."""
    fsm = WorkflowStateMachine()
    fsm.transition("IDLE", "GENERATING")
    fsm.transition("GENERATING", "EVALUATING")
    with pytest.raises(InvalidTransitionError):
        fsm.transition("EVALUATING", "GENERATING")


def test_c2_invalid_transition_selecting_to_evaluating():
    """Test that C2 blocks invalid backwards transition from SELECTING to EVALUATING."""
    fsm = WorkflowStateMachine()
    fsm.transition("IDLE", "GENERATING")
    fsm.transition("GENERATING", "EVALUATING")
    fsm.transition("EVALUATING", "SELECTING")
    with pytest.raises(InvalidTransitionError):
        fsm.transition("SELECTING", "EVALUATING")


def test_c2_state_mismatch():
    """Test that C2 raises error when from_state doesn't match current state."""
    fsm = WorkflowStateMachine()
    fsm.transition("IDLE", "GENERATING")
    # Try to transition from EVALUATING when we're actually in GENERATING
    with pytest.raises(InvalidTransitionError):
        fsm.transition("EVALUATING", "SELECTING")


def test_c2_selecting_to_synthesizing():
    """Test that C2 allows valid transition from SELECTING to SYNTHESIZING."""
    fsm = WorkflowStateMachine()
    fsm.transition("IDLE", "GENERATING")
    fsm.transition("GENERATING", "EVALUATING")
    fsm.transition("EVALUATING", "SELECTING")
    fsm.transition("SELECTING", "SYNTHESIZING")
    assert fsm.current_state == "SYNTHESIZING"


def test_c2_selecting_to_generating_regeneration():
    """Test that C2 allows transition from SELECTING to GENERATING for regeneration."""
    fsm = WorkflowStateMachine()
    fsm.transition("IDLE", "GENERATING")
    fsm.transition("GENERATING", "EVALUATING")
    fsm.transition("EVALUATING", "SELECTING")
    # Diversity quota not met, need to regenerate
    fsm.transition("SELECTING", "GENERATING")
    assert fsm.current_state == "GENERATING"


def test_c2_complete_to_idle():
    """Test that C2 allows transition from COMPLETE to IDLE."""
    fsm = WorkflowStateMachine()
    fsm.transition("IDLE", "GENERATING")
    fsm.transition("GENERATING", "EVALUATING")
    fsm.transition("EVALUATING", "SELECTING")
    fsm.transition("SELECTING", "SYNTHESIZING")
    fsm.transition("SYNTHESIZING", "COMPLETE")
    fsm.transition("COMPLETE", "IDLE")
    assert fsm.current_state == "IDLE"


def test_c2_error_to_idle():
    """Test that C2 allows transition from ERROR to IDLE after resolution."""
    fsm = WorkflowStateMachine()
    fsm.transition("IDLE", "GENERATING")
    # Simulate error state (would normally be set by constraint violation)
    fsm.current_state = "ERROR"
    fsm.transition("ERROR", "IDLE")
    assert fsm.current_state == "IDLE"
