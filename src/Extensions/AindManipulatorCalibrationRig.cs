//----------------------
// <auto-generated>
//     Generated using the NJsonSchema v10.9.0.0 (Newtonsoft.Json v13.0.0.0) (http://NJsonSchema.org)
// </auto-generated>
//----------------------


namespace AindBehaviorServices.AindManipulatorCalibrationRig
{
    #pragma warning disable // Disable all warnings

    /// <summary>
    /// Aind manipulator calibration class
    /// </summary>
    [System.CodeDom.Compiler.GeneratedCodeAttribute("Bonsai.Sgen", "0.3.0.0 (Newtonsoft.Json v13.0.0.0)")]
    [System.ComponentModel.DescriptionAttribute("Aind manipulator calibration class")]
    [Bonsai.CombinatorAttribute()]
    [Bonsai.WorkflowElementCategoryAttribute(Bonsai.ElementCategory.Source)]
    public partial class AindManipulatorCalibration
    {
    
        private string _deviceName = "AindManipulator";
    
        private AindManipulatorCalibrationInput _input = new AindManipulatorCalibrationInput();
    
        private AindManipulatorCalibrationOutput _output = new AindManipulatorCalibrationOutput();
    
        private System.DateTimeOffset? _date;
    
        private string _description = "Calibration of the load cells system";
    
        private string _notes;
    
        public AindManipulatorCalibration()
        {
        }
    
        protected AindManipulatorCalibration(AindManipulatorCalibration other)
        {
            _deviceName = other._deviceName;
            _input = other._input;
            _output = other._output;
            _date = other._date;
            _description = other._description;
            _notes = other._notes;
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
    
        [System.Xml.Serialization.XmlIgnoreAttribute()]
        [Newtonsoft.Json.JsonPropertyAttribute("date")]
        public System.DateTimeOffset? Date
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
            stringBuilder.Append("device_name = " + _deviceName + ", ");
            stringBuilder.Append("input = " + _input + ", ");
            stringBuilder.Append("output = " + _output + ", ");
            stringBuilder.Append("date = " + _date + ", ");
            stringBuilder.Append("description = " + _description + ", ");
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
    
        private ManipulatorPosition _fullStepToMm;
    
        private System.Collections.Generic.List<AxisConfiguration> _axisConfiguration = new System.Collections.Generic.List<AxisConfiguration>();
    
        private System.Collections.Generic.List<Axis> _homingOrder = new System.Collections.Generic.List<Axis>();
    
        private ManipulatorPosition _initialPosition;
    
        public AindManipulatorCalibrationInput()
        {
        }
    
        protected AindManipulatorCalibrationInput(AindManipulatorCalibrationInput other)
        {
            _fullStepToMm = other._fullStepToMm;
            _axisConfiguration = other._axisConfiguration;
            _homingOrder = other._homingOrder;
            _initialPosition = other._initialPosition;
        }
    
        [System.Xml.Serialization.XmlIgnoreAttribute()]
        [Newtonsoft.Json.JsonPropertyAttribute("full_step_to_mm")]
        public ManipulatorPosition FullStepToMm
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
    
        [System.Xml.Serialization.XmlIgnoreAttribute()]
        [Newtonsoft.Json.JsonPropertyAttribute("axis_configuration")]
        public System.Collections.Generic.List<AxisConfiguration> AxisConfiguration
        {
            get
            {
                return _axisConfiguration;
            }
            set
            {
                _axisConfiguration = value;
            }
        }
    
        [System.Xml.Serialization.XmlIgnoreAttribute()]
        [Newtonsoft.Json.JsonPropertyAttribute("homing_order")]
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
        [Newtonsoft.Json.JsonPropertyAttribute("initial_position")]
        public ManipulatorPosition InitialPosition
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
            stringBuilder.Append("full_step_to_mm = " + _fullStepToMm + ", ");
            stringBuilder.Append("axis_configuration = " + _axisConfiguration + ", ");
            stringBuilder.Append("homing_order = " + _homingOrder + ", ");
            stringBuilder.Append("initial_position = " + _initialPosition);
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
    public partial class AindManipulatorDevice
    {
    
        private string _deviceType = "stepperdriver";
    
        private BaseModel _additionalSettings;
    
        private AindManipulatorCalibration _calibration;
    
        private int _whoAmI = 1130;
    
        private string _serialNumber;
    
        private string _portName;
    
        public AindManipulatorDevice()
        {
        }
    
        protected AindManipulatorDevice(AindManipulatorDevice other)
        {
            _deviceType = other._deviceType;
            _additionalSettings = other._additionalSettings;
            _calibration = other._calibration;
            _whoAmI = other._whoAmI;
            _serialNumber = other._serialNumber;
            _portName = other._portName;
        }
    
        [Newtonsoft.Json.JsonPropertyAttribute("device_type")]
        public string DeviceType
        {
            get
            {
                return _deviceType;
            }
            set
            {
                _deviceType = value;
            }
        }
    
        /// <summary>
        /// Additional settings
        /// </summary>
        [System.Xml.Serialization.XmlIgnoreAttribute()]
        [Newtonsoft.Json.JsonPropertyAttribute("additional_settings")]
        [System.ComponentModel.DescriptionAttribute("Additional settings")]
        public BaseModel AdditionalSettings
        {
            get
            {
                return _additionalSettings;
            }
            set
            {
                _additionalSettings = value;
            }
        }
    
        [System.Xml.Serialization.XmlIgnoreAttribute()]
        [Newtonsoft.Json.JsonPropertyAttribute("calibration")]
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
    
        [Newtonsoft.Json.JsonPropertyAttribute("who_am_i")]
        public int WhoAmI
        {
            get
            {
                return _whoAmI;
            }
            set
            {
                _whoAmI = value;
            }
        }
    
        /// <summary>
        /// Device serial number
        /// </summary>
        [Newtonsoft.Json.JsonPropertyAttribute("serial_number")]
        [System.ComponentModel.DescriptionAttribute("Device serial number")]
        public string SerialNumber
        {
            get
            {
                return _serialNumber;
            }
            set
            {
                _serialNumber = value;
            }
        }
    
        /// <summary>
        /// Device port name
        /// </summary>
        [Newtonsoft.Json.JsonPropertyAttribute("port_name", Required=Newtonsoft.Json.Required.Always)]
        [System.ComponentModel.DescriptionAttribute("Device port name")]
        public string PortName
        {
            get
            {
                return _portName;
            }
            set
            {
                _portName = value;
            }
        }
    
        public System.IObservable<AindManipulatorDevice> Process()
        {
            return System.Reactive.Linq.Observable.Defer(() => System.Reactive.Linq.Observable.Return(new AindManipulatorDevice(this)));
        }
    
        public System.IObservable<AindManipulatorDevice> Process<TSource>(System.IObservable<TSource> source)
        {
            return System.Reactive.Linq.Observable.Select(source, _ => new AindManipulatorDevice(this));
        }
    
        protected virtual bool PrintMembers(System.Text.StringBuilder stringBuilder)
        {
            stringBuilder.Append("device_type = " + _deviceType + ", ");
            stringBuilder.Append("additional_settings = " + _additionalSettings + ", ");
            stringBuilder.Append("calibration = " + _calibration + ", ");
            stringBuilder.Append("who_am_i = " + _whoAmI + ", ");
            stringBuilder.Append("serial_number = " + _serialNumber + ", ");
            stringBuilder.Append("port_name = " + _portName);
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
        None = 0,
    
        [System.Runtime.Serialization.EnumMemberAttribute(Value="1")]
        X = 1,
    
        [System.Runtime.Serialization.EnumMemberAttribute(Value="2")]
        Y1 = 2,
    
        [System.Runtime.Serialization.EnumMemberAttribute(Value="3")]
        Y2 = 3,
    
        [System.Runtime.Serialization.EnumMemberAttribute(Value="4")]
        Z = 4,
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
    
        private MicrostepResolution _microstepResolution = AindBehaviorServices.AindManipulatorCalibrationRig.MicrostepResolution.Microstep8;
    
        private int _maximumStepInterval = 2000;
    
        private MotorOperationMode _motorOperationMode = AindBehaviorServices.AindManipulatorCalibrationRig.MotorOperationMode.Quiet;
    
        private double _maxLimit = 25D;
    
        private double _minLimit = -0.01D;
    
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
        public double MaxLimit
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
        public double MinLimit
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
    [Bonsai.CombinatorAttribute()]
    [Bonsai.WorkflowElementCategoryAttribute(Bonsai.ElementCategory.Source)]
    public partial class BaseModel
    {
    
        public BaseModel()
        {
        }
    
        protected BaseModel(BaseModel other)
        {
        }
    
        public System.IObservable<BaseModel> Process()
        {
            return System.Reactive.Linq.Observable.Defer(() => System.Reactive.Linq.Observable.Return(new BaseModel(this)));
        }
    
        public System.IObservable<BaseModel> Process<TSource>(System.IObservable<TSource> source)
        {
            return System.Reactive.Linq.Observable.Select(source, _ => new BaseModel(this));
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
    public partial class ManipulatorPosition
    {
    
        private double _x;
    
        private double _y1;
    
        private double _y2;
    
        private double _z;
    
        public ManipulatorPosition()
        {
        }
    
        protected ManipulatorPosition(ManipulatorPosition other)
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
    
        public System.IObservable<ManipulatorPosition> Process()
        {
            return System.Reactive.Linq.Observable.Defer(() => System.Reactive.Linq.Observable.Return(new ManipulatorPosition(this)));
        }
    
        public System.IObservable<ManipulatorPosition> Process<TSource>(System.IObservable<TSource> source)
        {
            return System.Reactive.Linq.Observable.Select(source, _ => new ManipulatorPosition(this));
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
    public enum MicrostepResolution
    {
    
        [System.Runtime.Serialization.EnumMemberAttribute(Value="0")]
        Microstep8 = 0,
    
        [System.Runtime.Serialization.EnumMemberAttribute(Value="1")]
        Microstep16 = 1,
    
        [System.Runtime.Serialization.EnumMemberAttribute(Value="2")]
        Microstep32 = 2,
    
        [System.Runtime.Serialization.EnumMemberAttribute(Value="3")]
        Microstep64 = 3,
    }


    [System.CodeDom.Compiler.GeneratedCodeAttribute("Bonsai.Sgen", "0.3.0.0 (Newtonsoft.Json v13.0.0.0)")]
    public enum MotorOperationMode
    {
    
        [System.Runtime.Serialization.EnumMemberAttribute(Value="0")]
        Quiet = 0,
    
        [System.Runtime.Serialization.EnumMemberAttribute(Value="1")]
        Dynamic = 1,
    }


    [System.CodeDom.Compiler.GeneratedCodeAttribute("Bonsai.Sgen", "0.3.0.0 (Newtonsoft.Json v13.0.0.0)")]
    [Bonsai.CombinatorAttribute()]
    [Bonsai.WorkflowElementCategoryAttribute(Bonsai.ElementCategory.Source)]
    public partial class CalibrationRig
    {
    
        private string _aindBehaviorServicesPkgVersion = "0.8.8";
    
        private string _version = "0.1.0";
    
        private string _computerName;
    
        private string _rigName;
    
        private AindManipulatorDevice _manipulator;
    
        public CalibrationRig()
        {
        }
    
        protected CalibrationRig(CalibrationRig other)
        {
            _aindBehaviorServicesPkgVersion = other._aindBehaviorServicesPkgVersion;
            _version = other._version;
            _computerName = other._computerName;
            _rigName = other._rigName;
            _manipulator = other._manipulator;
        }
    
        [Newtonsoft.Json.JsonPropertyAttribute("aind_behavior_services_pkg_version")]
        public string AindBehaviorServicesPkgVersion
        {
            get
            {
                return _aindBehaviorServicesPkgVersion;
            }
            set
            {
                _aindBehaviorServicesPkgVersion = value;
            }
        }
    
        [Newtonsoft.Json.JsonPropertyAttribute("version")]
        public string Version
        {
            get
            {
                return _version;
            }
            set
            {
                _version = value;
            }
        }
    
        /// <summary>
        /// Computer name
        /// </summary>
        [Newtonsoft.Json.JsonPropertyAttribute("computer_name")]
        [System.ComponentModel.DescriptionAttribute("Computer name")]
        public string ComputerName
        {
            get
            {
                return _computerName;
            }
            set
            {
                _computerName = value;
            }
        }
    
        /// <summary>
        /// Rig name
        /// </summary>
        [Newtonsoft.Json.JsonPropertyAttribute("rig_name", Required=Newtonsoft.Json.Required.Always)]
        [System.ComponentModel.DescriptionAttribute("Rig name")]
        public string RigName
        {
            get
            {
                return _rigName;
            }
            set
            {
                _rigName = value;
            }
        }
    
        [System.Xml.Serialization.XmlIgnoreAttribute()]
        [Newtonsoft.Json.JsonPropertyAttribute("manipulator")]
        public AindManipulatorDevice Manipulator
        {
            get
            {
                return _manipulator;
            }
            set
            {
                _manipulator = value;
            }
        }
    
        public System.IObservable<CalibrationRig> Process()
        {
            return System.Reactive.Linq.Observable.Defer(() => System.Reactive.Linq.Observable.Return(new CalibrationRig(this)));
        }
    
        public System.IObservable<CalibrationRig> Process<TSource>(System.IObservable<TSource> source)
        {
            return System.Reactive.Linq.Observable.Select(source, _ => new CalibrationRig(this));
        }
    
        protected virtual bool PrintMembers(System.Text.StringBuilder stringBuilder)
        {
            stringBuilder.Append("aind_behavior_services_pkg_version = " + _aindBehaviorServicesPkgVersion + ", ");
            stringBuilder.Append("version = " + _version + ", ");
            stringBuilder.Append("computer_name = " + _computerName + ", ");
            stringBuilder.Append("rig_name = " + _rigName + ", ");
            stringBuilder.Append("manipulator = " + _manipulator);
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

        public System.IObservable<string> Process(System.IObservable<AindManipulatorDevice> source)
        {
            return Process<AindManipulatorDevice>(source);
        }

        public System.IObservable<string> Process(System.IObservable<AxisConfiguration> source)
        {
            return Process<AxisConfiguration>(source);
        }

        public System.IObservable<string> Process(System.IObservable<BaseModel> source)
        {
            return Process<BaseModel>(source);
        }

        public System.IObservable<string> Process(System.IObservable<ManipulatorPosition> source)
        {
            return Process<ManipulatorPosition>(source);
        }

        public System.IObservable<string> Process(System.IObservable<CalibrationRig> source)
        {
            return Process<CalibrationRig>(source);
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
    [System.Xml.Serialization.XmlIncludeAttribute(typeof(Bonsai.Expressions.TypeMapping<AindManipulatorDevice>))]
    [System.Xml.Serialization.XmlIncludeAttribute(typeof(Bonsai.Expressions.TypeMapping<AxisConfiguration>))]
    [System.Xml.Serialization.XmlIncludeAttribute(typeof(Bonsai.Expressions.TypeMapping<BaseModel>))]
    [System.Xml.Serialization.XmlIncludeAttribute(typeof(Bonsai.Expressions.TypeMapping<ManipulatorPosition>))]
    [System.Xml.Serialization.XmlIncludeAttribute(typeof(Bonsai.Expressions.TypeMapping<CalibrationRig>))]
    public partial class DeserializeFromJson : Bonsai.Expressions.SingleArgumentExpressionBuilder
    {
    
        public DeserializeFromJson()
        {
            Type = new Bonsai.Expressions.TypeMapping<CalibrationRig>();
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