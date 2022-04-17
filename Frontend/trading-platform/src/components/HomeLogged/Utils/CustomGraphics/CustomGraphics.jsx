import { Button, ButtonGroup } from "@mui/material";
import React from "react";
import Chart from "react-apexcharts";

export default function CustomGraphics() {
    var state = {

        options: {
            chart: {
                toolbar: {
                    show: false
                },
                type: 'line',
                stacked: false,
                parentHeightOffset: 0,
                zoom: {
                    type: 'x',
                    enabled: false,
                    autoScaleYaxis: true
                },
            },
            grid: {
                show: false
            },
            dataLabels: {
                enabled: false
            },
            fill: {
                type: 'gradient',
                gradient: {
                    shadeIntensity: 1,
                    inverseColors: false,
                    opacityFrom: 0.5,
                    opacityTo: 0.5,
                    stops: [100]
                },
            },
            markers: {
                size: 0,
            },
            xaxis: {
                categories: ['Mai', 'Iunie', 'Iulie', 'August', 'Septembrie', 'Octombrie', 'Noiembrie', 'Decembrie', 'Ianuarie']
            },
        },
        series: [
            {
                name: "Microsoft",
                data: [200.39, 205.06, 301.1, 287.4, 299.44, 250.1, 250.1, 250.1]
            }
        ]
    };


    return (
        <div>
            <Chart
                options={state.options}
                series={state.series}
                type="area"
                height='270px'
                style={{ marginTop: '200px' }}
            />
            <Button style={{ margin: '5px' }}>1D</Button>
            <Button style={{ margin: '5px' }}>1W</Button>
            <Button style={{ margin: '5px' }}>1M</Button>
            <Button style={{ margin: '5px' }}>3M</Button>
            <Button style={{ margin: '5px' }}>MAX</Button>

        </div>
    );
}