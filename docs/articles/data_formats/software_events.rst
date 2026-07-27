Software Events
------------------------------------------

Version
#############
0.2.0-draft

.. note::
    **Changed in 0.2.0-draft** (`#230 <https://github.com/AllenNeuralDynamics/Aind.Behavior.Services/issues/230>`_): ``SoftwareEvent`` files now use the ``.jsonl`` extension (`JSON Lines <https://jsonlines.org/>`_) instead of ``.json``. Each file was already a line-delimited sequence of JSON objects rather than a single JSON document, so ``.json`` was misleading. This is a breaking change at the file-system layer; ingestion tools such as `contraqctor <https://github.com/AllenNeuralDynamics/contraqctor/>`_ abstract the extension away.

Introduction
##############

For simplicity all software events will be logged following a common generic schema. This schema is described in this repository by the class:

:py:class:`~aind_behavior_services.data_types.SoftwareEvent` and implemented in a strict isomorphism in `AllenNeuralDynamics.AindBehaviorServices Bonsai package <https://www.nuget.org/packages/AllenNeuralDynamics.AindBehaviorServices/>`_.

This data format is used to address some issues / limitations of other formats, specifically Harp and CSV. Briefly:

- Most of the times, ``SoftwareEvent`` used to log events that happen on the PC side and can't be timestamped from a RTOS device. As a result, the `timestamp` field is a software time stamp, which is given by the time the event was logged (in total seconds). The time can be provided by a variety of sources, but we strongly recommend using a continuous stream of ``Harp Messages`` from a single device as a source of the latest timestamp. This is because the timestamps in the ``Harp Messages`` are synchronized with the distributed clock, and can be used to synchronize the software events with the device's data. Moreover, past benchmarks have shown that the jitter that results from this strategy is below 4ms.

    .. caution::
        While the temporal axis is the same as harp, it is important to note that the timestamp in the ``SoftwareEvent`` is not synchronized with the distributed clock and should not be used for precise synchronization during analysis!

- A ``SoftwareEvent`` can effectively be considered a generic on type ``T``, where ``T`` represents the type of the data embedded in the event. This is extremely useful since, if one assumes that ``T`` is serializable, then any type of event can be easily wrapped by this structure. This allows classes/records to be easily (de)serialized without having to worry about the specifics of the serialization process, while maintaining a stable wrapping structure (e.g. the existence of `timestamp`). Moreover, given the wide-spread use of JSON and pydantic in this library, this allows for a seamless integration when ingesting this data.

- Finally, the serialized data record does not need to be flat (e.g. harp message) and can instead by arbitrarily nested. This is useful when the event is complex and requires a more complex structure to be represented.

Format specification
####################################

The ``SoftwareEvent`` can exists as standalone files or part of a larger directory structure. In either case, the file name should be descriptive of the event that it represents (or even match the event name). The extension of the file will always be ``.jsonl`` (`JSON Lines <https://jsonlines.org/>`_), reflecting that each file is a line-delimited sequence of JSON objects rather than a single JSON document.

.. code-block:: none

    📦SoftwareEvents
    ┣ 📜Foo.jsonl
    ┣ 📜Bar.jsonl
    ┣ ...
    ┗ 📜Baz.jsonl

All ``SoftwareEvent`` files are expected to be demuxed by ``name``. This means that each file should contain a single event type.

Each file will thus simply be a series of lines where each line is a serialized JSON object with fields given by the :py:class:`~aind_behavior_services.data_types.SoftwareEvent` class. This is the `JSON Lines <https://jsonlines.org/>`_ convention: newline-delimited, one complete JSON object per line, so a file can be read and appended to incrementally without parsing the whole document.

Application notes
#####################


Logging
+++++++++++++++++++++++

For logging using bonsai see this `recipe <https://allenneuraldynamics.github.io/Bonsai.AllenNeuralDynamics/articles/core-logging.html#software-events>`_.


Ingestion
+++++++++++++++++++++++

To ingest the data, simply read the file line by line and either:

- Deserialize the JSON object as a generic dictionary
- Use :py:meth:`~aind_behavior_services.data_types.SoftwareEvent.model_validate_json` to deserialize, and validate, the JSON object as a :py:class:`~aind_behavior_services.data_types.SoftwareEvent` object.


File Quality Assurances
##########################

- All json objects are expected to be valid and complete in a given file.
- Files may be empty
- Files may contain any number of events
- Unless otherwise stated, `timestamp` field information should not be used for analysis that rely on temporal synchronization.