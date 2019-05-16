var opts;
opts = {
    angle: 0.1, // The span of the gauge arc
    lineWidth: 0.55, // The line thickness
    radiusScale: 1, // Relative radius
    pointer: {
        length: 0.62, // // Relative to gauge radius
        strokeWidth: 0.0, // The thickness
        color: '#000000' // Fill color
    },
    limitMax: false,     // If false, max value increases automatically if value > maxValue
    limitMin: false,     // If true, the min value of the gauge will be fixed
    colorStart: '#3399FF',   // Colors
    colorStop: '#8FC0DA',    // just experiment with them
    strokeColor: '#E0E0E0',  // to see which ones work best for you
    generateGradient: true,
    highDpiSupport: true,     // High resolution support
    // renderTicks is Optional
    renderTicks: {
        divisions: 0,
        divWidth: 0.6,
        divLength: 0.61,
        divColor: '#333333',
        subDivisions: 2,
        subLength: 0.3,
        subWidth: 0.6,
        subColor: '#666666'

    },
    percentColors: percentColors = [[0.0, "#a9d70b"], [0.50, "#f9c802"], [1.0, "#ff0000"]],
    staticLabels: {
        font: "14px sans-serif",  // Specifies font
        labels: [0, 500, 750, 1000, 1500,],  // Print labels at these values
        color: "#FFFFFF",  // Optional: Label text color
        fractionDigits: 0  // Optional: Numerical precision. 0=round off.
    },
};
var target = document.getElementById('foo'); // your canvas element
var gaugepritisak = new Gauge(target).setOptions(opts); // create sexy gauge!
gaugepritisak.maxValue = 1500; // set max gauge value
gaugepritisak.setMinValue(0);  // Prefer setter over gauge.minValue = 0
gaugepritisak.animationSpeed = 32; // set animation speed (32 is default value)
gaugepritisak.set(950); // set actual value