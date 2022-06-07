import React, { useEffect } from "react";
import UnauthentichatedHeader from "./Utils/UnauthentichatedHeader/UnauthentichatedHeader"
import Footer from "../../Utils/Footer/Footer"
import Typography from '@mui/material/Typography';
import Container from '@mui/material/Container';
import "./Home.css"
import InfoIcon from '@mui/icons-material/Info';
import { Grid } from '@mui/material';
import FadeIn from 'react-fade-in';
import { useCookies } from 'react-cookie';
import { useNavigate } from 'react-router-dom';

const Home = () => {
    document.title = "Invest"
    const [cookies, setCookie, removeCookie] = useCookies(['jwt_otp']);
    const navigate = useNavigate();
    useEffect(() => {
        if (cookies.jwt) {
            navigate('/home');
        }
    });

    return (
        <div className="main-div">
            <UnauthentichatedHeader></UnauthentichatedHeader>
            <div className="firstDiv">
                <FadeIn transitionDuration="1000">
                    <Container disableGutters maxWidth="sm" component="main" sx={{ pt: 8, pb: 6 }}>
                        <Typography
                            component="h1"
                            variant="h2"
                            align="center"
                            color="#FFF"
                            gutterBottom
                            id='typographyHome'
                        >

                            Investitii pentru toata lumea fara comision

                        </Typography>
                        <Typography variant="h5" align="center" color="#ffcc00" component="p" gutterBottom>
                            <InfoIcon id='infoIconHome' fontSize='large'></InfoIcon> Se pot aplica si alte taxe. <a>Consultati termenii nostri de tranzactionare</a>.
                        </Typography>
                        <Typography id='typographyHome' variant="h3" align="center" color="#FFF" background="white">

                            Inregisreaza-te acum!

                        </Typography>
                    </Container>
                </FadeIn>
            </div>
            <div className="secondDiv">
                <Container>
                    <div style={{ padding: 20 }}>
                        <Grid container spacing={15} alignItems="center" justifyContent="center"  >
                            <Grid item>
                                <Typography id='typographyHome' variant="h4" align="center" color="#0066cc">
                                    1,5 milioane
                                </Typography>
                                <Typography variant="h6" align="center" color="#000">
                                    clienti
                                </Typography>
                            </Grid>
                            <Grid item>
                                <Typography id='typographyHome' variant="h4" align="center" color="#0066cc">
                                    3,5 miliarde de euro
                                </Typography>
                                <Typography variant="h6" align="center">
                                    in activele clientilor
                                </Typography>
                            </Grid>
                            <Grid item>
                                <Typography id='typographyHome' variant="h4" align="center" color="#0066cc">
                                    1,5 milioane
                                </Typography>
                                <Typography variant="h6" align="center" color="#000">
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
                        <div className="svgDIV">
                            <figure>
                                <svg width="187" height="166" viewBox="0 0 187 166" fill="none" xmlns="http://www.w3.org/2000/svg">
                                    <path fillRule="evenodd" clipRule="evenodd" d="M185.447 39.4468C180.404 72.862 162.668 104.6 103.513 152.822C35.3972 208.347 -35.1484 58.6708 20.9247 32.1842C75.1651 6.56338 199.517 -27.0968 185.447 39.4468Z" fill="#0066cc"></path>
                                </svg>
                            </figure>
                            <figure className="overlap">
                                <center><img src={require('./resource/CySEC.png')} width="50%" height="50%" /></center>
                            </figure>
                        </div>
                        <Typography id='typographyHome' variant="h5" align="center" color="#0066cc">
                            Reglementata de CySEC
                        </Typography>
                        <Typography variant="h7" align="center" color="#000">
                            Trading este autorizata si reglementata de catre CYSEC
                        </Typography>
                    </Grid>
                    <Grid item>
                        <div className="svgDIV">
                            <figure>
                                <svg width="192" height="178" viewBox="0 0 192 178" fill="none" xmlns="http://www.w3.org/2000/svg">
                                    <path fillRule="evenodd" clipRule="evenodd" d="M163.877 171.606C130.324 179.236 92.1325 184.443 25.3786 147.185C-51.4853 104.284 69.3774 -34.0645 114.376 8.33988C157.904 49.3585 232.118 160.16 163.877 171.606Z" fill="#ffcc00"></path>
                                </svg>
                            </figure>
                            <figure className="overlap">
                                <center><img src={require('./resource/Fonduri.png')} width="50%" height="50%" /></center>
                            </figure>
                        </div>
                        <Typography id='typographyHome' variant="h5" align="center" color="#0066cc">
                            Fondurile tale sunt in siguranta
                        </Typography>
                        <Typography variant="h7" align="center" >
                            Fondurile dvs. sunt tinute intr-un cont separat, protejat de ICF in limita a 20.000 $.
                        </Typography>

                    </Grid>
                    <Grid item>
                        <div className="svgDIV">
                            <figure>
                                <svg width="197" height="174" viewBox="0 0 197 174" fill="none" xmlns="http://www.w3.org/2000/svg">
                                    <path fillRule="evenodd" clipRule="evenodd" d="M33.5876 2.13818C70.1321 -3.63092 108.213 3.34863 174.46 44.9496C250.741 92.8514 111.3 208.321 68.7726 162.778C27.6349 118.723 -40.2365 9.75045 33.5876 2.13818Z" fill="#0066cc"></path>
                                </svg>
                            </figure>
                            <figure className="overlap">
                                <center><img src={require('./resource/Date.png')} width="50%" height="50%" /></center>
                            </figure>
                        </div>
                        <Typography id='typographyHome' variant="h5" align="center" color="#0066cc">
                            Datele dvs. sunt protejate
                        </Typography>
                        <Typography variant="h7" align="center" color="#000">
                            Datele dvs sunt protejate datorita implementarii celor mai bune practici din domeniu
                        </Typography>
                    </Grid>
                </Grid>
            </div>
            <div className="thirdDiv">

                <Container disableGutters maxWidth="sm" component="main" sx={{ pt: 8, pb: 6 }}>
                    <Typography
                        component="h1"
                        variant="h2"
                        align="center"
                        color="#FFF"
                        gutterBottom
                        id='typographyHome'
                    >
                        <FadeIn>
                            Incepe sa investesti acum!
                        </FadeIn>
                    </Typography>
                </Container>
            </div>
            <div className="footerDiv">
                <Footer className='footer'></Footer>
            </div>
        </div>
    )
}

export default Home;

