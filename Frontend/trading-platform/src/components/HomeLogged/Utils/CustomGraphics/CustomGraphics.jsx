import { Button } from "@mui/material";
import React from "react";
import Chart from "react-apexcharts";
import './CustomGraphics.css';


export default function CustomGraphics({ name, margin, datas, setPeriod, period, color }) {

    function click_1D() {
        setPeriod('1D');
    };

    function click_1M() {
        setPeriod('1M');
    };

    function click_3M() {
        setPeriod('3M');
    };

    function click_6M() {
        setPeriod('6M');
    };

    function click_max() {
        setPeriod('max');
    };

    var state = {

        options: {
            colors: [color],
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
                },
                tooltip: {
                    enabled: false
                }
            },
            yaxis: {
                opposite: true,
            }
        },
        series: [
            {
                name: name,
                data: datas
            }
        ]
    };

    var typeClick = null;
    if (color === '#2AAA8A') {
        typeClick = 'buttonClickedPeriodUp';
    }
    else {
        typeClick = 'buttonClickedPeriodDown';
    }

    return (
        <div style={{ marginLeft: '15px', marginRight: '15px' }}>
            <Chart
                options={state.options}
                series={state.series}
                type="area"
                height='270px'
                style={{ marginTop: margin }}
            />
            <Button id={(period === '1D') ? typeClick : 'buttonPeriod'} onClick={click_1D} disableRipple >1D</Button>
            <Button disableRipple id={(period === '1M') ? typeClick : 'buttonPeriod'} onClick={click_1M}>1M</Button>
            <Button disableRipple id={(period === '3M') ? typeClick : 'buttonPeriod'} onClick={click_3M}>3M</Button>
            <Button disableRipple id={(period === '6M') ? typeClick : 'buttonPeriod'} onClick={click_6M}>6M</Button>
            <Button disableRipple id={(period === 'max') ? typeClick : 'buttonPeriod'} onClick={click_max}>MAX</Button>

        </div>
    );
}