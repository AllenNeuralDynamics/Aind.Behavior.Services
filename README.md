# aind-behavior-services

A repository containing code for data acquisition and processing for AIND behavior rigs.

---

## Deployment

Install the [prerequisites](#prerequisites) mentioned below.
From the root of the repository, run `./scripts/deploy.ps1` to bootstrap both python and bonsai environments.

---

## Prerequisites

These should only need to be installed once on a fresh new system, and are not required if simply refreshing the install or deploying to a new folder.

- Windows 10 or 11
- Run `./scripts/install_dependencies.ps1` to automatically install dependencies
- The following dependencies should be manually installed:
  - [FTDI CDM Driver 2.12.28](https://www.ftdichip.com/Drivers/CDM/CDM21228_Setup.zip) (serial port drivers for HARP devices)
  - [Spinnaker SDK 1.29.0.5](https://www.flir.co.uk/support/products/spinnaker-sdk/#Downloads) (device drivers for FLIR cameras)
    - On FLIR website: `Download > archive > 1.29.0.5 > SpinnakerSDK_FULL_1.29.0.5_x64.exe`
---

## Generating valid JSON input files

One of the core principles of this repository is the strict adherence to [json-schemas](https://json-schema.org/). We use [Pydantic](https://pydantic.dev/) as a way to write and compile our schemas, but also to generate valid JSON input files. These files can be used by Bonsai (powered by [Bonsai.SGen](https://github.com/bonsai-rx/sgen) code generation tool) or to simply record metadata. Examples of how to interact with the library can be found in the `./examples` folder.

---

## Regenerating schemas

Once a Pydantic model is updated, updates to all downstream dependencies must be made to ensure that the ground-truth data schemas (and all dependent interoperability tools) are also updated. This can be achieved by running the `./scripts/renegerate.ps1` script from the root of the repository.
This script will regenerate all `json-schemas` along with `C#` code (`./scr/Extensions`) used by the Bonsai environment.

---

## Contributors

Contributions to this repository are welcome! However, please ensure that your code adheres to the recommended DevOps practices below:

### Linting

We use [flake8](https://flake8.pycqa.org/), [black](https://black.readthedocs.io/), and [isort](https://pycqa.github.io/isort/) as our linting tools.

### Testing

Attempt to add tests when new features are added.
To run the currently available tests, run `python -m unittest` from the root of the repository.

### Versioning

Where possible, adhere to [Semantic Versioning](https://semver.org/).

---

## Project dependency tree

![Dependency tree](https://github.com/AllenNeuralDynamics/Aind.Behavior.Services/raw/main/assets/dependency_tree.drawio.svg)
