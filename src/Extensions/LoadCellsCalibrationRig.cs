//----------------------
// <auto-generated>
//     Generated using the NJsonSchema v10.9.0.0 (Newtonsoft.Json v13.0.0.0) (http://NJsonSchema.org)
// </auto-generated>
//----------------------


namespace AindBehaviorServices.LoadCellsCalibrationRig
{
    #pragma warning disable // Disable all warnings

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
    public partial class LoadCellCalibrationInput
    {
    
        private int _channel;
    
        private System.Collections.Generic.List<MeasuredOffset> _offsetMeasurement = new System.Collections.Generic.List<MeasuredOffset>();
    
        private System.Collections.Generic.List<MeasuredWeight> _weightMeasurement = new System.Collections.Generic.List<MeasuredWeight>();
    
        public LoadCellCalibrationInput()
        {
        }
    
        protected LoadCellCalibrationInput(LoadCellCalibrationInput other)
        {
            _channel = other._channel;
            _offsetMeasurement = other._offsetMeasurement;
            _weightMeasurement = other._weightMeasurement;
        }
    
        /// <summary>
        /// Load cell channel number available
        /// </summary>
        [Newtonsoft.Json.JsonPropertyAttribute("channel", Required=Newtonsoft.Json.Required.Always)]
        [System.ComponentModel.DescriptionAttribute("Load cell channel number available")]
        public int Channel
        {
            get
            {
                return _channel;
            }
            set
            {
                _channel = value;
            }
        }
    
        [System.Xml.Serialization.XmlIgnoreAttribute()]
        [Newtonsoft.Json.JsonPropertyAttribute("offset_measurement")]
        public System.Collections.Generic.List<MeasuredOffset> OffsetMeasurement
        {
            get
            {
                return _offsetMeasurement;
            }
            set
            {
                _offsetMeasurement = value;
            }
        }
    
        [System.Xml.Serialization.XmlIgnoreAttribute()]
        [Newtonsoft.Json.JsonPropertyAttribute("weight_measurement")]
        public System.Collections.Generic.List<MeasuredWeight> WeightMeasurement
        {
            get
            {
                return _weightMeasurement;
            }
            set
            {
                _weightMeasurement = value;
            }
        }
    
        public System.IObservable<LoadCellCalibrationInput> Process()
        {
            return System.Reactive.Linq.Observable.Defer(() => System.Reactive.Linq.Observable.Return(new LoadCellCalibrationInput(this)));
        }
    
        public System.IObservable<LoadCellCalibrationInput> Process<TSource>(System.IObservable<TSource> source)
        {
            return System.Reactive.Linq.Observable.Select(source, _ => new LoadCellCalibrationInput(this));
        }
    
        protected virtual bool PrintMembers(System.Text.StringBuilder stringBuilder)
        {
            stringBuilder.Append("channel = " + _channel + ", ");
            stringBuilder.Append("offset_measurement = " + _offsetMeasurement + ", ");
            stringBuilder.Append("weight_measurement = " + _weightMeasurement);
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
    public partial class LoadCellCalibrationOutput
    {
    
        private int _channel;
    
        private int? _offset;
    
        private double? _baseline;
    
        private double? _slope;
    
        private System.Collections.Generic.List<MeasuredWeight> _weightLookup = new System.Collections.Generic.List<MeasuredWeight>();
    
        public LoadCellCalibrationOutput()
        {
        }
    
        protected LoadCellCalibrationOutput(LoadCellCalibrationOutput other)
        {
            _channel = other._channel;
            _offset = other._offset;
            _baseline = other._baseline;
            _slope = other._slope;
            _weightLookup = other._weightLookup;
        }
    
        /// <summary>
        /// Load cell channel number available
        /// </summary>
        [Newtonsoft.Json.JsonPropertyAttribute("channel", Required=Newtonsoft.Json.Required.Always)]
        [System.ComponentModel.DescriptionAttribute("Load cell channel number available")]
        public int Channel
        {
            get
            {
                return _channel;
            }
            set
            {
                _channel = value;
            }
        }
    
        [System.Xml.Serialization.XmlIgnoreAttribute()]
        [Newtonsoft.Json.JsonPropertyAttribute("offset")]
        public int? Offset
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
    
        [System.Xml.Serialization.XmlIgnoreAttribute()]
        [Newtonsoft.Json.JsonPropertyAttribute("baseline")]
        public double? Baseline
        {
            get
            {
                return _baseline;
            }
            set
            {
                _baseline = value;
            }
        }
    
        [System.Xml.Serialization.XmlIgnoreAttribute()]
        [Newtonsoft.Json.JsonPropertyAttribute("slope")]
        public double? Slope
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
    
        [System.Xml.Serialization.XmlIgnoreAttribute()]
        [Newtonsoft.Json.JsonPropertyAttribute("weight_lookup")]
        public System.Collections.Generic.List<MeasuredWeight> WeightLookup
        {
            get
            {
                return _weightLookup;
            }
            set
            {
                _weightLookup = value;
            }
        }
    
        public System.IObservable<LoadCellCalibrationOutput> Process()
        {
            return System.Reactive.Linq.Observable.Defer(() => System.Reactive.Linq.Observable.Return(new LoadCellCalibrationOutput(this)));
        }
    
        public System.IObservable<LoadCellCalibrationOutput> Process<TSource>(System.IObservable<TSource> source)
        {
            return System.Reactive.Linq.Observable.Select(source, _ => new LoadCellCalibrationOutput(this));
        }
    
        protected virtual bool PrintMembers(System.Text.StringBuilder stringBuilder)
        {
            stringBuilder.Append("channel = " + _channel + ", ");
            stringBuilder.Append("offset = " + _offset + ", ");
            stringBuilder.Append("baseline = " + _baseline + ", ");
            stringBuilder.Append("slope = " + _slope + ", ");
            stringBuilder.Append("weight_lookup = " + _weightLookup);
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
    public partial class LoadCells
    {
    
        private string _deviceType = "loadcells";
    
        private BaseModel _additionalSettings;
    
        private LoadCellsCalibration _calibration;
    
        private int _whoAmI = 1232;
    
        private string _serialNumber;
    
        private string _portName;
    
        public LoadCells()
        {
        }
    
        protected LoadCells(LoadCells other)
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
        public LoadCellsCalibration Calibration
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
    
        public System.IObservable<LoadCells> Process()
        {
            return System.Reactive.Linq.Observable.Defer(() => System.Reactive.Linq.Observable.Return(new LoadCells(this)));
        }
    
        public System.IObservable<LoadCells> Process<TSource>(System.IObservable<TSource> source)
        {
            return System.Reactive.Linq.Observable.Select(source, _ => new LoadCells(this));
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
    /// Load cells calibration class
    /// </summary>
    [System.CodeDom.Compiler.GeneratedCodeAttribute("Bonsai.Sgen", "0.3.0.0 (Newtonsoft.Json v13.0.0.0)")]
    [System.ComponentModel.DescriptionAttribute("Load cells calibration class")]
    [Bonsai.CombinatorAttribute()]
    [Bonsai.WorkflowElementCategoryAttribute(Bonsai.ElementCategory.Source)]
    public partial class LoadCellsCalibration
    {
    
        private string _deviceName = "LoadCells";
    
        private LoadCellsCalibrationInput _input = new LoadCellsCalibrationInput();
    
        private LoadCellsCalibrationOutput _output = new LoadCellsCalibrationOutput();
    
        private System.DateTimeOffset? _date;
    
        private string _description = "Calibration of the load cells system";
    
        private string _notes;
    
        public LoadCellsCalibration()
        {
        }
    
        protected LoadCellsCalibration(LoadCellsCalibration other)
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
        public LoadCellsCalibrationInput Input
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
        public LoadCellsCalibrationOutput Output
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
    
        public System.IObservable<LoadCellsCalibration> Process()
        {
            return System.Reactive.Linq.Observable.Defer(() => System.Reactive.Linq.Observable.Return(new LoadCellsCalibration(this)));
        }
    
        public System.IObservable<LoadCellsCalibration> Process<TSource>(System.IObservable<TSource> source)
        {
            return System.Reactive.Linq.Observable.Select(source, _ => new LoadCellsCalibration(this));
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
    public partial class LoadCellsCalibrationInput
    {
    
        private System.Collections.Generic.List<LoadCellCalibrationInput> _channels = new System.Collections.Generic.List<LoadCellCalibrationInput>();
    
        public LoadCellsCalibrationInput()
        {
        }
    
        protected LoadCellsCalibrationInput(LoadCellsCalibrationInput other)
        {
            _channels = other._channels;
        }
    
        [System.Xml.Serialization.XmlIgnoreAttribute()]
        [Newtonsoft.Json.JsonPropertyAttribute("channels")]
        public System.Collections.Generic.List<LoadCellCalibrationInput> Channels
        {
            get
            {
                return _channels;
            }
            set
            {
                _channels = value;
            }
        }
    
        public System.IObservable<LoadCellsCalibrationInput> Process()
        {
            return System.Reactive.Linq.Observable.Defer(() => System.Reactive.Linq.Observable.Return(new LoadCellsCalibrationInput(this)));
        }
    
        public System.IObservable<LoadCellsCalibrationInput> Process<TSource>(System.IObservable<TSource> source)
        {
            return System.Reactive.Linq.Observable.Select(source, _ => new LoadCellsCalibrationInput(this));
        }
    
        protected virtual bool PrintMembers(System.Text.StringBuilder stringBuilder)
        {
            stringBuilder.Append("channels = " + _channels);
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
    public partial class LoadCellsCalibrationOutput
    {
    
        private System.Collections.Generic.List<LoadCellCalibrationOutput> _channels = new System.Collections.Generic.List<LoadCellCalibrationOutput>();
    
        public LoadCellsCalibrationOutput()
        {
        }
    
        protected LoadCellsCalibrationOutput(LoadCellsCalibrationOutput other)
        {
            _channels = other._channels;
        }
    
        [System.Xml.Serialization.XmlIgnoreAttribute()]
        [Newtonsoft.Json.JsonPropertyAttribute("channels")]
        public System.Collections.Generic.List<LoadCellCalibrationOutput> Channels
        {
            get
            {
                return _channels;
            }
            set
            {
                _channels = value;
            }
        }
    
        public System.IObservable<LoadCellsCalibrationOutput> Process()
        {
            return System.Reactive.Linq.Observable.Defer(() => System.Reactive.Linq.Observable.Return(new LoadCellsCalibrationOutput(this)));
        }
    
        public System.IObservable<LoadCellsCalibrationOutput> Process<TSource>(System.IObservable<TSource> source)
        {
            return System.Reactive.Linq.Observable.Select(source, _ => new LoadCellsCalibrationOutput(this));
        }
    
        protected virtual bool PrintMembers(System.Text.StringBuilder stringBuilder)
        {
            stringBuilder.Append("channels = " + _channels);
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
    public partial class MeasuredOffset
    {
    
        private int _offset;
    
        private double _baseline;
    
        public MeasuredOffset()
        {
        }
    
        protected MeasuredOffset(MeasuredOffset other)
        {
            _offset = other._offset;
            _baseline = other._baseline;
        }
    
        /// <summary>
        /// The applied offset resistor value[-255, 255]
        /// </summary>
        [Newtonsoft.Json.JsonPropertyAttribute("offset", Required=Newtonsoft.Json.Required.Always)]
        [System.ComponentModel.DescriptionAttribute("The applied offset resistor value[-255, 255]")]
        public int Offset
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
        /// The measured baseline value
        /// </summary>
        [Newtonsoft.Json.JsonPropertyAttribute("baseline", Required=Newtonsoft.Json.Required.Always)]
        [System.ComponentModel.DescriptionAttribute("The measured baseline value")]
        public double Baseline
        {
            get
            {
                return _baseline;
            }
            set
            {
                _baseline = value;
            }
        }
    
        public System.IObservable<MeasuredOffset> Process()
        {
            return System.Reactive.Linq.Observable.Defer(() => System.Reactive.Linq.Observable.Return(new MeasuredOffset(this)));
        }
    
        public System.IObservable<MeasuredOffset> Process<TSource>(System.IObservable<TSource> source)
        {
            return System.Reactive.Linq.Observable.Select(source, _ => new MeasuredOffset(this));
        }
    
        protected virtual bool PrintMembers(System.Text.StringBuilder stringBuilder)
        {
            stringBuilder.Append("offset = " + _offset + ", ");
            stringBuilder.Append("baseline = " + _baseline);
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
    public partial class MeasuredWeight
    {
    
        private double _weight;
    
        private double _baseline;
    
        public MeasuredWeight()
        {
        }
    
        protected MeasuredWeight(MeasuredWeight other)
        {
            _weight = other._weight;
            _baseline = other._baseline;
        }
    
        /// <summary>
        /// The applied weight in grams
        /// </summary>
        [Newtonsoft.Json.JsonPropertyAttribute("weight", Required=Newtonsoft.Json.Required.Always)]
        [System.ComponentModel.DescriptionAttribute("The applied weight in grams")]
        public double Weight
        {
            get
            {
                return _weight;
            }
            set
            {
                _weight = value;
            }
        }
    
        /// <summary>
        /// The measured baseline value
        /// </summary>
        [Newtonsoft.Json.JsonPropertyAttribute("baseline", Required=Newtonsoft.Json.Required.Always)]
        [System.ComponentModel.DescriptionAttribute("The measured baseline value")]
        public double Baseline
        {
            get
            {
                return _baseline;
            }
            set
            {
                _baseline = value;
            }
        }
    
        public System.IObservable<MeasuredWeight> Process()
        {
            return System.Reactive.Linq.Observable.Defer(() => System.Reactive.Linq.Observable.Return(new MeasuredWeight(this)));
        }
    
        public System.IObservable<MeasuredWeight> Process<TSource>(System.IObservable<TSource> source)
        {
            return System.Reactive.Linq.Observable.Select(source, _ => new MeasuredWeight(this));
        }
    
        protected virtual bool PrintMembers(System.Text.StringBuilder stringBuilder)
        {
            stringBuilder.Append("weight = " + _weight + ", ");
            stringBuilder.Append("baseline = " + _baseline);
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
    public partial class CalibrationRig
    {
    
        private string _aindBehaviorServicesPkgVersion = "0.8.9";
    
        private string _version = "0.0.0";
    
        private string _computerName;
    
        private string _rigName;
    
        private LoadCells _loadCells = new LoadCells();
    
        public CalibrationRig()
        {
        }
    
        protected CalibrationRig(CalibrationRig other)
        {
            _aindBehaviorServicesPkgVersion = other._aindBehaviorServicesPkgVersion;
            _version = other._version;
            _computerName = other._computerName;
            _rigName = other._rigName;
            _loadCells = other._loadCells;
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
        [Newtonsoft.Json.JsonPropertyAttribute("load_cells", Required=Newtonsoft.Json.Required.Always)]
        public LoadCells LoadCells
        {
            get
            {
                return _loadCells;
            }
            set
            {
                _loadCells = value;
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
            stringBuilder.Append("load_cells = " + _loadCells);
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

        public System.IObservable<string> Process(System.IObservable<BaseModel> source)
        {
            return Process<BaseModel>(source);
        }

        public System.IObservable<string> Process(System.IObservable<LoadCellCalibrationInput> source)
        {
            return Process<LoadCellCalibrationInput>(source);
        }

        public System.IObservable<string> Process(System.IObservable<LoadCellCalibrationOutput> source)
        {
            return Process<LoadCellCalibrationOutput>(source);
        }

        public System.IObservable<string> Process(System.IObservable<LoadCells> source)
        {
            return Process<LoadCells>(source);
        }

        public System.IObservable<string> Process(System.IObservable<LoadCellsCalibration> source)
        {
            return Process<LoadCellsCalibration>(source);
        }

        public System.IObservable<string> Process(System.IObservable<LoadCellsCalibrationInput> source)
        {
            return Process<LoadCellsCalibrationInput>(source);
        }

        public System.IObservable<string> Process(System.IObservable<LoadCellsCalibrationOutput> source)
        {
            return Process<LoadCellsCalibrationOutput>(source);
        }

        public System.IObservable<string> Process(System.IObservable<MeasuredOffset> source)
        {
            return Process<MeasuredOffset>(source);
        }

        public System.IObservable<string> Process(System.IObservable<MeasuredWeight> source)
        {
            return Process<MeasuredWeight>(source);
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
    [System.Xml.Serialization.XmlIncludeAttribute(typeof(Bonsai.Expressions.TypeMapping<BaseModel>))]
    [System.Xml.Serialization.XmlIncludeAttribute(typeof(Bonsai.Expressions.TypeMapping<LoadCellCalibrationInput>))]
    [System.Xml.Serialization.XmlIncludeAttribute(typeof(Bonsai.Expressions.TypeMapping<LoadCellCalibrationOutput>))]
    [System.Xml.Serialization.XmlIncludeAttribute(typeof(Bonsai.Expressions.TypeMapping<LoadCells>))]
    [System.Xml.Serialization.XmlIncludeAttribute(typeof(Bonsai.Expressions.TypeMapping<LoadCellsCalibration>))]
    [System.Xml.Serialization.XmlIncludeAttribute(typeof(Bonsai.Expressions.TypeMapping<LoadCellsCalibrationInput>))]
    [System.Xml.Serialization.XmlIncludeAttribute(typeof(Bonsai.Expressions.TypeMapping<LoadCellsCalibrationOutput>))]
    [System.Xml.Serialization.XmlIncludeAttribute(typeof(Bonsai.Expressions.TypeMapping<MeasuredOffset>))]
    [System.Xml.Serialization.XmlIncludeAttribute(typeof(Bonsai.Expressions.TypeMapping<MeasuredWeight>))]
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