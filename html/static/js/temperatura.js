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
    colorStart: '#252CE8',   // Colors
    colorStop: '#ff0000',    // just experiment with them
    strokeColor: '#E0E0E0',  // to see which ones work best for you
    generateGradient: false,
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
    percentColors: percentColors = [[-0.20, "#252CE8"], [0.20, "#619EFF"], [0.60, "#FF780D"], [1.0, "#ff0000"]],
    staticLabels: {
        font: "14px sans-serif",  // Specifies font
        labels: [ -20,-10,0, 10, 20, 30, 40, 50, 60],  // Print labels at these values
        color: "#FFFFFF",  // Optional: Label text color
        fractionDigits: 0  // Optional: Numerical precision. 0=round off.
    },
};
var target = document.getElementById('foo2'); // your canvas element
var gauge = new Gauge(target).setOptions(opts); // create sexy gauge!
gauge.maxValue = 60; // set max gauge value
gauge.setMinValue(-20);  // Prefer setter over gauge.minValue = 0
gauge.animationSpeed = 32; // set animation speed (32 is default value)
gauge.set(25); // set actual value