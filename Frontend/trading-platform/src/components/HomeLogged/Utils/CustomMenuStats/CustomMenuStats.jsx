import { Chart as ChartJS, ArcElement } from 'chart.js';
import { Doughnut } from 'react-chartjs-2';
import { Typography, Grid } from '@mui/material';
import Menu from '@mui/material/Menu';
import './CustomMenuStats.css';

ChartJS.register(ArcElement);

export function CustomMenuStats({anchorAccountStats, handleCloseAccountStats,data,funds, portofolio}) {
    return (
        <Menu
            keepMounted
            anchorEl={anchorAccountStats}
            onClose={handleCloseAccountStats}
            open={Boolean(anchorAccountStats)}
        >
            <div id='firstDivMenuStats'>
                <div id='secondDivMenuStats'>
                    <Doughnut data={data} />
                </div>
                <div id='textDivMenuStats'>
                    <Grid container spacing={1} direction='column'>
                        <Grid item xs={1} ><Typography>Free funds</Typography></Grid>

                        <Grid item xs={1} ><Typography id='fundsTypographyMenuStats'>${funds}</Typography></Grid>

                        <Grid item xs={1} ><Typography>Portofolio</Typography></Grid>

                        <Grid item xs={1} ><Typography id='portofolioTypographyMenuStats'>${portofolio}</Typography></Grid>
                    </Grid>
                </div>
            </div>
        </Menu>
    )
}