function plot (selector, csv_file) {
  d3.csv(csv_file, d => [+d.decompositions, +d.time]).then( data => {

  var div = d3.select(selector);
  // set the dimensions and margins of the graph
  var margin = {top: 10, right: 30, bottom: 40, left: 60};
  var width = 400;
  var height = width;

  // append the svg object to the body of the page
  var svg = div
    .select("svg")
      .attr("width", width + margin.left + margin.right)
      .attr("height", height + margin.top + margin.bottom)
    .append("g")
      .attr("transform",
            "translate(" + margin.left + "," + margin.top + ")");


  logs = data.map(i => [Math.log(i[0]), Math.log(i[1])])
  fit = polyfit(logs.map(i=>i[0]), logs.map(i=>i[1]), 2)
  xs = linspace(0, Math.log(1000), 20)
  ys = polyval(fit, xs)

  approx = xs.map((_, i) => [Math.exp(xs[i]), Math.exp(ys[i])])


  var x = d3.scaleLog()
    .domain([1, 1000])
    .range([ 0, width ]);
  svg.append("g")
    .attr("transform", "translate(0," + height + ")")
    .call(d3.axisBottom(x).tickValues([1, 10, 100, 1000]).tickFormat(d3.format(".0f")));


  function formatPower(x) {
    const e = Math.log10(x);
    if (e !== Math.floor(e)) return; // Ignore non-exact power of ten.
    return `10${(e + "").replace(/./g, c => "⁰¹²³⁴⁵⁶⁷⁸⁹"[c] || "⁻")}`;
  }


  // Add Y axis
  var y = d3.scaleLog()
    .domain(d3.extent(approx, i => i[1]))
    .range([ height, 0 ]);
  svg.append("g")
    .call(d3.axisLeft(y).ticks(9).tickFormat(formatPower));

  svg.append("path")
    .datum(approx)
    .attr("stroke", "currentColor")
    .attr("fill", "none")
    .attr("stroke-width", 1.5)
    .attr("d", d3.line()
      .x(i => x(i[0]))
      .y(i => y(i[1]))
      )

  const tooltip = div.append("div")
    .attr("class", "svg-tooltip")
      .style("position", "absolute")
      .style("visibility", "hidden")

  svg.append("g")
        .attr("fill", "currentColor")
        .attr("class", "data")
        .attr("stroke", "none")
      .selectAll("circle")
      .data(data)
      .join("circle")
        .attr("cx", i => x(i[0]))
        .attr("cy", i => y(i[1]))
        .attr("r", 3)
        .on("mouseover", function(event, d) {
          tooltip.style("visibility", "visible");
          d3.select(this).attr("opacity", 0.5);
        })
        .on("mousemove", (event, d) => tooltip.style("top", (event.pageY-10)+"px")
                                             .style("left",(event.pageX+10)+"px")
                                             .html("s:" + d[0] + "<br/>time: " + d3.format(".2s")(d[1]) + "s"))
        .on("mouseout", function(event, d) {
          tooltip.style("visibility", "hidden"),
          d3.select(this).attr("opacity", 1);
        });

  svg.append("text")
      .attr("fill", "currentColor")
      .attr("text-anchor", "middle")
      .attr("x", width/2)
      .attr("y", height + margin.top + 20)
      .text("Количество разложений, s");

  svg.append("text")
      .attr("fill", "currentColor")
      .attr("text-anchor", "middle")
      .attr("transform", "rotate(-90)")
      .attr("y", -margin.left+20)
      .attr("x", -margin.top-height/2)
      .text("Время работы алгоритма, с");
  });
}
