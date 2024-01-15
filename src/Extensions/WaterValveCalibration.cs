//----------------------
// <auto-generated>
//     Generated using the NJsonSchema v10.9.0.0 (Newtonsoft.Json v13.0.0.0) (http://NJsonSchema.org)
// </auto-generated>
//----------------------


namespace AindBehaviorRigCalibration.WaterValveCalibration
{
    #pragma warning disable // Disable all warnings

    /// <summary>
    /// Water valve calibration class
    /// </summary>
    [System.CodeDom.Compiler.GeneratedCodeAttribute("Bonsai.Sgen", "0.3.0.0 (Newtonsoft.Json v13.0.0.0, YamlDotNet v13.0.0.0)")]
    [System.ComponentModel.DescriptionAttribute("Water valve calibration class")]
    [Bonsai.CombinatorAttribute()]
    [Bonsai.WorkflowElementCategoryAttribute(Bonsai.ElementCategory.Source)]
    public partial class WaterValveCalibration
    {
    
        private System.DateTimeOffset _calibration_date;
    
        private string _device_name = "WaterValve";
    
        private object _description;
    
        private System.Collections.Generic.List<WaterValveCalibrationInput> _input = new System.Collections.Generic.List<WaterValveCalibrationInput>();
    
        private WaterValveCalibrationOutput _output;
    
        private string _notes;
    
        public WaterValveCalibration()
        {
        }
    
        protected WaterValveCalibration(WaterValveCalibration other)
        {
            _calibration_date = other._calibration_date;
            _device_name = other._device_name;
            _description = other._description;
            _input = other._input;
            _output = other._output;
            _notes = other._notes;
        }
    
        [System.Xml.Serialization.XmlIgnoreAttribute()]
        [Newtonsoft.Json.JsonPropertyAttribute("calibration_date", Required=Newtonsoft.Json.Required.Always)]
        [YamlDotNet.Serialization.YamlMemberAttribute(Alias="calibration_date")]
        public System.DateTimeOffset Calibration_date
        {
            get
            {
                return _calibration_date;
            }
            set
            {
                _calibration_date = value;
            }
        }
    
        /// <summary>
        /// Must match a device name in rig/instrument
        /// </summary>
        [Newtonsoft.Json.JsonPropertyAttribute("device_name")]
        [YamlDotNet.Serialization.YamlMemberAttribute(Alias="device_name")]
        [System.ComponentModel.DescriptionAttribute("Must match a device name in rig/instrument")]
        public string Device_name
        {
            get
            {
                return _device_name;
            }
            set
            {
                _device_name = value;
            }
        }
    
        [System.Xml.Serialization.XmlIgnoreAttribute()]
        [Newtonsoft.Json.JsonPropertyAttribute("description")]
        [YamlDotNet.Serialization.YamlMemberAttribute(Alias="description")]
        public object Description
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
        [Newtonsoft.Json.JsonPropertyAttribute("input")]
        [YamlDotNet.Serialization.YamlMemberAttribute(Alias="input")]
        public System.Collections.Generic.List<WaterValveCalibrationInput> Input
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
        [Newtonsoft.Json.JsonPropertyAttribute("output")]
        [YamlDotNet.Serialization.YamlMemberAttribute(Alias="output")]
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
        [YamlDotNet.Serialization.YamlMemberAttribute(Alias="notes")]
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
            stringBuilder.Append("calibration_date = " + _calibration_date + ", ");
            stringBuilder.Append("device_name = " + _device_name + ", ");
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


    /// <summary>
    /// Input for water valve calibration class
    /// </summary>
    [System.CodeDom.Compiler.GeneratedCodeAttribute("Bonsai.Sgen", "0.3.0.0 (Newtonsoft.Json v13.0.0.0, YamlDotNet v13.0.0.0)")]
    [System.ComponentModel.DescriptionAttribute("Input for water valve calibration class")]
    [Bonsai.CombinatorAttribute()]
    [Bonsai.WorkflowElementCategoryAttribute(Bonsai.ElementCategory.Source)]
    public partial class WaterValveCalibrationInput
    {
    
        private double _valve_open_interval;
    
        private double _valve_open_time;
    
        private System.Collections.Generic.List<double> _water_weight = new System.Collections.Generic.List<double>();
    
        private int _repeat_count;
    
        public WaterValveCalibrationInput()
        {
        }
    
        protected WaterValveCalibrationInput(WaterValveCalibrationInput other)
        {
            _valve_open_interval = other._valve_open_interval;
            _valve_open_time = other._valve_open_time;
            _water_weight = other._water_weight;
            _repeat_count = other._repeat_count;
        }
    
        /// <summary>
        /// Time between two consecutive valve openings (s)
        /// </summary>
        [Newtonsoft.Json.JsonPropertyAttribute("valve_open_interval", Required=Newtonsoft.Json.Required.Always)]
        [YamlDotNet.Serialization.YamlMemberAttribute(Alias="valve_open_interval")]
        [System.ComponentModel.DescriptionAttribute("Time between two consecutive valve openings (s)")]
        public double Valve_open_interval
        {
            get
            {
                return _valve_open_interval;
            }
            set
            {
                _valve_open_interval = value;
            }
        }
    
        /// <summary>
        /// Valve open interval (s)
        /// </summary>
        [Newtonsoft.Json.JsonPropertyAttribute("valve_open_time", Required=Newtonsoft.Json.Required.Always)]
        [YamlDotNet.Serialization.YamlMemberAttribute(Alias="valve_open_time")]
        [System.ComponentModel.DescriptionAttribute("Valve open interval (s)")]
        public double Valve_open_time
        {
            get
            {
                return _valve_open_time;
            }
            set
            {
                _valve_open_time = value;
            }
        }
    
        /// <summary>
        /// Weight of water delivered (g)
        /// </summary>
        [System.Xml.Serialization.XmlIgnoreAttribute()]
        [Newtonsoft.Json.JsonPropertyAttribute("water_weight", Required=Newtonsoft.Json.Required.Always)]
        [YamlDotNet.Serialization.YamlMemberAttribute(Alias="water_weight")]
        [System.ComponentModel.DescriptionAttribute("Weight of water delivered (g)")]
        public System.Collections.Generic.List<double> Water_weight
        {
            get
            {
                return _water_weight;
            }
            set
            {
                _water_weight = value;
            }
        }
    
        /// <summary>
        /// Number of times the valve opened.
        /// </summary>
        [Newtonsoft.Json.JsonPropertyAttribute("repeat_count", Required=Newtonsoft.Json.Required.Always)]
        [YamlDotNet.Serialization.YamlMemberAttribute(Alias="repeat_count")]
        [System.ComponentModel.DescriptionAttribute("Number of times the valve opened.")]
        public int Repeat_count
        {
            get
            {
                return _repeat_count;
            }
            set
            {
                _repeat_count = value;
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
            stringBuilder.Append("valve_open_interval = " + _valve_open_interval + ", ");
            stringBuilder.Append("valve_open_time = " + _valve_open_time + ", ");
            stringBuilder.Append("water_weight = " + _water_weight + ", ");
            stringBuilder.Append("repeat_count = " + _repeat_count);
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
    [System.CodeDom.Compiler.GeneratedCodeAttribute("Bonsai.Sgen", "0.3.0.0 (Newtonsoft.Json v13.0.0.0, YamlDotNet v13.0.0.0)")]
    [System.ComponentModel.DescriptionAttribute("Output for water valve calibration class")]
    [Bonsai.CombinatorAttribute()]
    [Bonsai.WorkflowElementCategoryAttribute(Bonsai.ElementCategory.Source)]
    public partial class WaterValveCalibrationOutput
    {
    
        private System.Collections.Generic.IDictionary<string, double> _interval_average;
    
        private double _slope;
    
        private double _offset;
    
        private double _r2;
    
        private System.Collections.Generic.List<double> _valid_domain;
    
        public WaterValveCalibrationOutput()
        {
        }
    
        protected WaterValveCalibrationOutput(WaterValveCalibrationOutput other)
        {
            _interval_average = other._interval_average;
            _slope = other._slope;
            _offset = other._offset;
            _r2 = other._r2;
            _valid_domain = other._valid_domain;
        }
    
        /// <summary>
        /// Dictionary keyed by measured valve interval and corresponding average single event volume.
        /// </summary>
        [System.Xml.Serialization.XmlIgnoreAttribute()]
        [Newtonsoft.Json.JsonPropertyAttribute("interval_average")]
        [YamlDotNet.Serialization.YamlMemberAttribute(Alias="interval_average")]
        [System.ComponentModel.DescriptionAttribute("Dictionary keyed by measured valve interval and corresponding average single even" +
            "t volume.")]
        public System.Collections.Generic.IDictionary<string, double> Interval_average
        {
            get
            {
                return _interval_average;
            }
            set
            {
                _interval_average = value;
            }
        }
    
        /// <summary>
        /// Slope of the linear regression : Volume(g) = Slope(g/s) * time(s) + offset(g)
        /// </summary>
        [Newtonsoft.Json.JsonPropertyAttribute("slope", Required=Newtonsoft.Json.Required.Always)]
        [YamlDotNet.Serialization.YamlMemberAttribute(Alias="slope")]
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
        [YamlDotNet.Serialization.YamlMemberAttribute(Alias="offset")]
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
        [Newtonsoft.Json.JsonPropertyAttribute("r2", Required=Newtonsoft.Json.Required.Always)]
        [YamlDotNet.Serialization.YamlMemberAttribute(Alias="r2")]
        [System.ComponentModel.DescriptionAttribute("R2 metric from the linear model.")]
        public double R2
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
        [YamlDotNet.Serialization.YamlMemberAttribute(Alias="valid_domain")]
        [System.ComponentModel.DescriptionAttribute("The optional time-intervals the calibration curve was calculated on.")]
        public System.Collections.Generic.List<double> Valid_domain
        {
            get
            {
                return _valid_domain;
            }
            set
            {
                _valid_domain = value;
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
            stringBuilder.Append("interval_average = " + _interval_average + ", ");
            stringBuilder.Append("slope = " + _slope + ", ");
            stringBuilder.Append("offset = " + _offset + ", ");
            stringBuilder.Append("r2 = " + _r2 + ", ");
            stringBuilder.Append("valid_domain = " + _valid_domain);
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
    [System.CodeDom.Compiler.GeneratedCodeAttribute("Bonsai.Sgen", "0.3.0.0 (Newtonsoft.Json v13.0.0.0, YamlDotNet v13.0.0.0)")]
    [System.ComponentModel.DescriptionAttribute("Olfactometer operation control model that is used to run a calibration data acqui" +
        "sition workflow")]
    [Bonsai.CombinatorAttribute()]
    [Bonsai.WorkflowElementCategoryAttribute(Bonsai.ElementCategory.Source)]
    public partial class WaterValveOperationControl
    {
    
        private System.Collections.Generic.List<double> _valve_open_time = new System.Collections.Generic.List<double>();
    
        private double _valve_open_interval = 0.2D;
    
        private int _repeat_count = 200;
    
        public WaterValveOperationControl()
        {
        }
    
        protected WaterValveOperationControl(WaterValveOperationControl other)
        {
            _valve_open_time = other._valve_open_time;
            _valve_open_interval = other._valve_open_interval;
            _repeat_count = other._repeat_count;
        }
    
        /// <summary>
        /// An array with the times (s) the valve is open during calibration
        /// </summary>
        [System.Xml.Serialization.XmlIgnoreAttribute()]
        [Newtonsoft.Json.JsonPropertyAttribute("valve_open_time", Required=Newtonsoft.Json.Required.Always)]
        [YamlDotNet.Serialization.YamlMemberAttribute(Alias="valve_open_time")]
        [System.ComponentModel.DescriptionAttribute("An array with the times (s) the valve is open during calibration")]
        public System.Collections.Generic.List<double> Valve_open_time
        {
            get
            {
                return _valve_open_time;
            }
            set
            {
                _valve_open_time = value;
            }
        }
    
        /// <summary>
        /// Time between two consecutive valve openings (s)
        /// </summary>
        [Newtonsoft.Json.JsonPropertyAttribute("valve_open_interval")]
        [YamlDotNet.Serialization.YamlMemberAttribute(Alias="valve_open_interval")]
        [System.ComponentModel.DescriptionAttribute("Time between two consecutive valve openings (s)")]
        public double Valve_open_interval
        {
            get
            {
                return _valve_open_interval;
            }
            set
            {
                _valve_open_interval = value;
            }
        }
    
        /// <summary>
        /// Number of times the valve opened per measure valve_open_time entry
        /// </summary>
        [Newtonsoft.Json.JsonPropertyAttribute("repeat_count")]
        [YamlDotNet.Serialization.YamlMemberAttribute(Alias="repeat_count")]
        [System.ComponentModel.DescriptionAttribute("Number of times the valve opened per measure valve_open_time entry")]
        public int Repeat_count
        {
            get
            {
                return _repeat_count;
            }
            set
            {
                _repeat_count = value;
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
            stringBuilder.Append("valve_open_time = " + _valve_open_time + ", ");
            stringBuilder.Append("valve_open_interval = " + _valve_open_interval + ", ");
            stringBuilder.Append("repeat_count = " + _repeat_count);
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


    [System.CodeDom.Compiler.GeneratedCodeAttribute("Bonsai.Sgen", "0.3.0.0 (Newtonsoft.Json v13.0.0.0, YamlDotNet v13.0.0.0)")]
    [Bonsai.CombinatorAttribute()]
    [Bonsai.WorkflowElementCategoryAttribute(Bonsai.ElementCategory.Source)]
    public partial class WaterValveCalibrationModel
    {
    
        private string _describedBy;
    
        private object _schema_version;
    
        private WaterValveOperationControl _operation_control = new WaterValveOperationControl();
    
        private WaterValveCalibration _calibration = new WaterValveCalibration();
    
        private string _rootPath;
    
        private System.DateTimeOffset? _date;
    
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
            _schema_version = other._schema_version;
            _operation_control = other._operation_control;
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
    
        [Newtonsoft.Json.JsonPropertyAttribute("describedBy", Required=Newtonsoft.Json.Required.Always)]
        [YamlDotNet.Serialization.YamlMemberAttribute(Alias="describedBy")]
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
    
        [System.Xml.Serialization.XmlIgnoreAttribute()]
        [Newtonsoft.Json.JsonPropertyAttribute("schema_version")]
        [YamlDotNet.Serialization.YamlMemberAttribute(Alias="schema_version")]
        public object Schema_version
        {
            get
            {
                return _schema_version;
            }
            set
            {
                _schema_version = value;
            }
        }
    
        [System.Xml.Serialization.XmlIgnoreAttribute()]
        [Newtonsoft.Json.JsonPropertyAttribute("operation_control", Required=Newtonsoft.Json.Required.Always)]
        [YamlDotNet.Serialization.YamlMemberAttribute(Alias="operation_control")]
        public WaterValveOperationControl Operation_control
        {
            get
            {
                return _operation_control;
            }
            set
            {
                _operation_control = value;
            }
        }
    
        [System.Xml.Serialization.XmlIgnoreAttribute()]
        [Newtonsoft.Json.JsonPropertyAttribute("calibration", Required=Newtonsoft.Json.Required.Always)]
        [YamlDotNet.Serialization.YamlMemberAttribute(Alias="calibration")]
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
        [YamlDotNet.Serialization.YamlMemberAttribute(Alias="rootPath")]
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
        [YamlDotNet.Serialization.YamlMemberAttribute(Alias="date")]
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
    
        [Newtonsoft.Json.JsonPropertyAttribute("notes")]
        [YamlDotNet.Serialization.YamlMemberAttribute(Alias="notes")]
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
        [YamlDotNet.Serialization.YamlMemberAttribute(Alias="experiment")]
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
        [YamlDotNet.Serialization.YamlMemberAttribute(Alias="experimenter")]
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
        [YamlDotNet.Serialization.YamlMemberAttribute(Alias="allowDirty")]
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
        [YamlDotNet.Serialization.YamlMemberAttribute(Alias="remoteDataPath")]
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
        [YamlDotNet.Serialization.YamlMemberAttribute(Alias="rngSeed")]
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
        [YamlDotNet.Serialization.YamlMemberAttribute(Alias="commitHash")]
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
            stringBuilder.Append("schema_version = " + _schema_version + ", ");
            stringBuilder.Append("operation_control = " + _operation_control + ", ");
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
    [System.CodeDom.Compiler.GeneratedCodeAttribute("Bonsai.Sgen", "0.3.0.0 (Newtonsoft.Json v13.0.0.0, YamlDotNet v13.0.0.0)")]
    [System.ComponentModel.DescriptionAttribute("Serializes a sequence of data model objects into JSON strings.")]
    [Bonsai.CombinatorAttribute()]
    [Bonsai.WorkflowElementCategoryAttribute(Bonsai.ElementCategory.Transform)]
    public partial class SerializeToJson
    {
    
        private System.IObservable<string> Process<T>(System.IObservable<T> source)
        {
            return System.Reactive.Linq.Observable.Select(source, value => Newtonsoft.Json.JsonConvert.SerializeObject(value));
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
    [System.CodeDom.Compiler.GeneratedCodeAttribute("Bonsai.Sgen", "0.3.0.0 (Newtonsoft.Json v13.0.0.0, YamlDotNet v13.0.0.0)")]
    [System.ComponentModel.DescriptionAttribute("Deserializes a sequence of JSON strings into data model objects.")]
    [System.ComponentModel.DefaultPropertyAttribute("Type")]
    [Bonsai.WorkflowElementCategoryAttribute(Bonsai.ElementCategory.Transform)]
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


    /// <summary>
    /// Serializes a sequence of data model objects into YAML strings.
    /// </summary>
    [System.CodeDom.Compiler.GeneratedCodeAttribute("Bonsai.Sgen", "0.3.0.0 (Newtonsoft.Json v13.0.0.0, YamlDotNet v13.0.0.0)")]
    [System.ComponentModel.DescriptionAttribute("Serializes a sequence of data model objects into YAML strings.")]
    [Bonsai.CombinatorAttribute()]
    [Bonsai.WorkflowElementCategoryAttribute(Bonsai.ElementCategory.Transform)]
    public partial class SerializeToYaml
    {
    
        private System.IObservable<string> Process<T>(System.IObservable<T> source)
        {
            return System.Reactive.Linq.Observable.Defer(() =>
            {
                var serializer = new YamlDotNet.Serialization.SerializerBuilder()
                    .Build();
                return System.Reactive.Linq.Observable.Select(source, value => serializer.Serialize(value)); 
            });
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
    /// Deserializes a sequence of YAML strings into data model objects.
    /// </summary>
    [System.CodeDom.Compiler.GeneratedCodeAttribute("Bonsai.Sgen", "0.3.0.0 (Newtonsoft.Json v13.0.0.0, YamlDotNet v13.0.0.0)")]
    [System.ComponentModel.DescriptionAttribute("Deserializes a sequence of YAML strings into data model objects.")]
    [System.ComponentModel.DefaultPropertyAttribute("Type")]
    [Bonsai.WorkflowElementCategoryAttribute(Bonsai.ElementCategory.Transform)]
    [System.Xml.Serialization.XmlIncludeAttribute(typeof(Bonsai.Expressions.TypeMapping<WaterValveCalibration>))]
    [System.Xml.Serialization.XmlIncludeAttribute(typeof(Bonsai.Expressions.TypeMapping<WaterValveCalibrationInput>))]
    [System.Xml.Serialization.XmlIncludeAttribute(typeof(Bonsai.Expressions.TypeMapping<WaterValveCalibrationOutput>))]
    [System.Xml.Serialization.XmlIncludeAttribute(typeof(Bonsai.Expressions.TypeMapping<WaterValveOperationControl>))]
    [System.Xml.Serialization.XmlIncludeAttribute(typeof(Bonsai.Expressions.TypeMapping<WaterValveCalibrationModel>))]
    public partial class DeserializeFromYaml : Bonsai.Expressions.SingleArgumentExpressionBuilder
    {
    
        public DeserializeFromYaml()
        {
            Type = new Bonsai.Expressions.TypeMapping<WaterValveCalibrationModel>();
        }

        public Bonsai.Expressions.TypeMapping Type { get; set; }

        public override System.Linq.Expressions.Expression Build(System.Collections.Generic.IEnumerable<System.Linq.Expressions.Expression> arguments)
        {
            var typeMapping = (Bonsai.Expressions.TypeMapping)Type;
            var returnType = typeMapping.GetType().GetGenericArguments()[0];
            return System.Linq.Expressions.Expression.Call(
                typeof(DeserializeFromYaml),
                "Process",
                new System.Type[] { returnType },
                System.Linq.Enumerable.Single(arguments));
        }

        private static System.IObservable<T> Process<T>(System.IObservable<string> source)
        {
            return System.Reactive.Linq.Observable.Defer(() =>
            {
                var serializer = new YamlDotNet.Serialization.DeserializerBuilder()
                    .Build();
                return System.Reactive.Linq.Observable.Select(source, value =>
                {
                    var reader = new System.IO.StringReader(value);
                    var parser = new YamlDotNet.Core.MergingParser(new YamlDotNet.Core.Parser(reader));
                    return serializer.Deserialize<T>(parser);
                });
            });
        }
    }
}