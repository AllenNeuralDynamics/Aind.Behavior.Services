//----------------------
// <auto-generated>
//     Generated using the NJsonSchema v10.9.0.0 (Newtonsoft.Json v13.0.0.0) (http://NJsonSchema.org)
// </auto-generated>
//----------------------


namespace AindBehaviorRigCalibration.AindManipulatorCalibration
{
    #pragma warning disable // Disable all warnings

    /// <summary>
    /// Load cells calibration class
    /// </summary>
    [System.CodeDom.Compiler.GeneratedCodeAttribute("Bonsai.Sgen", "0.3.0.0 (Newtonsoft.Json v13.0.0.0)")]
    [System.ComponentModel.DescriptionAttribute("Load cells calibration class")]
    [Bonsai.CombinatorAttribute()]
    [Bonsai.WorkflowElementCategoryAttribute(Bonsai.ElementCategory.Source)]
    public partial class AindManipulatorCalibration
    {
    
        private System.DateTimeOffset _calibrationDate;
    
        private string _deviceName = "AindManipulator";
    
        private string _description = "Calibration of the load cells system";
    
        private AindManipulatorCalibrationInput _input = new AindManipulatorCalibrationInput();
    
        private AindManipulatorCalibrationOutput _output = new AindManipulatorCalibrationOutput();
    
        private string _notes;
    
        public AindManipulatorCalibration()
        {
        }
    
        protected AindManipulatorCalibration(AindManipulatorCalibration other)
        {
            _calibrationDate = other._calibrationDate;
            _deviceName = other._deviceName;
            _description = other._description;
            _input = other._input;
            _output = other._output;
            _notes = other._notes;
        }
    
        [System.Xml.Serialization.XmlIgnoreAttribute()]
        [Newtonsoft.Json.JsonPropertyAttribute("calibration_date", Required=Newtonsoft.Json.Required.Always)]
        public System.DateTimeOffset CalibrationDate
        {
            get
            {
                return _calibrationDate;
            }
            set
            {
                _calibrationDate = value;
            }
        }
    
        /// <summary>
        /// Must match a device name in rig/instrument
        /// </summary>
        [Newtonsoft.Json.JsonPropertyAttribute("device_name")]
        [System.ComponentModel.DescriptionAttribute("Must match a device name in rig/instrument")]
        public string DeviceName
        {
            get
            {
                return _deviceName;
            }
            set
            {
                _deviceName = value;
            }
        }
    
        [Newtonsoft.Json.JsonPropertyAttribute("description")]
        public string Description
        {
            get
            {
                return _description;
            }
            set
            {
                _description = value;
            }
        }
    
        [System.Xml.Serialization.XmlIgnoreAttribute()]
        [Newtonsoft.Json.JsonPropertyAttribute("input", Required=Newtonsoft.Json.Required.Always)]
        public AindManipulatorCalibrationInput Input
        {
            get
            {
                return _input;
            }
            set
            {
                _input = value;
            }
        }
    
        [System.Xml.Serialization.XmlIgnoreAttribute()]
        [Newtonsoft.Json.JsonPropertyAttribute("output", Required=Newtonsoft.Json.Required.Always)]
        public AindManipulatorCalibrationOutput Output
        {
            get
            {
                return _output;
            }
            set
            {
                _output = value;
            }
        }
    
        [Newtonsoft.Json.JsonPropertyAttribute("notes")]
        public string Notes
        {
            get
            {
                return _notes;
            }
            set
            {
                _notes = value;
            }
        }
    
        public System.IObservable<AindManipulatorCalibration> Process()
        {
            return System.Reactive.Linq.Observable.Defer(() => System.Reactive.Linq.Observable.Return(new AindManipulatorCalibration(this)));
        }
    
        public System.IObservable<AindManipulatorCalibration> Process<TSource>(System.IObservable<TSource> source)
        {
            return System.Reactive.Linq.Observable.Select(source, _ => new AindManipulatorCalibration(this));
        }
    
        protected virtual bool PrintMembers(System.Text.StringBuilder stringBuilder)
        {
            stringBuilder.Append("calibration_date = " + _calibrationDate + ", ");
            stringBuilder.Append("device_name = " + _deviceName + ", ");
            stringBuilder.Append("description = " + _description + ", ");
            stringBuilder.Append("input = " + _input + ", ");
            stringBuilder.Append("output = " + _output + ", ");
            stringBuilder.Append("notes = " + _notes);
            return true;
        }
    
        public override string ToString()
        {
            System.Text.StringBuilder stringBuilder = new System.Text.StringBuilder();
            stringBuilder.Append(GetType().Name);
            stringBuilder.Append(" { ");
            if (PrintMembers(stringBuilder))
            {
                stringBuilder.Append(" ");
            }
            stringBuilder.Append("}");
            return stringBuilder.ToString();
        }
    }


    [System.CodeDom.Compiler.GeneratedCodeAttribute("Bonsai.Sgen", "0.3.0.0 (Newtonsoft.Json v13.0.0.0)")]
    [Bonsai.CombinatorAttribute()]
    [Bonsai.WorkflowElementCategoryAttribute(Bonsai.ElementCategory.Source)]
    public partial class AindManipulatorCalibrationInput
    {
    
        private Vector4 _fullStepToMm;
    
        public AindManipulatorCalibrationInput()
        {
        }
    
        protected AindManipulatorCalibrationInput(AindManipulatorCalibrationInput other)
        {
            _fullStepToMm = other._fullStepToMm;
        }
    
        [System.Xml.Serialization.XmlIgnoreAttribute()]
        [Newtonsoft.Json.JsonPropertyAttribute("full_step_to_mm")]
        public Vector4 FullStepToMm
        {
            get
            {
                return _fullStepToMm;
            }
            set
            {
                _fullStepToMm = value;
            }
        }
    
        public System.IObservable<AindManipulatorCalibrationInput> Process()
        {
            return System.Reactive.Linq.Observable.Defer(() => System.Reactive.Linq.Observable.Return(new AindManipulatorCalibrationInput(this)));
        }
    
        public System.IObservable<AindManipulatorCalibrationInput> Process<TSource>(System.IObservable<TSource> source)
        {
            return System.Reactive.Linq.Observable.Select(source, _ => new AindManipulatorCalibrationInput(this));
        }
    
        protected virtual bool PrintMembers(System.Text.StringBuilder stringBuilder)
        {
            stringBuilder.Append("full_step_to_mm = " + _fullStepToMm);
            return true;
        }
    
        public override string ToString()
        {
            System.Text.StringBuilder stringBuilder = new System.Text.StringBuilder();
            stringBuilder.Append(GetType().Name);
            stringBuilder.Append(" { ");
            if (PrintMembers(stringBuilder))
            {
                stringBuilder.Append(" ");
            }
            stringBuilder.Append("}");
            return stringBuilder.ToString();
        }
    }


    [System.CodeDom.Compiler.GeneratedCodeAttribute("Bonsai.Sgen", "0.3.0.0 (Newtonsoft.Json v13.0.0.0)")]
    [Bonsai.CombinatorAttribute()]
    [Bonsai.WorkflowElementCategoryAttribute(Bonsai.ElementCategory.Source)]
    public partial class AindManipulatorCalibrationOutput
    {
    
        public AindManipulatorCalibrationOutput()
        {
        }
    
        protected AindManipulatorCalibrationOutput(AindManipulatorCalibrationOutput other)
        {
        }
    
        public System.IObservable<AindManipulatorCalibrationOutput> Process()
        {
            return System.Reactive.Linq.Observable.Defer(() => System.Reactive.Linq.Observable.Return(new AindManipulatorCalibrationOutput(this)));
        }
    
        public System.IObservable<AindManipulatorCalibrationOutput> Process<TSource>(System.IObservable<TSource> source)
        {
            return System.Reactive.Linq.Observable.Select(source, _ => new AindManipulatorCalibrationOutput(this));
        }
    
        protected virtual bool PrintMembers(System.Text.StringBuilder stringBuilder)
        {
            return false;
        }
    
        public override string ToString()
        {
            System.Text.StringBuilder stringBuilder = new System.Text.StringBuilder();
            stringBuilder.Append(GetType().Name);
            stringBuilder.Append(" { ");
            if (PrintMembers(stringBuilder))
            {
                stringBuilder.Append(" ");
            }
            stringBuilder.Append("}");
            return stringBuilder.ToString();
        }
    }


    [System.CodeDom.Compiler.GeneratedCodeAttribute("Bonsai.Sgen", "0.3.0.0 (Newtonsoft.Json v13.0.0.0)")]
    [Bonsai.CombinatorAttribute()]
    [Bonsai.WorkflowElementCategoryAttribute(Bonsai.ElementCategory.Source)]
    public partial class AindManipulatorOperationControl
    {
    
        private System.Collections.Generic.List<AxisConfiguration> _axesConfiguration = new System.Collections.Generic.List<AxisConfiguration>();
    
        private System.Collections.Generic.List<Axis> _homingOrder = new System.Collections.Generic.List<Axis>();
    
        private Vector4 _initialPosition;
    
        public AindManipulatorOperationControl()
        {
        }
    
        protected AindManipulatorOperationControl(AindManipulatorOperationControl other)
        {
            _axesConfiguration = other._axesConfiguration;
            _homingOrder = other._homingOrder;
            _initialPosition = other._initialPosition;
        }
    
        [System.Xml.Serialization.XmlIgnoreAttribute()]
        [Newtonsoft.Json.JsonPropertyAttribute("AxesConfiguration")]
        public System.Collections.Generic.List<AxisConfiguration> AxesConfiguration
        {
            get
            {
                return _axesConfiguration;
            }
            set
            {
                _axesConfiguration = value;
            }
        }
    
        [System.Xml.Serialization.XmlIgnoreAttribute()]
        [Newtonsoft.Json.JsonPropertyAttribute("HomingOrder")]
        public System.Collections.Generic.List<Axis> HomingOrder
        {
            get
            {
                return _homingOrder;
            }
            set
            {
                _homingOrder = value;
            }
        }
    
        [System.Xml.Serialization.XmlIgnoreAttribute()]
        [Newtonsoft.Json.JsonPropertyAttribute("InitialPosition")]
        public Vector4 InitialPosition
        {
            get
            {
                return _initialPosition;
            }
            set
            {
                _initialPosition = value;
            }
        }
    
        public System.IObservable<AindManipulatorOperationControl> Process()
        {
            return System.Reactive.Linq.Observable.Defer(() => System.Reactive.Linq.Observable.Return(new AindManipulatorOperationControl(this)));
        }
    
        public System.IObservable<AindManipulatorOperationControl> Process<TSource>(System.IObservable<TSource> source)
        {
            return System.Reactive.Linq.Observable.Select(source, _ => new AindManipulatorOperationControl(this));
        }
    
        protected virtual bool PrintMembers(System.Text.StringBuilder stringBuilder)
        {
            stringBuilder.Append("AxesConfiguration = " + _axesConfiguration + ", ");
            stringBuilder.Append("HomingOrder = " + _homingOrder + ", ");
            stringBuilder.Append("InitialPosition = " + _initialPosition);
            return true;
        }
    
        public override string ToString()
        {
            System.Text.StringBuilder stringBuilder = new System.Text.StringBuilder();
            stringBuilder.Append(GetType().Name);
            stringBuilder.Append(" { ");
            if (PrintMembers(stringBuilder))
            {
                stringBuilder.Append(" ");
            }
            stringBuilder.Append("}");
            return stringBuilder.ToString();
        }
    }


    /// <summary>
    /// Motor axis available
    /// </summary>
    [System.CodeDom.Compiler.GeneratedCodeAttribute("Bonsai.Sgen", "0.3.0.0 (Newtonsoft.Json v13.0.0.0)")]
    public enum Axis
    {
    
        [System.Runtime.Serialization.EnumMemberAttribute(Value="0")]
        _0 = 0,
    
        [System.Runtime.Serialization.EnumMemberAttribute(Value="1")]
        _1 = 1,
    
        [System.Runtime.Serialization.EnumMemberAttribute(Value="2")]
        _2 = 2,
    
        [System.Runtime.Serialization.EnumMemberAttribute(Value="3")]
        _3 = 3,
    
        [System.Runtime.Serialization.EnumMemberAttribute(Value="4")]
        _4 = 4,
    }


    /// <summary>
    /// Axis configuration
    /// </summary>
    [System.CodeDom.Compiler.GeneratedCodeAttribute("Bonsai.Sgen", "0.3.0.0 (Newtonsoft.Json v13.0.0.0)")]
    [System.ComponentModel.DescriptionAttribute("Axis configuration")]
    [Bonsai.CombinatorAttribute()]
    [Bonsai.WorkflowElementCategoryAttribute(Bonsai.ElementCategory.Source)]
    public partial class AxisConfiguration
    {
    
        private Axis _axis;
    
        private int _stepAccelerationInterval = 100;
    
        private int _stepInterval = 100;
    
        private MicrostepResolution _microstepResolution = AindBehaviorRigCalibration.AindManipulatorCalibration.MicrostepResolution._0;
    
        private int _maximumStepInterval = 2000;
    
        private MotorOperationMode _motorOperationMode = AindBehaviorRigCalibration.AindManipulatorCalibration.MotorOperationMode._0;
    
        private int _maxLimit = 24000;
    
        private int _minLimit = -1;
    
        public AxisConfiguration()
        {
        }
    
        protected AxisConfiguration(AxisConfiguration other)
        {
            _axis = other._axis;
            _stepAccelerationInterval = other._stepAccelerationInterval;
            _stepInterval = other._stepInterval;
            _microstepResolution = other._microstepResolution;
            _maximumStepInterval = other._maximumStepInterval;
            _motorOperationMode = other._motorOperationMode;
            _maxLimit = other._maxLimit;
            _minLimit = other._minLimit;
        }
    
        [System.Xml.Serialization.XmlIgnoreAttribute()]
        [Newtonsoft.Json.JsonPropertyAttribute("axis", Required=Newtonsoft.Json.Required.Always)]
        public Axis Axis
        {
            get
            {
                return _axis;
            }
            set
            {
                _axis = value;
            }
        }
    
        /// <summary>
        /// Acceleration of the step interval in microseconds
        /// </summary>
        [Newtonsoft.Json.JsonPropertyAttribute("step_acceleration_interval")]
        [System.ComponentModel.DescriptionAttribute("Acceleration of the step interval in microseconds")]
        public int StepAccelerationInterval
        {
            get
            {
                return _stepAccelerationInterval;
            }
            set
            {
                _stepAccelerationInterval = value;
            }
        }
    
        /// <summary>
        /// Step interval in microseconds.
        /// </summary>
        [Newtonsoft.Json.JsonPropertyAttribute("step_interval")]
        [System.ComponentModel.DescriptionAttribute("Step interval in microseconds.")]
        public int StepInterval
        {
            get
            {
                return _stepInterval;
            }
            set
            {
                _stepInterval = value;
            }
        }
    
        [System.Xml.Serialization.XmlIgnoreAttribute()]
        [Newtonsoft.Json.JsonPropertyAttribute("microstep_resolution")]
        public MicrostepResolution MicrostepResolution
        {
            get
            {
                return _microstepResolution;
            }
            set
            {
                _microstepResolution = value;
            }
        }
    
        [Newtonsoft.Json.JsonPropertyAttribute("maximum_step_interval")]
        public int MaximumStepInterval
        {
            get
            {
                return _maximumStepInterval;
            }
            set
            {
                _maximumStepInterval = value;
            }
        }
    
        [System.Xml.Serialization.XmlIgnoreAttribute()]
        [Newtonsoft.Json.JsonPropertyAttribute("motor_operation_mode")]
        public MotorOperationMode MotorOperationMode
        {
            get
            {
                return _motorOperationMode;
            }
            set
            {
                _motorOperationMode = value;
            }
        }
    
        [Newtonsoft.Json.JsonPropertyAttribute("max_limit")]
        public int MaxLimit
        {
            get
            {
                return _maxLimit;
            }
            set
            {
                _maxLimit = value;
            }
        }
    
        [Newtonsoft.Json.JsonPropertyAttribute("min_limit")]
        public int MinLimit
        {
            get
            {
                return _minLimit;
            }
            set
            {
                _minLimit = value;
            }
        }
    
        public System.IObservable<AxisConfiguration> Process()
        {
            return System.Reactive.Linq.Observable.Defer(() => System.Reactive.Linq.Observable.Return(new AxisConfiguration(this)));
        }
    
        public System.IObservable<AxisConfiguration> Process<TSource>(System.IObservable<TSource> source)
        {
            return System.Reactive.Linq.Observable.Select(source, _ => new AxisConfiguration(this));
        }
    
        protected virtual bool PrintMembers(System.Text.StringBuilder stringBuilder)
        {
            stringBuilder.Append("axis = " + _axis + ", ");
            stringBuilder.Append("step_acceleration_interval = " + _stepAccelerationInterval + ", ");
            stringBuilder.Append("step_interval = " + _stepInterval + ", ");
            stringBuilder.Append("microstep_resolution = " + _microstepResolution + ", ");
            stringBuilder.Append("maximum_step_interval = " + _maximumStepInterval + ", ");
            stringBuilder.Append("motor_operation_mode = " + _motorOperationMode + ", ");
            stringBuilder.Append("max_limit = " + _maxLimit + ", ");
            stringBuilder.Append("min_limit = " + _minLimit);
            return true;
        }
    
        public override string ToString()
        {
            System.Text.StringBuilder stringBuilder = new System.Text.StringBuilder();
            stringBuilder.Append(GetType().Name);
            stringBuilder.Append(" { ");
            if (PrintMembers(stringBuilder))
            {
                stringBuilder.Append(" ");
            }
            stringBuilder.Append("}");
            return stringBuilder.ToString();
        }
    }


    [System.CodeDom.Compiler.GeneratedCodeAttribute("Bonsai.Sgen", "0.3.0.0 (Newtonsoft.Json v13.0.0.0)")]
    public enum MicrostepResolution
    {
    
        [System.Runtime.Serialization.EnumMemberAttribute(Value="0")]
        _0 = 0,
    
        [System.Runtime.Serialization.EnumMemberAttribute(Value="1")]
        _1 = 1,
    
        [System.Runtime.Serialization.EnumMemberAttribute(Value="2")]
        _2 = 2,
    
        [System.Runtime.Serialization.EnumMemberAttribute(Value="3")]
        _3 = 3,
    }


    [System.CodeDom.Compiler.GeneratedCodeAttribute("Bonsai.Sgen", "0.3.0.0 (Newtonsoft.Json v13.0.0.0)")]
    public enum MotorOperationMode
    {
    
        [System.Runtime.Serialization.EnumMemberAttribute(Value="0")]
        _0 = 0,
    
        [System.Runtime.Serialization.EnumMemberAttribute(Value="1")]
        _1 = 1,
    }


    [System.CodeDom.Compiler.GeneratedCodeAttribute("Bonsai.Sgen", "0.3.0.0 (Newtonsoft.Json v13.0.0.0)")]
    [Bonsai.CombinatorAttribute()]
    [Bonsai.WorkflowElementCategoryAttribute(Bonsai.ElementCategory.Source)]
    public partial class Vector4
    {
    
        private double _x;
    
        private double _y1;
    
        private double _y2;
    
        private double _z;
    
        public Vector4()
        {
        }
    
        protected Vector4(Vector4 other)
        {
            _x = other._x;
            _y1 = other._y1;
            _y2 = other._y2;
            _z = other._z;
        }
    
        [Newtonsoft.Json.JsonPropertyAttribute("x", Required=Newtonsoft.Json.Required.Always)]
        public double X
        {
            get
            {
                return _x;
            }
            set
            {
                _x = value;
            }
        }
    
        [Newtonsoft.Json.JsonPropertyAttribute("y1", Required=Newtonsoft.Json.Required.Always)]
        public double Y1
        {
            get
            {
                return _y1;
            }
            set
            {
                _y1 = value;
            }
        }
    
        [Newtonsoft.Json.JsonPropertyAttribute("y2", Required=Newtonsoft.Json.Required.Always)]
        public double Y2
        {
            get
            {
                return _y2;
            }
            set
            {
                _y2 = value;
            }
        }
    
        [Newtonsoft.Json.JsonPropertyAttribute("z", Required=Newtonsoft.Json.Required.Always)]
        public double Z
        {
            get
            {
                return _z;
            }
            set
            {
                _z = value;
            }
        }
    
        public System.IObservable<Vector4> Process()
        {
            return System.Reactive.Linq.Observable.Defer(() => System.Reactive.Linq.Observable.Return(new Vector4(this)));
        }
    
        public System.IObservable<Vector4> Process<TSource>(System.IObservable<TSource> source)
        {
            return System.Reactive.Linq.Observable.Select(source, _ => new Vector4(this));
        }
    
        protected virtual bool PrintMembers(System.Text.StringBuilder stringBuilder)
        {
            stringBuilder.Append("x = " + _x + ", ");
            stringBuilder.Append("y1 = " + _y1 + ", ");
            stringBuilder.Append("y2 = " + _y2 + ", ");
            stringBuilder.Append("z = " + _z);
            return true;
        }
    
        public override string ToString()
        {
            System.Text.StringBuilder stringBuilder = new System.Text.StringBuilder();
            stringBuilder.Append(GetType().Name);
            stringBuilder.Append(" { ");
            if (PrintMembers(stringBuilder))
            {
                stringBuilder.Append(" ");
            }
            stringBuilder.Append("}");
            return stringBuilder.ToString();
        }
    }


    [System.CodeDom.Compiler.GeneratedCodeAttribute("Bonsai.Sgen", "0.3.0.0 (Newtonsoft.Json v13.0.0.0)")]
    [Bonsai.CombinatorAttribute()]
    [Bonsai.WorkflowElementCategoryAttribute(Bonsai.ElementCategory.Source)]
    public partial class AindManipulatorCalibrationModel
    {
    
        private string _describedBy = "https://raw.githubusercontent.com/AllenNeuralDynamics/Aind.Behavior.Services/main/src/DataSchemas/schemas/aind_manipulator_calibration.json";
    
        private string _schemaVersion = "0.1.0";
    
        private AindManipulatorOperationControl _operationControl = new AindManipulatorOperationControl();
    
        private AindManipulatorCalibration _calibration;
    
        private string _rootPath;
    
        private System.DateTimeOffset _date;
    
        private string _notes = "";
    
        private string _experiment = "Calibration";
    
        private string _experimenter = "Experimenter";
    
        private bool _allowDirty = false;
    
        private string _remoteDataPath;
    
        private int _rngSeed = 0;
    
        private string _commitHash;
    
        public AindManipulatorCalibrationModel()
        {
        }
    
        protected AindManipulatorCalibrationModel(AindManipulatorCalibrationModel other)
        {
            _describedBy = other._describedBy;
            _schemaVersion = other._schemaVersion;
            _operationControl = other._operationControl;
            _calibration = other._calibration;
            _rootPath = other._rootPath;
            _date = other._date;
            _notes = other._notes;
            _experiment = other._experiment;
            _experimenter = other._experimenter;
            _allowDirty = other._allowDirty;
            _remoteDataPath = other._remoteDataPath;
            _rngSeed = other._rngSeed;
            _commitHash = other._commitHash;
        }
    
        [Newtonsoft.Json.JsonPropertyAttribute("describedBy")]
        public string DescribedBy
        {
            get
            {
                return _describedBy;
            }
            set
            {
                _describedBy = value;
            }
        }
    
        [Newtonsoft.Json.JsonPropertyAttribute("schema_version")]
        public string SchemaVersion
        {
            get
            {
                return _schemaVersion;
            }
            set
            {
                _schemaVersion = value;
            }
        }
    
        [System.Xml.Serialization.XmlIgnoreAttribute()]
        [Newtonsoft.Json.JsonPropertyAttribute("operation_control", Required=Newtonsoft.Json.Required.Always)]
        public AindManipulatorOperationControl OperationControl
        {
            get
            {
                return _operationControl;
            }
            set
            {
                _operationControl = value;
            }
        }
    
        /// <summary>
        /// Calibration data
        /// </summary>
        [System.Xml.Serialization.XmlIgnoreAttribute()]
        [Newtonsoft.Json.JsonPropertyAttribute("calibration")]
        [System.ComponentModel.DescriptionAttribute("Calibration data")]
        public AindManipulatorCalibration Calibration
        {
            get
            {
                return _calibration;
            }
            set
            {
                _calibration = value;
            }
        }
    
        /// <summary>
        /// Root path of the experiment
        /// </summary>
        [Newtonsoft.Json.JsonPropertyAttribute("rootPath", Required=Newtonsoft.Json.Required.Always)]
        [System.ComponentModel.DescriptionAttribute("Root path of the experiment")]
        public string RootPath
        {
            get
            {
                return _rootPath;
            }
            set
            {
                _rootPath = value;
            }
        }
    
        [System.Xml.Serialization.XmlIgnoreAttribute()]
        [Newtonsoft.Json.JsonPropertyAttribute("date")]
        public System.DateTimeOffset Date
        {
            get
            {
                return _date;
            }
            set
            {
                _date = value;
            }
        }
    
        [Newtonsoft.Json.JsonPropertyAttribute("notes")]
        public string Notes
        {
            get
            {
                return _notes;
            }
            set
            {
                _notes = value;
            }
        }
    
        /// <summary>
        /// Name of the experiment
        /// </summary>
        [Newtonsoft.Json.JsonPropertyAttribute("experiment")]
        [System.ComponentModel.DescriptionAttribute("Name of the experiment")]
        public string Experiment
        {
            get
            {
                return _experiment;
            }
            set
            {
                _experiment = value;
            }
        }
    
        /// <summary>
        /// Name of the subject
        /// </summary>
        [Newtonsoft.Json.JsonPropertyAttribute("experimenter")]
        [System.ComponentModel.DescriptionAttribute("Name of the subject")]
        public string Experimenter
        {
            get
            {
                return _experimenter;
            }
            set
            {
                _experimenter = value;
            }
        }
    
        /// <summary>
        /// Allow code to run from dirty repository
        /// </summary>
        [Newtonsoft.Json.JsonPropertyAttribute("allowDirty")]
        [System.ComponentModel.DescriptionAttribute("Allow code to run from dirty repository")]
        public bool AllowDirty
        {
            get
            {
                return _allowDirty;
            }
            set
            {
                _allowDirty = value;
            }
        }
    
        /// <summary>
        /// Path to remote data. If null, no attempt to copy data will be made
        /// </summary>
        [Newtonsoft.Json.JsonPropertyAttribute("remoteDataPath")]
        [System.ComponentModel.DescriptionAttribute("Path to remote data. If null, no attempt to copy data will be made")]
        public string RemoteDataPath
        {
            get
            {
                return _remoteDataPath;
            }
            set
            {
                _remoteDataPath = value;
            }
        }
    
        /// <summary>
        /// Seed of the random number generator. If 0 it will be randomized.
        /// </summary>
        [Newtonsoft.Json.JsonPropertyAttribute("rngSeed")]
        [System.ComponentModel.DescriptionAttribute("Seed of the random number generator. If 0 it will be randomized.")]
        public int RngSeed
        {
            get
            {
                return _rngSeed;
            }
            set
            {
                _rngSeed = value;
            }
        }
    
        /// <summary>
        /// Commit hash of the repository
        /// </summary>
        [Newtonsoft.Json.JsonPropertyAttribute("commitHash")]
        [System.ComponentModel.DescriptionAttribute("Commit hash of the repository")]
        public string CommitHash
        {
            get
            {
                return _commitHash;
            }
            set
            {
                _commitHash = value;
            }
        }
    
        public System.IObservable<AindManipulatorCalibrationModel> Process()
        {
            return System.Reactive.Linq.Observable.Defer(() => System.Reactive.Linq.Observable.Return(new AindManipulatorCalibrationModel(this)));
        }
    
        public System.IObservable<AindManipulatorCalibrationModel> Process<TSource>(System.IObservable<TSource> source)
        {
            return System.Reactive.Linq.Observable.Select(source, _ => new AindManipulatorCalibrationModel(this));
        }
    
        protected virtual bool PrintMembers(System.Text.StringBuilder stringBuilder)
        {
            stringBuilder.Append("describedBy = " + _describedBy + ", ");
            stringBuilder.Append("schema_version = " + _schemaVersion + ", ");
            stringBuilder.Append("operation_control = " + _operationControl + ", ");
            stringBuilder.Append("calibration = " + _calibration + ", ");
            stringBuilder.Append("rootPath = " + _rootPath + ", ");
            stringBuilder.Append("date = " + _date + ", ");
            stringBuilder.Append("notes = " + _notes + ", ");
            stringBuilder.Append("experiment = " + _experiment + ", ");
            stringBuilder.Append("experimenter = " + _experimenter + ", ");
            stringBuilder.Append("allowDirty = " + _allowDirty + ", ");
            stringBuilder.Append("remoteDataPath = " + _remoteDataPath + ", ");
            stringBuilder.Append("rngSeed = " + _rngSeed + ", ");
            stringBuilder.Append("commitHash = " + _commitHash);
            return true;
        }
    
        public override string ToString()
        {
            System.Text.StringBuilder stringBuilder = new System.Text.StringBuilder();
            stringBuilder.Append(GetType().Name);
            stringBuilder.Append(" { ");
            if (PrintMembers(stringBuilder))
            {
                stringBuilder.Append(" ");
            }
            stringBuilder.Append("}");
            return stringBuilder.ToString();
        }
    }


    /// <summary>
    /// Serializes a sequence of data model objects into JSON strings.
    /// </summary>
    [System.CodeDom.Compiler.GeneratedCodeAttribute("Bonsai.Sgen", "0.3.0.0 (Newtonsoft.Json v13.0.0.0)")]
    [System.ComponentModel.DescriptionAttribute("Serializes a sequence of data model objects into JSON strings.")]
    [Bonsai.CombinatorAttribute()]
    [Bonsai.WorkflowElementCategoryAttribute(Bonsai.ElementCategory.Transform)]
    public partial class SerializeToJson
    {
    
        private System.IObservable<string> Process<T>(System.IObservable<T> source)
        {
            return System.Reactive.Linq.Observable.Select(source, value => Newtonsoft.Json.JsonConvert.SerializeObject(value));
        }

        public System.IObservable<string> Process(System.IObservable<AindManipulatorCalibration> source)
        {
            return Process<AindManipulatorCalibration>(source);
        }

        public System.IObservable<string> Process(System.IObservable<AindManipulatorCalibrationInput> source)
        {
            return Process<AindManipulatorCalibrationInput>(source);
        }

        public System.IObservable<string> Process(System.IObservable<AindManipulatorCalibrationOutput> source)
        {
            return Process<AindManipulatorCalibrationOutput>(source);
        }

        public System.IObservable<string> Process(System.IObservable<AindManipulatorOperationControl> source)
        {
            return Process<AindManipulatorOperationControl>(source);
        }

        public System.IObservable<string> Process(System.IObservable<AxisConfiguration> source)
        {
            return Process<AxisConfiguration>(source);
        }

        public System.IObservable<string> Process(System.IObservable<Vector4> source)
        {
            return Process<Vector4>(source);
        }

        public System.IObservable<string> Process(System.IObservable<AindManipulatorCalibrationModel> source)
        {
            return Process<AindManipulatorCalibrationModel>(source);
        }
    }


    /// <summary>
    /// Deserializes a sequence of JSON strings into data model objects.
    /// </summary>
    [System.CodeDom.Compiler.GeneratedCodeAttribute("Bonsai.Sgen", "0.3.0.0 (Newtonsoft.Json v13.0.0.0)")]
    [System.ComponentModel.DescriptionAttribute("Deserializes a sequence of JSON strings into data model objects.")]
    [System.ComponentModel.DefaultPropertyAttribute("Type")]
    [Bonsai.WorkflowElementCategoryAttribute(Bonsai.ElementCategory.Transform)]
    [System.Xml.Serialization.XmlIncludeAttribute(typeof(Bonsai.Expressions.TypeMapping<AindManipulatorCalibration>))]
    [System.Xml.Serialization.XmlIncludeAttribute(typeof(Bonsai.Expressions.TypeMapping<AindManipulatorCalibrationInput>))]
    [System.Xml.Serialization.XmlIncludeAttribute(typeof(Bonsai.Expressions.TypeMapping<AindManipulatorCalibrationOutput>))]
    [System.Xml.Serialization.XmlIncludeAttribute(typeof(Bonsai.Expressions.TypeMapping<AindManipulatorOperationControl>))]
    [System.Xml.Serialization.XmlIncludeAttribute(typeof(Bonsai.Expressions.TypeMapping<AxisConfiguration>))]
    [System.Xml.Serialization.XmlIncludeAttribute(typeof(Bonsai.Expressions.TypeMapping<Vector4>))]
    [System.Xml.Serialization.XmlIncludeAttribute(typeof(Bonsai.Expressions.TypeMapping<AindManipulatorCalibrationModel>))]
    public partial class DeserializeFromJson : Bonsai.Expressions.SingleArgumentExpressionBuilder
    {
    
        public DeserializeFromJson()
        {
            Type = new Bonsai.Expressions.TypeMapping<AindManipulatorCalibrationModel>();
        }

        public Bonsai.Expressions.TypeMapping Type { get; set; }

        public override System.Linq.Expressions.Expression Build(System.Collections.Generic.IEnumerable<System.Linq.Expressions.Expression> arguments)
        {
            var typeMapping = (Bonsai.Expressions.TypeMapping)Type;
            var returnType = typeMapping.GetType().GetGenericArguments()[0];
            return System.Linq.Expressions.Expression.Call(
                typeof(DeserializeFromJson),
                "Process",
                new System.Type[] { returnType },
                System.Linq.Enumerable.Single(arguments));
        }

        private static System.IObservable<T> Process<T>(System.IObservable<string> source)
        {
            return System.Reactive.Linq.Observable.Select(source, value => Newtonsoft.Json.JsonConvert.DeserializeObject<T>(value));
        }
    }
}