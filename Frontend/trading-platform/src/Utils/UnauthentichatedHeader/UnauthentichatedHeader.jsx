import "./UnauthentichatedHeader.css";
import { Button } from "@mui/material";
import React, {useState} from "react";
import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import TextField from '@mui/material/TextField';
import Dialog from '@mui/material/Dialog';
import DialogActions from '@mui/material/DialogActions';
import DialogContent from '@mui/material/DialogContent';
import DialogTitle from '@mui/material/DialogTitle'
import Slide from '@mui/material/Slide';
import countries from '../countries';
import InputLabel from '@mui/material/InputLabel';
import Select from '@mui/material/Select';
import MenuItem from '@mui/material/MenuItem';
import FormControl from '@mui/material/FormControl';
import AdapterDateFns from '@mui/lab/AdapterDateFns';
import LocalizationProvider from '@mui/lab/LocalizationProvider';
import DesktopDatePicker from '@mui/lab/DesktopDatePicker';
import Stack from '@mui/material/Stack';

const Transition = React.forwardRef(function Transition(props, ref) {
    return <Slide direction="up" ref={ref} {...props} />;
  });

 

export default function UnauthentichatedHeader ()
{


    const [openLogin, setOpenLogin] = React.useState(false);
    const [openRegister, setOpenRegister] = React.useState(false);

    const [identifierLogin, setIdentifierLogin] = React.useState("");
    const handleChangeIdentifierLogin =(event)=>{
        setIdentifierLogin(event.target.value);
    };

    const [passwordLogin, setPasswordLogin] = React.useState("");
    const handleChangePasswordLogin =(event)=>{
        setPasswordLogin(event.target.value);
    };

    const [usernameRegister, setUsernameRegister] = React.useState("");
    const handleChangeUsernameRegister =(event)=>{
        setUsernameRegister(event.target.value);
    };

    const [passwordRegister, setPasswordRegister] = React.useState("");
    const handleChangePasswordRegister =(event)=>{
        setPasswordRegister(event.target.value);
    };

    const [emailRegister, setEmailRegister] = React.useState("");
    const handleChangeEmailRegister =(event)=>{
        setEmailRegister(event.target.value);
    };

    const [phoneRegister, setPhoneRegister] = React.useState("");
    const handleChangePhoneRegister =(event)=>{
        setPhoneRegister(event.target.value);
    };

    const [nameRegister, setNameRegister] = React.useState("");
    const handleChangeNameRegister =(event)=>{
        setNameRegister(event.target.value);
    };

    const [surnameRegister, setSurnameRegister] = React.useState("");
    const handleChangeSurnameRegister =(event)=>{
        setSurnameRegister(event.target.value);
    };

    const [addressRegister, setAddressRegister] = React.useState("");
    const handleChangeAddressRegister =(event)=>{
        setAddressRegister(event.target.value);
    };

    const [country, setCountry] = React.useState("");
    const handleChangeCountry =(event)=>{
        setCountry(event.target.value);
    }

    const [nationality, setNationality] = React.useState("");
    const handleChangeNationality =(event)=>{
        setNationality(event.target.value);
    }

    const [dateRegister, setDateRegister] = React.useState(new Date());
    const handleChangeDateRegister = (newValue) => {
      setDateRegister(newValue);
    };

    const handleClickOpenLogin = () => {
      setOpenLogin(true);
    };
  
    const handleCloseLogin = () => {
      setIdentifierLogin("");
      setPasswordLogin("");
      setOpenLogin(false);
    };

    const handleSendLogin = () => {
        fetch("https://127.0.0.1:5001/login",{
            method: "POST",
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                identifier: identifierLogin,
                password: passwordLogin,
            }),        
        })
        .then((data) => {
            if (data.status === 200) {
              data.json().then((message)=>{
                console.log(message);
              });

            } else if (data.status === 404 || data.status === 400 | data.status===401) {
              data.json().then((message) => {
                  console.log(message)
              });
            } else {
              throw new Error("Internal server error");
            }
          })
          .catch((error) => {
            console.log(error);
          });
        handleCloseLogin();
    };

    const handleClickOpenRegister = () => {
        setOpenRegister(true);
      };
    
      const handleCloseRegister = () => {
        setUsernameRegister("");
        setPasswordRegister("");
        setEmailRegister("");
        setNameRegister("");
        setSurnameRegister("");
        setAddressRegister("");
        setCountry("");
        setNationality("");
        setDateRegister(new Date());
        setOpenRegister(false);
      };
  
      const handleSendRegister = () => {
          var dateBirthRegister=dateRegister.toUTCString()
          console.log(dateRegister);
        fetch("https://127.0.0.1:5001/register",{
            method: "POST",
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                username: usernameRegister,
                password: passwordRegister,
                email: emailRegister,
                name: nameRegister,
                surname: surnameRegister,
                address: addressRegister,
                nationality: nationality,
                phone: phoneRegister,
                date_of_birth: dateBirthRegister,
                country: country
            }),        
        })
        .then((data) => {
            if (data.status === 201) {
              data.json().then((message)=>{
                console.log(message);
              });

            } else if (data.status === 404 || data.status === 400 | data.status===401) {
              data.json().then((message) => {
                  console.log(message)
              });
            } else {
              throw new Error("Internal server error");
            }
          })
          .catch((error) => {
            console.log(error);
          });
          handleCloseRegister();
      };

    return (
        <header className="header">
            <div className="header_header-container header_accent">
                <Box sx={{ flexGrow: 1 }}>
                    <section className="warning">
                        <div className="main-wrapper">
                            <div className="warningDiv">
                                <p className="warningText">Investițiile pot să scadă sau să crească. Puteți primi înapoi mai puțin decât ați investit. Performanțele anterioare nu reprezintă o garanție a rezultatelor viitoare.</p>
                            </div>
                        </div>
                    </section>
                </Box>
                <Box sx={{ flexGrow: 1 }}>
                    <AppBar style={{ background: '#0066cc' }} position="static">
                        <Toolbar>
                        <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
                            <div className="svg-icon">
                                <svg width="213" height="27" viewBox="0 0 213 27" fill="none" xmlns="http://www.w3.org/2000/svg">
                                    <path fillRule="evenodd" clipRule="evenodd" d="M112.018 1.39444V11.8079L112.349 17.017L103.279 1.11442C103.001 0.651061 102.722 0.463867 102.163 0.463867H98.6311C97.9798 0.463867 97.7009 0.836328 97.7009 1.39444V25.5671C97.7009 26.1256 97.9798 26.4961 98.6311 26.4961H101.977C102.536 26.4961 102.906 26.1256 102.906 25.5671V15.1535L102.577 9.94372L111.646 25.8463C111.926 26.3104 112.205 26.4961 112.762 26.4961H116.295C116.852 26.4961 117.225 26.2176 117.225 25.5671V1.39444C117.225 0.744272 116.852 0.463867 116.295 0.463867H112.948C112.297 0.463867 112.018 0.744272 112.018 1.39444Z" fill="#FFF"></path>
                                    <path fillRule="evenodd" clipRule="evenodd" d="M92.6801 25.5671V1.39444C92.6801 0.743887 92.3084 0.463867 91.7503 0.463867H88.4032C87.7526 0.463867 87.4734 0.835943 87.4734 1.39444V25.5671C87.4734 26.1252 87.7526 26.4961 88.4032 26.4961H91.7503C92.3084 26.4961 92.6801 26.1252 92.6801 25.5671Z" fill="#FFF"></path>
                                    <path fillRule="evenodd" clipRule="evenodd" d="M51.5874 6.54006L55.2127 14.5955C55.3991 15.1537 55.7692 15.3408 56.2353 15.3408H59.6756C60.419 15.3408 60.6967 14.8759 60.419 14.225L54.5613 1.20774C54.3757 0.651164 54.0032 0.464355 53.5391 0.464355H49.635C49.1693 0.464355 48.798 0.651164 48.6112 1.20774L42.7543 14.225C42.4754 14.8759 42.7543 15.3408 43.4977 15.3408H46.9376C47.4029 15.3408 47.7746 15.1537 47.9606 14.5955L51.5874 6.54006Z" fill="#ebc340"></path>
                                    <path fillRule="evenodd" clipRule="evenodd" d="M30.76 11.9932H27.1347V5.11212H30.76C33.9215 5.11212 35.2241 6.04347 35.2241 8.55363C35.2241 11.0623 33.9215 11.9932 30.76 11.9932ZM36.09 15.8576C39.8196 14.4803 40.5225 11.4898 40.5225 8.55363C40.5225 4.55555 39.2218 0.463867 30.76 0.463867H22.8593C22.2072 0.463867 21.928 0.836328 21.928 1.39444V25.5671C21.928 26.1252 22.2072 26.4961 22.8593 26.4961H26.2049C26.763 26.4961 27.1347 26.1252 27.1347 25.5671V16.6407L31.0234 16.6403L34.8513 25.7535C35.0373 26.3104 35.409 26.4961 35.8747 26.4961H39.3135C40.0588 26.4961 40.3361 26.0312 40.0588 25.3806L36.09 15.8576Z" fill="#FFF"></path>
                                    <path fillRule="evenodd" clipRule="evenodd" d="M18.0236 0.464355H1.28908C0.637366 0.464355 0.358887 0.744375 0.358887 1.39493V4.18319C0.358887 4.74053 0.730963 5.11261 1.28908 5.11261H7.05317V25.5675C7.05317 26.1257 7.33204 26.4966 7.98259 26.4966H11.3301C11.8878 26.4966 12.2595 26.1257 12.2595 25.5675V5.11261H18.0236C18.581 5.11261 18.9527 4.74053 18.9527 4.18319V1.39493C18.9527 0.744375 18.581 0.464355 18.0236 0.464355Z" fill="#FFF"></path>
                                    <path fillRule="evenodd" clipRule="evenodd" d="M140.375 12.5504H132.472C131.823 12.5504 131.543 12.8297 131.543 13.481V16.2712C131.543 16.8274 131.823 17.2002 132.472 17.2002H136.006V18.1289C136.006 21.5681 134.702 22.3138 131.543 22.3138C128.382 22.3138 127.08 21.5681 127.08 18.1289V8.83237C127.08 5.39202 128.382 4.64825 131.543 4.64825C134.424 4.64825 135.726 5.29919 136.006 7.9018C136.006 8.55389 136.284 8.83237 136.935 8.83237H140.375C140.933 8.83237 141.304 8.46068 141.304 7.9018C141.119 3.16033 139.445 0 131.543 0C123.083 0 121.781 3.62447 121.781 8.55389V18.407C121.781 23.3364 123.083 26.962 131.543 26.962C140.003 26.962 141.304 23.3364 141.304 18.407V13.481C141.304 12.8297 140.933 12.5504 140.375 12.5504Z" fill="#FFF"></path>
                                    <path fillRule="evenodd" clipRule="evenodd" d="M77.5263 17.6638C77.5263 21.1046 76.2244 21.8487 73.063 21.8487H69.4369V5.11261H73.063C76.2244 5.11261 77.5263 5.85753 77.5263 9.29712V17.6638ZM73.063 0.464355H65.1604C64.5098 0.464355 64.231 0.836431 64.231 1.39455V25.5675C64.231 26.1257 64.5098 26.4966 65.1604 26.4966H73.063C81.5233 26.4966 82.8244 22.871 82.8244 17.9442V9.01787C82.8244 4.08998 81.5233 0.464355 73.063 0.464355Z" fill="#FFF"></path>
                                </svg>
                            </div>
                        </Typography>
                        <Stack spacing={2} direction="row">
                            <Button variant="outlined" color='inherit' onClick={handleClickOpenRegister}>Register</Button>
                            <Button color="inherit" onClick={handleClickOpenLogin}>Login</Button>
                        </Stack>
                        </Toolbar>
                    </AppBar>
                </Box>

                <Dialog 
                    open={openLogin} 
                    onClose={handleCloseLogin}
                    TransitionComponent={Transition}
                    keepMounted
                >
                    <DialogTitle>Login</DialogTitle>
                    <DialogContent>
                    <TextField
                        autoFocus
                        margin="dense"
                        id="identifierLogin"
                        label="Username or Email Address"
                        type="string"
                        value={identifierLogin}
                        onChange={handleChangeIdentifierLogin}
                        fullWidth
                    />
                    <TextField
                        autoFocus
                        margin="dense"
                        id="passwordLogin"
                        label="Password"
                        type="password"
                        value={passwordLogin}
                        onChange={handleChangePasswordLogin}
                        fullWidth
                    />
                    </DialogContent>
                    <DialogActions>
                    <Button onClick={handleCloseLogin}>Cancel</Button>
                    <Button onClick={handleSendLogin}>Login</Button>
                    </DialogActions>
                </Dialog>

                <Dialog 
                    open={openRegister} 
                    onClose={handleCloseRegister}
                    TransitionComponent={Transition}
                    keepMounted
                >
                    <DialogTitle>Register</DialogTitle>
                    <DialogContent>
                    <TextField
                        autoFocus
                        margin="dense"
                        id="username"
                        label="Username"
                        type="string"
                        value={usernameRegister}
                        onChange={handleChangeUsernameRegister}
                        fullWidth
                    />
                    <TextField
                        autoFocus
                        margin="dense"
                        id="password"
                        label="Password"
                        type="password"
                        value={passwordRegister}
                        onChange={handleChangePasswordRegister}
                        fullWidth
                    />
                    <TextField
                        autoFocus
                        margin="dense"
                        id="email"
                        label="Email"
                        type="email"
                        value={emailRegister}
                        onChange={handleChangeEmailRegister}
                        fullWidth
                    />
                    <TextField
                        autoFocus
                        margin="dense"
                        id="phone"
                        label="Phone"
                        type="string"
                        value={phoneRegister}
                        onChange={handleChangePhoneRegister}
                        fullWidth
                    />                    
                    <TextField
                        autoFocus
                        margin="dense"
                        id="name"
                        label="Name"
                        type="string"
                        value={nameRegister}
                        onChange={handleChangeNameRegister}
                        fullWidth
                    />
                    <TextField
                        autoFocus
                        margin="dense"
                        id="surname"
                        label="Surname"
                        type="string"
                        value={surnameRegister}
                        onChange={handleChangeSurnameRegister}
                        fullWidth
                    />
                    <TextField
                        autoFocus
                        margin="dense"
                        id="address"
                        label="Address"
                        type="string"
                        value={addressRegister}
                        onChange={handleChangeAddressRegister}
                        fullWidth

                    />
                    <Box sx={{ minWidth: 120 }}>
                        <FormControl margin="dense" fullWidth>
                            <InputLabel id="demo-simple-select-label">Country</InputLabel>
                            <Select
                            labelId="demo-simple-select-label"
                            id="demo-simple-select"
                            value={country}
                            label="Country"
                            onChange={handleChangeCountry}
                            >
                                {countries.map((country) => (
                                    <MenuItem
                                    value={country.countryName}
                                    key={country.countryShortCode}
                                    >
                                    {country.countryName}
                                    </MenuItem>
                                ))}
                            </Select>
                        </FormControl>
                    </Box>
                    <Box sx={{ minWidth: 120 }}>
                        <FormControl margin="dense" fullWidth>
                            <InputLabel id="demo-simple-select-label">Nationality</InputLabel>
                            <Select
                            labelId="demo-simple-select-label"
                            id="demo-simple-select"
                            value={nationality}
                            label="Nationality"
                            onChange={handleChangeNationality}
                            >
                                {countries.map((country) => (
                                    <MenuItem
                                    value={country.countryName}
                                    key={country.countryShortCode}
                                    >
                                    {country.countryName}
                                    </MenuItem>
                                ))}
                            </Select>
                        </FormControl>
                    </Box>
                    <FormControl margin="dense" fullWidth>
                        <LocalizationProvider dateAdapter={AdapterDateFns}>
                            <Stack spacing={3}>
                                <DesktopDatePicker
                                label="Date of birth"
                                inputFormat="dd/MM/yyyy"
                                value={dateRegister}
                                onChange={handleChangeDateRegister}
                                renderInput={(params) => <TextField {...params} />}
                                />
                            </Stack>
                        </LocalizationProvider>
                    </FormControl>
                    </DialogContent>
                    <DialogActions>
                    <Button onClick={handleCloseRegister}>Cancel</Button>
                    <Button onClick={handleSendRegister}>Register</Button>
                    </DialogActions>
                </Dialog>

            </div>
        </header>
    );
}