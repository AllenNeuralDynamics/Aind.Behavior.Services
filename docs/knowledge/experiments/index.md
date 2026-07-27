# Experiments

How concrete experiments materialize on top of the framework. Each paradigm lives in its own repository that [subclasses Rig and Task](../concepts/rig-task-session.md), owns a Bonsai workflow, and regenerates its C# from its Pydantic models.

## Contents

- [anatomy-of-an-experiment-repo.md](anatomy-of-an-experiment-repo.md) — the canonical repository skeleton shared across the leaf repos, and the launcher pattern.
- [behavior-vs-experiment-repos.md](behavior-vs-experiment-repos.md) — the distinction between `Aind.Behavior.*` (one acquisition unit) and `Aind.Experiment.*` (a composition of several).
- [vr-foraging.md](vr-foraging.md) — the flagship paradigm: the science, the DSL, and the full pipeline. The reference implementation.
- [catalog.md](catalog.md) — the surveyed repos and their relative maturity.
