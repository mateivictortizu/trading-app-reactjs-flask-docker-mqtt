import { Button } from "@mui/material";
import React from "react";
import Chart from "react-apexcharts";

export default function CustomGraphics({ margin, datas }) {
    var state = {

        options: {
            colors : ['#2AAA8A'],
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
                type: 'category',
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
                name: "Apple",
                data: datas
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
            <Button style={{ margin: '5px' }}>1M</Button>
            <Button style={{ margin: '5px' }}>3M</Button>
            <Button style={{ margin: '5px' }}>6M</Button>
            <Button style={{ margin: '5px' }}>MAX</Button>

        </div>
    );
}