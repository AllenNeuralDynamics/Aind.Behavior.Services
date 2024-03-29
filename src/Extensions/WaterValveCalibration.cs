//----------------------
// <auto-generated>
//     Generated using the NJsonSchema v10.9.0.0 (Newtonsoft.Json v13.0.0.0) (http://NJsonSchema.org)
// </auto-generated>
//----------------------


namespace AindBehaviorRigCalibration.WaterValveCalibration
{
    #pragma warning disable // Disable all warnings

    /// <summary>
    /// Input for water valve calibration class
    /// </summary>
    [System.CodeDom.Compiler.GeneratedCodeAttribute("Bonsai.Sgen", "0.3.0.0 (Newtonsoft.Json v13.0.0.0)")]
    [System.ComponentModel.DescriptionAttribute("Input for water valve calibration class")]
    [Bonsai.CombinatorAttribute()]
    [Bonsai.WorkflowElementCategoryAttribute(Bonsai.ElementCategory.Source)]
    public partial class Measurement
    {
    
        private double _valveOpenInterval;
    
        private double _valveOpenTime;
    
        private System.Collections.Generic.List<double> _waterWeight = new System.Collections.Generic.List<double>();
    
        private int _repeatCount;
    
        public Measurement()
        {
        }
    
        protected Measurement(Measurement other)
        {
            _valveOpenInterval = other._valveOpenInterval;
            _valveOpenTime = other._valveOpenTime;
            _waterWeight = other._waterWeight;
            _repeatCount = other._repeatCount;
        }
    
        /// <summary>
        /// Time between two consecutive valve openings (s)
        /// </summary>
        [Newtonsoft.Json.JsonPropertyAttribute("valve_open_interval", Required=Newtonsoft.Json.Required.Always)]
        [System.ComponentModel.DescriptionAttribute("Time between two consecutive valve openings (s)")]
        public double ValveOpenInterval
        {
            get
            {
                return _valveOpenInterval;
            }
            set
            {
                _valveOpenInterval = value;
            }
        }
    
        /// <summary>
        /// Valve open interval (s)
        /// </summary>
        [Newtonsoft.Json.JsonPropertyAttribute("valve_open_time", Required=Newtonsoft.Json.Required.Always)]
        [System.ComponentModel.DescriptionAttribute("Valve open interval (s)")]
        public double ValveOpenTime
        {
            get
            {
                return _valveOpenTime;
            }
            set
            {
                _valveOpenTime = value;
            }
        }
    
        /// <summary>
        /// Weight of water delivered (g)
        /// </summary>
        [System.Xml.Serialization.XmlIgnoreAttribute()]
        [Newtonsoft.Json.JsonPropertyAttribute("water_weight", Required=Newtonsoft.Json.Required.Always)]
        [System.ComponentModel.DescriptionAttribute("Weight of water delivered (g)")]
        public System.Collections.Generic.List<double> WaterWeight
        {
            get
            {
                return _waterWeight;
            }
            set
            {
                _waterWeight = value;
            }
        }
    
        /// <summary>
        /// Number of times the valve opened.
        /// </summary>
        [Newtonsoft.Json.JsonPropertyAttribute("repeat_count", Required=Newtonsoft.Json.Required.Always)]
        [System.ComponentModel.DescriptionAttribute("Number of times the valve opened.")]
        public int RepeatCount
        {
            get
            {
                return _repeatCount;
            }
            set
            {
                _repeatCount = value;
            }
        }
    
        public System.IObservable<Measurement> Process()
        {
            return System.Reactive.Linq.Observable.Defer(() => System.Reactive.Linq.Observable.Return(new Measurement(this)));
        }
    
        public System.IObservable<Measurement> Process<TSource>(System.IObservable<TSource> source)
        {
            return System.Reactive.Linq.Observable.Select(source, _ => new Measurement(this));
        }
    
        protected virtual bool PrintMembers(System.Text.StringBuilder stringBuilder)
        {
            stringBuilder.Append("valve_open_interval = " + _valveOpenInterval + ", ");
            stringBuilder.Append("valve_open_time = " + _valveOpenTime + ", ");
            stringBuilder.Append("water_weight = " + _waterWeight + ", ");
            stringBuilder.Append("repeat_count = " + _repeatCount);
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
    /// Water valve calibration class
    /// </summary>
    [System.CodeDom.Compiler.GeneratedCodeAttribute("Bonsai.Sgen", "0.3.0.0 (Newtonsoft.Json v13.0.0.0)")]
    [System.ComponentModel.DescriptionAttribute("Water valve calibration class")]
    [Bonsai.CombinatorAttribute()]
    [Bonsai.WorkflowElementCategoryAttribute(Bonsai.ElementCategory.Source)]
    public partial class WaterValveCalibration
    {
    
        private System.DateTimeOffset _calibrationDate;
    
        private string _deviceName = "WaterValve";
    
        private string _description = "Calibration of the water valve delivery system";
    
        private WaterValveCalibrationInput _input = new WaterValveCalibrationInput();
    
        private WaterValveCalibrationOutput _output = new WaterValveCalibrationOutput();
    
        private string _notes;
    
        public WaterValveCalibration()
        {
        }
    
        protected WaterValveCalibration(WaterValveCalibration other)
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
        public WaterValveCalibrationInput Input
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
        public WaterValveCalibrationOutput Output
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
    
        public System.IObservable<WaterValveCalibration> Process()
        {
            return System.Reactive.Linq.Observable.Defer(() => System.Reactive.Linq.Observable.Return(new WaterValveCalibration(this)));
        }
    
        public System.IObservable<WaterValveCalibration> Process<TSource>(System.IObservable<TSource> source)
        {
            return System.Reactive.Linq.Observable.Select(source, _ => new WaterValveCalibration(this));
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
    public partial class WaterValveCalibrationInput
    {
    
        private System.Collections.Generic.List<Measurement> _measurements = new System.Collections.Generic.List<Measurement>();
    
        public WaterValveCalibrationInput()
        {
        }
    
        protected WaterValveCalibrationInput(WaterValveCalibrationInput other)
        {
            _measurements = other._measurements;
        }
    
        /// <summary>
        /// List of measurements
        /// </summary>
        [System.Xml.Serialization.XmlIgnoreAttribute()]
        [Newtonsoft.Json.JsonPropertyAttribute("measurements")]
        [System.ComponentModel.DescriptionAttribute("List of measurements")]
        public System.Collections.Generic.List<Measurement> Measurements
        {
            get
            {
                return _measurements;
            }
            set
            {
                _measurements = value;
            }
        }
    
        public System.IObservable<WaterValveCalibrationInput> Process()
        {
            return System.Reactive.Linq.Observable.Defer(() => System.Reactive.Linq.Observable.Return(new WaterValveCalibrationInput(this)));
        }
    
        public System.IObservable<WaterValveCalibrationInput> Process<TSource>(System.IObservable<TSource> source)
        {
            return System.Reactive.Linq.Observable.Select(source, _ => new WaterValveCalibrationInput(this));
        }
    
        protected virtual bool PrintMembers(System.Text.StringBuilder stringBuilder)
        {
            stringBuilder.Append("measurements = " + _measurements);
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
    /// Output for water valve calibration class
    /// </summary>
    [System.CodeDom.Compiler.GeneratedCodeAttribute("Bonsai.Sgen", "0.3.0.0 (Newtonsoft.Json v13.0.0.0)")]
    [System.ComponentModel.DescriptionAttribute("Output for water valve calibration class")]
    [Bonsai.CombinatorAttribute()]
    [Bonsai.WorkflowElementCategoryAttribute(Bonsai.ElementCategory.Source)]
    public partial class WaterValveCalibrationOutput
    {
    
        private System.Collections.Generic.IDictionary<string, double> _intervalAverage;
    
        private double _slope;
    
        private double _offset;
    
        private double? _r2;
    
        private System.Collections.Generic.List<double> _validDomain;
    
        public WaterValveCalibrationOutput()
        {
        }
    
        protected WaterValveCalibrationOutput(WaterValveCalibrationOutput other)
        {
            _intervalAverage = other._intervalAverage;
            _slope = other._slope;
            _offset = other._offset;
            _r2 = other._r2;
            _validDomain = other._validDomain;
        }
    
        /// <summary>
        /// Dictionary keyed by measured valve interval and corresponding average single event volume.
        /// </summary>
        [System.Xml.Serialization.XmlIgnoreAttribute()]
        [Newtonsoft.Json.JsonPropertyAttribute("interval_average")]
        [System.ComponentModel.DescriptionAttribute("Dictionary keyed by measured valve interval and corresponding average single even" +
            "t volume.")]
        public System.Collections.Generic.IDictionary<string, double> IntervalAverage
        {
            get
            {
                return _intervalAverage;
            }
            set
            {
                _intervalAverage = value;
            }
        }
    
        /// <summary>
        /// Slope of the linear regression : Volume(g) = Slope(g/s) * time(s) + offset(g)
        /// </summary>
        [Newtonsoft.Json.JsonPropertyAttribute("slope", Required=Newtonsoft.Json.Required.Always)]
        [System.ComponentModel.DescriptionAttribute("Slope of the linear regression : Volume(g) = Slope(g/s) * time(s) + offset(g)")]
        public double Slope
        {
            get
            {
                return _slope;
            }
            set
            {
                _slope = value;
            }
        }
    
        /// <summary>
        /// Offset of the linear regression : Volume(g) = Slope(g/s) * time(s) + offset(g)
        /// </summary>
        [Newtonsoft.Json.JsonPropertyAttribute("offset", Required=Newtonsoft.Json.Required.Always)]
        [System.ComponentModel.DescriptionAttribute("Offset of the linear regression : Volume(g) = Slope(g/s) * time(s) + offset(g)")]
        public double Offset
        {
            get
            {
                return _offset;
            }
            set
            {
                _offset = value;
            }
        }
    
        /// <summary>
        /// R2 metric from the linear model.
        /// </summary>
        [System.Xml.Serialization.XmlIgnoreAttribute()]
        [Newtonsoft.Json.JsonPropertyAttribute("r2")]
        [System.ComponentModel.DescriptionAttribute("R2 metric from the linear model.")]
        public double? R2
        {
            get
            {
                return _r2;
            }
            set
            {
                _r2 = value;
            }
        }
    
        /// <summary>
        /// The optional time-intervals the calibration curve was calculated on.
        /// </summary>
        [System.Xml.Serialization.XmlIgnoreAttribute()]
        [Newtonsoft.Json.JsonPropertyAttribute("valid_domain")]
        [System.ComponentModel.DescriptionAttribute("The optional time-intervals the calibration curve was calculated on.")]
        public System.Collections.Generic.List<double> ValidDomain
        {
            get
            {
                return _validDomain;
            }
            set
            {
                _validDomain = value;
            }
        }
    
        public System.IObservable<WaterValveCalibrationOutput> Process()
        {
            return System.Reactive.Linq.Observable.Defer(() => System.Reactive.Linq.Observable.Return(new WaterValveCalibrationOutput(this)));
        }
    
        public System.IObservable<WaterValveCalibrationOutput> Process<TSource>(System.IObservable<TSource> source)
        {
            return System.Reactive.Linq.Observable.Select(source, _ => new WaterValveCalibrationOutput(this));
        }
    
        protected virtual bool PrintMembers(System.Text.StringBuilder stringBuilder)
        {
            stringBuilder.Append("interval_average = " + _intervalAverage + ", ");
            stringBuilder.Append("slope = " + _slope + ", ");
            stringBuilder.Append("offset = " + _offset + ", ");
            stringBuilder.Append("r2 = " + _r2 + ", ");
            stringBuilder.Append("valid_domain = " + _validDomain);
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
    /// Olfactometer operation control model that is used to run a calibration data acquisition workflow
    /// </summary>
    [System.CodeDom.Compiler.GeneratedCodeAttribute("Bonsai.Sgen", "0.3.0.0 (Newtonsoft.Json v13.0.0.0)")]
    [System.ComponentModel.DescriptionAttribute("Olfactometer operation control model that is used to run a calibration data acqui" +
        "sition workflow")]
    [Bonsai.CombinatorAttribute()]
    [Bonsai.WorkflowElementCategoryAttribute(Bonsai.ElementCategory.Source)]
    public partial class WaterValveOperationControl
    {
    
        private System.Collections.Generic.List<double> _valveOpenTime = new System.Collections.Generic.List<double>();
    
        private double _valveOpenInterval = 0.2D;
    
        private int _repeatCount = 200;
    
        public WaterValveOperationControl()
        {
        }
    
        protected WaterValveOperationControl(WaterValveOperationControl other)
        {
            _valveOpenTime = other._valveOpenTime;
            _valveOpenInterval = other._valveOpenInterval;
            _repeatCount = other._repeatCount;
        }
    
        /// <summary>
        /// An array with the times (s) the valve is open during calibration
        /// </summary>
        [System.Xml.Serialization.XmlIgnoreAttribute()]
        [Newtonsoft.Json.JsonPropertyAttribute("valve_open_time", Required=Newtonsoft.Json.Required.Always)]
        [System.ComponentModel.DescriptionAttribute("An array with the times (s) the valve is open during calibration")]
        public System.Collections.Generic.List<double> ValveOpenTime
        {
            get
            {
                return _valveOpenTime;
            }
            set
            {
                _valveOpenTime = value;
            }
        }
    
        /// <summary>
        /// Time between two consecutive valve openings (s)
        /// </summary>
        [Newtonsoft.Json.JsonPropertyAttribute("valve_open_interval")]
        [System.ComponentModel.DescriptionAttribute("Time between two consecutive valve openings (s)")]
        public double ValveOpenInterval
        {
            get
            {
                return _valveOpenInterval;
            }
            set
            {
                _valveOpenInterval = value;
            }
        }
    
        /// <summary>
        /// Number of times the valve opened per measure valve_open_time entry
        /// </summary>
        [Newtonsoft.Json.JsonPropertyAttribute("repeat_count")]
        [System.ComponentModel.DescriptionAttribute("Number of times the valve opened per measure valve_open_time entry")]
        public int RepeatCount
        {
            get
            {
                return _repeatCount;
            }
            set
            {
                _repeatCount = value;
            }
        }
    
        public System.IObservable<WaterValveOperationControl> Process()
        {
            return System.Reactive.Linq.Observable.Defer(() => System.Reactive.Linq.Observable.Return(new WaterValveOperationControl(this)));
        }
    
        public System.IObservable<WaterValveOperationControl> Process<TSource>(System.IObservable<TSource> source)
        {
            return System.Reactive.Linq.Observable.Select(source, _ => new WaterValveOperationControl(this));
        }
    
        protected virtual bool PrintMembers(System.Text.StringBuilder stringBuilder)
        {
            stringBuilder.Append("valve_open_time = " + _valveOpenTime + ", ");
            stringBuilder.Append("valve_open_interval = " + _valveOpenInterval + ", ");
            stringBuilder.Append("repeat_count = " + _repeatCount);
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
    public partial class WaterValveCalibrationModel
    {
    
        private string _describedBy = "";
    
        private string _schemaVersion = "0.1.0";
    
        private WaterValveOperationControl _operationControl = new WaterValveOperationControl();
    
        private WaterValveCalibration _calibration;
    
        private string _rootPath;
    
        private System.DateTimeOffset _date;
    
        private string _notes = "";
    
        private string _experiment = "Calibration";
    
        private string _experimenter = "Experimenter";
    
        private bool _allowDirty = false;
    
        private string _remoteDataPath;
    
        private int _rngSeed = 0;
    
        private string _commitHash;
    
        public WaterValveCalibrationModel()
        {
        }
    
        protected WaterValveCalibrationModel(WaterValveCalibrationModel other)
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
        public WaterValveOperationControl OperationControl
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
        public WaterValveCalibration Calibration
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
    
        public System.IObservable<WaterValveCalibrationModel> Process()
        {
            return System.Reactive.Linq.Observable.Defer(() => System.Reactive.Linq.Observable.Return(new WaterValveCalibrationModel(this)));
        }
    
        public System.IObservable<WaterValveCalibrationModel> Process<TSource>(System.IObservable<TSource> source)
        {
            return System.Reactive.Linq.Observable.Select(source, _ => new WaterValveCalibrationModel(this));
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

        public System.IObservable<string> Process(System.IObservable<Measurement> source)
        {
            return Process<Measurement>(source);
        }

        public System.IObservable<string> Process(System.IObservable<WaterValveCalibration> source)
        {
            return Process<WaterValveCalibration>(source);
        }

        public System.IObservable<string> Process(System.IObservable<WaterValveCalibrationInput> source)
        {
            return Process<WaterValveCalibrationInput>(source);
        }

        public System.IObservable<string> Process(System.IObservable<WaterValveCalibrationOutput> source)
        {
            return Process<WaterValveCalibrationOutput>(source);
        }

        public System.IObservable<string> Process(System.IObservable<WaterValveOperationControl> source)
        {
            return Process<WaterValveOperationControl>(source);
        }

        public System.IObservable<string> Process(System.IObservable<WaterValveCalibrationModel> source)
        {
            return Process<WaterValveCalibrationModel>(source);
        }
    }


    /// <summary>
    /// Deserializes a sequence of JSON strings into data model objects.
    /// </summary>
    [System.CodeDom.Compiler.GeneratedCodeAttribute("Bonsai.Sgen", "0.3.0.0 (Newtonsoft.Json v13.0.0.0)")]
    [System.ComponentModel.DescriptionAttribute("Deserializes a sequence of JSON strings into data model objects.")]
    [System.ComponentModel.DefaultPropertyAttribute("Type")]
    [Bonsai.WorkflowElementCategoryAttribute(Bonsai.ElementCategory.Transform)]
    [System.Xml.Serialization.XmlIncludeAttribute(typeof(Bonsai.Expressions.TypeMapping<Measurement>))]
    [System.Xml.Serialization.XmlIncludeAttribute(typeof(Bonsai.Expressions.TypeMapping<WaterValveCalibration>))]
    [System.Xml.Serialization.XmlIncludeAttribute(typeof(Bonsai.Expressions.TypeMapping<WaterValveCalibrationInput>))]
    [System.Xml.Serialization.XmlIncludeAttribute(typeof(Bonsai.Expressions.TypeMapping<WaterValveCalibrationOutput>))]
    [System.Xml.Serialization.XmlIncludeAttribute(typeof(Bonsai.Expressions.TypeMapping<WaterValveOperationControl>))]
    [System.Xml.Serialization.XmlIncludeAttribute(typeof(Bonsai.Expressions.TypeMapping<WaterValveCalibrationModel>))]
    public partial class DeserializeFromJson : Bonsai.Expressions.SingleArgumentExpressionBuilder
    {
    
        public DeserializeFromJson()
        {
            Type = new Bonsai.Expressions.TypeMapping<WaterValveCalibrationModel>();
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