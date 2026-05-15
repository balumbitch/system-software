def next_state(state: str, event: str) -> str:
    transitions = {
        ("NEW", "PAY_OK"): "PAID",
        ("NEW", "PAY_FAIL"): "CANCELLED",
    }
    return transitions.get((state, event), state)
