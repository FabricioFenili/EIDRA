from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class PatchProposal:
    target_file: str
    content: str


class PatchGenerator:
    def generate(self, target_file: str, content: str) -> PatchProposal:
        return PatchProposal(target_file=target_file, content=content)
