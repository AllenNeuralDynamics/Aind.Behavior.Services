# Ecosystem

The tools `aind-behavior-services` brings together. Dependencies point downward: `aind-behavior-curriculum` → **aind-behavior-services** → `clabe` and the experiment repos; `contraqctor` sits downstream of the acquired data. See the [overview](../overview.md) for the layered diagram.

## Contents

- [aind-behavior-services.md](aind-behavior-services.md) — the framework package itself: package layout and public API.
- [clabe.md](clabe.md) — the launcher framework that picks configs, runs Bonsai, and maps/transfers data.
- [contraqctor.md](contraqctor.md) — the downstream data-contract + quality-control library.
- [curriculum.md](curriculum.md) — automated training: curricula as graphs of task-config stages.
- [bonsai-harp.md](bonsai-harp.md) — the acquisition runtime (Bonsai) and hardware ecosystem (Harp) the schemas configure.
