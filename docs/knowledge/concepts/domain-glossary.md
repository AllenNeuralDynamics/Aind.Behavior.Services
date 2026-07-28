---
type: Glossary
title: Scientific domain glossary
description: The behavioral-neuroscience vocabulary the software models — rig, task, session, patch, virtual site, choice/rejection, reward dynamics, environment models — grounded in the VR Foraging paradigm that motivates the framework.
resource: https://github.com/AllenNeuralDynamics/Aind.Behavior.VrForaging
tags: [glossary, vocabulary, domain, foraging, science]
timestamp: 2026-07-27T00:00:00Z
---

# Scientific domain glossary

The framework's abstractions map directly onto behavioral-neuroscience concepts. This glossary defines the domain terms — most sharply exercised by the [VR Foraging](../experiments/vr-foraging.md) paradigm, whose white paper is the canonical source. Terminology here follows that project's style guide (e.g. "stop and harvest / choice", never "poke" or "response").

## Framework-level terms

- **Rig** — the physical apparatus: Harp devices + COM ports, olfactometer channels/odorants, treadmill and water-valve calibrations, cameras, motorized spout, display. Modeled by [`Rig`](rig-task-session.md).
- **Task** — what the animal experiences: environment structure, patches, reward dynamics, virtual sites, operation control, adaptive updaters. Modeled by [`Task`](rig-task-session.md).
- **Session** — one run: subject, date, experimenter, output paths. Modeled by [`Session`](rig-task-session.md).

## VR-Foraging paradigm terms

The paradigm: a thirsty, head-fixed mouse runs on a treadmill; its locomotion drives forward motion through a rendered linear virtual corridor tiled into typed sites. Patches are marked by odor cues; harvesting depletes a patch, so the animal must decide *when to leave* and pay a *travel cost* to reach a fresher one.

- **Virtual site** — a tile of the corridor. Types: **InterPatch** (travel segment = the travel cost), **InterSite** (spacing within a patch), **RewardSite** (odor-cued harvest location), **PostPatch** (optional post-patch segment, e.g. added friction). Lengths are drawn from parameterized [distributions](rig-task-session.md) (typically truncated exponentials).
- **Patch** — a group of sites sharing: an **odor specification** (a mixture vector of up to 3 odor-channel concentrations = the identity cue), a **reward specification** (`amount` × `probability` × `available` count, plus optional operant logic), a **visual stimuli specification**, a per-site **friction** coefficient (rendered by the treadmill brake), **reward dynamics** (chained reward functions implementing depletion/replenishment), and **patch terminators** (end conditions).
- **Odor site / RewardSite** — where harvest attempts happen; odor-cued.
- **Reward** — water; delivered via `GiveReward` / `ForceGiveReward` events.
- **Choice vs. rejection** — at an odor-cued reward site the animal either **stops and harvests** (a *choice*) or **runs through** (a *rejection*). Operant logic may require the animal to hold velocity below a threshold for a `stop_duration` to count as a stop.
- **Trial** — *not* a native unit of this paradigm; the atomic unit is the patch / reward-site / choice. "Trial" appears only in downstream analysis (dashboard trial tables built via an NWB `TrialTableProcessor`).
- **Environment model** — a **Markov environment** (patches + transition matrix
  + first-state occupancy) or a **sequence environment** (ordered/sampled patch
  indices), grouped into **blocks** with end-conditions that enable within-session contingency changes.

## Task-DSL primitives

Composable grammar pieces (VR Foraging glossary): `RewardFunction` (Patch / Outside / OnThisPatchEntry / Persistent), `PatchUpdateFunction` (ClampedRate / Multiplicative / Saturating / SetValue / LookupTable / Ctcm = continuous-time Markov), `PatchTerminator`, `VirtualSiteGenerator`, `OperantLogic`, `NumericalUpdater`, and `OperationControl` (Odor / Position / Audio).

## Scientific motivation (why the paradigm)

Foraging is ethologically natural and quantitatively tractable (optimal foraging theory / Marginal Value Theorem; reinforcement learning). Two headline claims motivate the design: mice are **sensitive to reward statistics** (they track depletion and adjust leaving decisions), and the task **evokes cognition via stimulus–action dissociation** (the same odor cue can demand opposite actions depending on internal state), forcing reliance on latent internal variables in a way a two-alternative choice task cannot.

# Citations
1. vr-foraging-white-paper `WHITEPAPER_DRAFT.md` (paradigm, glossary Appendix A)
2. vr-foraging-white-paper `docs/context/style-guide.md` (terminology table)
