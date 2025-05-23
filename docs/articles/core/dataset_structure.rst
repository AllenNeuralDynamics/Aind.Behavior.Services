Dataset structure
---------------------

Version
#############
0.1.0-draft

Introduction
#############

The goal of this document is layout the generic structure of a dataset generated by any of the behavior tasks or other experiments run with this framework. This structure is designed to be flexible and allow for the inclusion of any type of data generated by the experiments. The structure is designed to be easily navigable and allow for the easy retrieval of data for analysis.
The general structure of the dataset should as stable as possible moving forward, yet flexibly support new data-types without breaking changes.
All data-types to be included in the dataset should be documented in this repository.

Format specification
#########################
Datasets will generally following the following structure:


.. code-block:: none

    📂───<AnimalId>_<Datetime>
    ├───<Modality>
    │   ├───<DataStream1>
    │   ├───<DataStream2>
    │   ├───<SubFolder>
    │   │   ├───<DataStream1>
    │   │   ├───<DataStream2>
    │   │   └───<DataStreamN>
    │   └───Logs
    │       ├───<DataStreamFoo>
    |       ├───session_input.json
    │       ├───rig_input.json
    │       └───tasklogic_input.json
    └───<Modality>
        ├───<DataStream1>
        └───<DataStream2>


where:

- ``<AnimalId>`` is the unique identifier for the animal, usually an integer.
- ``<Datetime>`` is the date and time of the session in the format specified in  :ref:`datetime <datetime_target>`.
- ``<Modality>`` is the type of data being stored and MUST be one of the modalities defined by `aind-data-schema-models <https://github.com/AllenNeuralDynamics/aind-data-schema-models/tree/main>`_
- ``<DataStreamN>`` is a data stream whose format should be specified in :doc:`Data formats </articles/data_standards>`
- ``<Modality>/Metadata/*_input.json`` are the serialized input files for the session, rig, and task logic respectively.
