"""Minimal Cog model, just enough to prove the GitHub -> Replicate pipeline."""

from cog import BaseRunner, Input


class Runner(BaseRunner):
    def setup(self) -> None:
        """Runs once per container. Load weights here in a real model."""
        self.greeting = "hello"

    def run(
        self,
        name: str = Input(description="Who to greet", default="Moh"),
        repeat: int = Input(description="How many times", default=1, ge=1, le=5),
    ) -> str:
        """Runs once per prediction."""
        return " ".join([f"{self.greeting} {name}"] * repeat)
