Architecture
##############

From the point of view of the software, an experiment instance can be seen as a "black box" function that takes a set of parameters (configuration) and produces a set of data (results). This has several implications, the most important of which is that, given a set of parameters and a `function`, one should be able to reproduce the same experiment.

This is the main goal of the `aind_behavior_services` framework: to provide a set of tools, patterns and standards to generate, maintain and produce data from behavior experiments.


Domain-specific language for experiment instantiation
==================================================================

When thinking about `parameters` of a behavior experiment, several examples come to mind:
   - The calibration parameters of a device (e.g. the weight of water delivered by a valve)
   - The delay between two stimuli presented to the animal
   - Metadata associated with the experiment (e.g. the date of the experiment, the animal ID, etc.)

Strategies to keep track of these parameters vary widely. One can hard-code parameters together with the code. This makes the "black box" a nullary function, as the parameters are not stored anywhere. This approach is not ideal since no settings can be changed without modifying the code.

Alternatively, one can store parameters in configuration files (e.g. a `json` or `csv` file). While affording flexibility, schema-free configuration files are not ideal since they do not provide a way to enforce the structure of the parameters. This can lead to inconsistencies and errors when reading the parameters.

An alternative is to define schemas that constrain the domain and type of the parameters. This approach offers several advantages:

   - Allows the definition of types and constraints for each parameter
   - Provides an easy way to validate the parameters, even before running the experiment
   - Provides an easy way to interface with databases, file systems, etc., by providing an easy way to serialize and deserialize the parameters
   - Picking a schema language that is widely adopted, such as `json-schema <https://json-schema.org/>`_, affords the use of a vast toolkit of interoperable libraries and tools
   - Provides an explicit way to document parameters in a machine-readable way
   - Provides an implicit way to document the parameter space via the structure of the schema itself
   - Provides a way to version control the language of the parameters since the schema language can be easily versioned and diff'ed when needed

As with most things, there is no free lunch. The main drawback of this approach is that it requires a bit more upfront work to define the schemas.

To help with this process, the `aind_behavior_services` framework adopts standard `json-schema <https://json-schema.org/>`_ schemas and uses `pydantic <https://docs.pydantic.dev/>`_ to compile Python classes into these.


`Rig`, `Session` and `Task`
-----------------------------------------------------

How are these parameters used in practice? In theory, one could define a single `schema` that contains all possible parameters for the experiment. In practice, this is not ideal since it would lead to a monolithic schema that is hard to maintain and understand. Instead, we define a set of three schemas that generally model the way we interact with experiments:

   - `Rig`: Is concerned with the hardware configuration of the experiment. Examples include: Device's :py:class:`~aind_behavior_services.calibration.Calibration`, COM ports expected to be used, socket endpoints, etc.
   - `Task`: Is concerned with settings that are specific to the behavior experiment. These parameters are usually set by the experiment to control the behavior software but are abstracted from hardware details. Examples include: the delay between two stimuli, the parameterization of a distribution to draw reward amounts from, etc.
   - `Session`: Is concerned with metadata necessary to run a single experiment instance. While the previous two instances are expected to be reused across several different experimental sessions, the `Session` instance is expected to be unique to a single experiment. It keeps track of metadata associated with the experiment such as date, subject ID, experimenter name, etc.

These three schemas are materialized in the `aind_behavior_services` framework as three classes: :py:class:`~aind_behavior_services.rig.Rig`, :py:class:`~aind_behavior_services.task.Task` and :py:class:`~aind_behavior_services.session.Session`.

Currently, we approach the use of these three classes in distinct ways:

   - `Rig` and `Task` are meant to provide a thin base class that is to be modified to model different experiments. This is necessary as distinct experiments will likely validate against distinct respective schemas;
   - `Session` is used to store metadata associated with the experiment. While in theory it can be subclassed and extended, in practice we have found little need to do so and simply use the base class.

Inheriting from these base classes ensures that basic functionality can be provided across tasks and rigs, especially when interacting with databases for parameter storage and retrieval.


Concrete implementations
-----------------------------------------------------

Examples of concrete implementations of these classes can be found in implementations of different behavior tasks:
   - `Force Foraging <https://github.com/AllenNeuralDynamics/Aind.Behavior.ForceForaging>`_
   - `Telekinesis <https://github.com/AllenNeuralDynamics/Aind.Behavior.Telekinesis>`_
   - `VR Foraging <https://github.com/AllenNeuralDynamics/Aind.Behavior.VrForaging>`_

but also physiology data acquisition platforms:
   - `Fip <https://github.com/AllenNeuralDynamics/Aind.Physiology.Fip>`_

and other smaller workflows:
   - `Olfactometer calibration <https://github.com/AllenNeuralDynamics/Aind.Behavior.Device.Olfactometer>`_
   - `Water valve calibration <https://github.com/AllenNeuralDynamics/Aind.Behavior.Device.WaterTuner>`_


Tooling
==================================================================
Adopting an underlying framework for experiment definition also affords the use of other tooling and patterns:


Automated API documentation
------------------------------

Several Sphinx extensions are available to interact with `json-schema` and `pydantic` models. These can be used to automatically generate class-level API as well as diagrams of the class hierarchy. For an example, see the `docs/api.session.rst` file.
