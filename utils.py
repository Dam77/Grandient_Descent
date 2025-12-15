def ask_parameter(iterations: int, tx: float) -> tuple[int, float]:
    iterations = int(input(f"Enter the number of iterations (default {iterations}): "))
    tx = float(input(f"Enter the learning rate"))
    return iterations, tx
