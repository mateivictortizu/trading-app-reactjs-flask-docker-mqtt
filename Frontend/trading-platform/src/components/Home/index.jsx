import UnauthentichatedHeader from "../../Utils/UnauthentichatedHeader/UnauthentichatedHeader"
import Footer from "../../Utils/Footer/Footer"
import Typography from '@mui/material/Typography';
import Container from '@mui/material/Container';
import "./Home.css"
import InfoIcon from '@mui/icons-material/Info';
import { Grid } from '@mui/material';
import FadeIn from 'react-fade-in';

const Home = () => {
    document.title = "Invest"

    return (
        <div className="main-div">
            <UnauthentichatedHeader></UnauthentichatedHeader>
            <div className="firstDiv">
                <Container disableGutters maxWidth="sm" component="main" sx={{ pt: 8, pb: 6 }}>
                    <Typography
                    component="h1"
                    variant="h2"
                    align="center"
                    color="#FFF"
                    gutterBottom
                    >
                    Investitii pentru toata lumea fara comision
                    </Typography>
                    <Typography variant="h5" align="center" color="#ffcc00" component="p" gutterBottom>
                        <InfoIcon style={{position: 'relative', top: '8px'}} fontSize='large'></InfoIcon> Se pot aplica si alte taxe. <a>Consultati termenii nostri de tranzactionare</a>.
                    </Typography>
                    <Typography variant="h3" align="center" color="#FFF">
                        Inregisreaza-te acum!
                    </Typography>               
                </Container>
            </div>
            <div className="secondDiv">
                <Container>
                <div style={{ padding: 20 }}>
                    <Grid container spacing={5} alignItems="center" justifyContent="center"  >
                        <Grid item>                    
                            <Typography variant="h3" align="center" color="#0066cc">
                                1,5 milioane
                            </Typography> 
                            <Typography variant="h4" align="center" color="#000">
                                clienti
                            </Typography> 
                        </Grid>
                        <Grid item>                    
                            <Typography variant="h3" align="center" color="#0066cc">
                                3,5 miliarde de euro
                            </Typography> 
                            <Typography variant="h4" align="center">
                                in activele clientilor
                            </Typography>
                        </Grid>
                        <Grid item>                    
                            <Typography variant="h3" align="center" color="#0066cc">
                                1,5 milioane
                            </Typography> 
                            <Typography variant="h4" align="center" color="#000">
                                ordine executate zilnic
                            </Typography> 
                        </Grid>
                    </Grid>
                </div>
                </Container>
            </div>
            <div style={{ padding: 20 }}>
                <Grid container spacing={5} 
                    direction="column"
                    alignItems="center"
                    justifyContent="center"
                >
                    <Grid item> 
                        <Typography variant="h4" align="center" color="#0066cc">
                            Reglementata de CySEC
                        </Typography> 
                        <Typography variant="h6" align="center" color="#000">
                            Trading este autorizata si reglementata de catre CYSEC
                        </Typography> 
                    </Grid>
                    <Grid item>                    
                        <Typography variant="h4" align="center" color="#0066cc">
                            Fondurile tale sunt in siguranta
                        </Typography> 
                        <Typography variant="h6" align="center">
                            Fondurile dvs. sunt tinute intr-un cont separat, protejat de ICF in limita a 20.000 $
                        </Typography>
                        <Typography variant="h6" align="center">
                            si in plus asigurat in limita a 1 milion $ de Lloyd's of Londone
                        </Typography>
                    </Grid>
                    <Grid item>                    
                        <Typography variant="h4" align="center" color="#0066cc">
                            Datele dvs. sunt protejate
                        </Typography> 
                        <Typography variant="h6" align="center" color="#000">
                            Datele dvs sunt protejate datorita implementarii celor mai bune practici din domeniu
                        </Typography> 
                    </Grid>
                </Grid>
            </div>
            <br></br>
            <Footer></Footer>
        </div>
        )
}

export default Home;

