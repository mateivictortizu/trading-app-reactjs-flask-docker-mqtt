import { Button } from "@mui/material";
import React from "react";
import Chart from "react-apexcharts";

export default function CustomGraphics({ margin }) {
    var state = {

        options: {
            chart: {
                toolbar: {
                    show: false
                },
                type: 'area',
                stacked: false,
                parentHeightOffset: 0,
                zoom: {
                    type: 'x',
                    enabled: false,
                    autoScaleYaxis: true
                },
            },
            grid: {
                show: true
            },
            dataLabels: {
                enabled: false
            },
            fill: {
                type: 'gradient',
                gradient: {
                    shadeIntensity: 1,
                    inverseColors: false,
                    opacityFrom: 0,
                    opacityTo: 0,
                    stops: [100]
                },
            },
            markers: {
                size: 0,
            },
            xaxis: {
                show: false,
                labels: {
                    show: false
                },
                axisBorder: {
                    show: false
                },
                axisTicks: {
                    show: false
                }
            },
            yaxis:{
                opposite: true,
            }
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
                style={{ marginTop: margin }}
            />
            <Button style={{ margin: '5px' }}>1D</Button>
            <Button style={{ margin: '5px' }}>1W</Button>
            <Button style={{ margin: '5px' }}>1M</Button>
            <Button style={{ margin: '5px' }}>3M</Button>
            <Button style={{ margin: '5px' }}>MAX</Button>

        </div>
    );
}