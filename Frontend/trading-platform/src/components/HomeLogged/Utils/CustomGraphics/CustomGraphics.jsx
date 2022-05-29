import { Button } from "@mui/material";
import React from "react";
import Chart from "react-apexcharts";
import './CustomGraphics.css';


export default function CustomGraphics({ margin, datas, setPeriod, period }) {

    function click_1D(){
        setPeriod('1D');
    };

    function click_1M(){
        setPeriod('1M');
    };

    function click_3M(){
        setPeriod('3M');
    };

    function click_6M(){
        setPeriod('6M');
    };

    function click_max(){
        setPeriod('max');
    };

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
            <Button id={(period=='1D')?'buttonClickedPeriod':'buttonPeriod'} onClick={click_1D} disableRipple >1D</Button>
            <Button disableRipple id={(period=='1M')?'buttonClickedPeriod':'buttonPeriod'} onClick={click_1M}>1M</Button>
            <Button disableRipple id={(period=='3M')?'buttonClickedPeriod':'buttonPeriod'} onClick={click_3M}>3M</Button>
            <Button disableRipple id={(period=='6M')?'buttonClickedPeriod':'buttonPeriod'} onClick={click_6M}>6M</Button>
            <Button disableRipple id={(period=='max')?'buttonClickedPeriod':'buttonPeriod'} onClick={click_max}>MAX</Button>

        </div>
    );
}