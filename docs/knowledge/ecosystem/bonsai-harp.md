---
type: Component
title: Bonsai and Harp — the acquisition runtime and hardware
description: Bonsai is the reactive-dataflow acquisition engine that runs an experiment's main.bonsai workflow; Harp is the hardware device ecosystem, sharing a common clock for sub-millisecond synchronization. The schemas the framework defines ultimately configure both.
resource: https://github.com/AllenNeuralDynamics/Aind.Behavior.VrForaging
tags: [bonsai, harp, acquisition, hardware, runtime]
timestamp: 2026-07-27T00:00:00Z
---

# Bonsai and Harp — the acquisition runtime and hardware

These are the external, non-Python systems the framework exists to configure. [Schema-first codegen](../concepts/schema-first.md) targets Bonsai; the [`Rig`](../concepts/rig-task-session.md) model describes Harp hardware.

## Bonsai — the acquisition runtime

[Bonsai](https://bonsai-rx.org) is a reactive dataflow programming environment (.NET Framework 4.8). Each experiment repo ships:

- `src/main.bonsai` — the top-level acquisition workflow launched at runtime. At launch it deserializes the three input JSON files ([rig/task/session](../concepts/rig-task-session.md)), instantiates hardware, and runs the closed loop.
- `src/Extensions/*.bonsai` — reusable sub-workflows (hardware setup, logging, visualizers, task logic).
- `src/Extensions/*.cs` — custom C# operators, compiled together with the generated `*.Generated.cs` into an assembly named `Extensions` via `Extensions.csproj`. The workflow references the generated types through `clr-namespace:<Namespace>;assembly=Extensions`.

The generated C# classes are the **strongly-typed representation of the Python schema inside Bonsai** — the mechanism that keeps the acquisition runtime in lockstep with the Pydantic models. In richer paradigms Bonsai also separates a hard-real-time hardware tier from a soft-real-time tier (VR rendering + task logic) via a message bus, and renders VR with BonVision/OpenGL and live panels with ImGui/ImPlot (see [VR Foraging](../experiments/vr-foraging.md)).

The framework provides low-level launch primitives in `aind_behavior_services/utils.py` (`run_bonsai_process`, `open_bonsai_process`, `_build_bonsai_process_command`); [clabe](clabe.md)'s `AindBehaviorServicesBonsaiApp` builds on these.

## Harp — the hardware ecosystem

[Harp](https://harp-tech.org) is an open standard for behavioral-neuroscience hardware. Devices are addressed by COM port in the `Rig` and **share a common hardware clock**, giving sub-millisecond, drift-corrected alignment across all data streams.

- The framework's Harp device classes are **code-generated** from the harp-tech `whoami.yml` registry into `rig/_harp_gen.py` (see [schema-first](../concepts/schema-first.md)), keeping the device library in sync with the community registry. `validate_harp_clock_output` checks clock-output count against the number of Harp devices.
- Typical devices (from VR Foraging): Behavior board (reward valve, digital I/O), Olfactometer(s), a lickometer (LicketySplit), Treadmill rotary encoder with a controllable brake (programmable friction), sniff detector, a White Rabbit clock generator, an AIND motorized manipulator (positions the lick spout), triggered Spinnaker/FLIR cameras, environment sensor, and display.
- Harp data is logged as per-device de-multiplexed binary (`<Device>.harp`); see [data contracts & standards](../concepts/data-contracts-and-standards.md). `contraqctor` reads it via `harp-python`.

## Version pinning

Acquisition is fully version-pinned for reproducibility: a `.bonsai/` config locks the Bonsai version and every NuGet/Harp package, and `uv` locks the Python environment. This is what makes an experiment a reproducible [black box](../overview.md).

# Citations
1. https://bonsai-rx.org
2. https://harp-tech.org
3. src/aind_behavior_services/rig/_harp_gen.py, rig/harp.py
