class ResearchRegistry:
    def __init__(self):
        self._hypotheses = []

    def register_hypothesis(self, hypothesis) -> None:
        self._hypotheses.append(hypothesis)
