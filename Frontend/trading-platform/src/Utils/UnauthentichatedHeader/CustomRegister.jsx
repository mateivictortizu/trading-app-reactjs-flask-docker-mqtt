import "./UnauthentichatedHeader.css";
import React from "react";
import countries from '../countries';
import AdapterDateFns from '@mui/lab/AdapterDateFns'
import { LocalizationProvider, DesktopDatePicker } from '@mui/lab';
import {
    Button, TextField, Grid, Stack, FormControl, Select, MenuItem, InputLabel,
    FormHelperText, Box, Dialog, DialogActions, DialogContent, DialogTitle
} from '@mui/material';
import {
    checkIsValidUsername, checkIsValidPassword, checkIsValidEmail, checkIsValidPhone, checkIsValidName, checkIsValidSurname, checkIsValidDate,
    checkIsValidCountryCode, checkIsValidNationality, checkIsValidCountry
} from '../validator';
import ReactCountryFlag from "react-country-flag";

export function CustomRegister({ openRegister, Transition, setOpenRegister,setMessageRegister, handleClickOpenRegisterComplete}) {

        const [usernameRegister, setUsernameRegister] = React.useState("");
        const handleChangeUsernameRegister = (event) => {
            setUsernameRegister(event.target.value);
            if (checkIsValidUsername(event.target.value)) {
                setErrorUsernameRegister(false);
            }
        };
    
        const [passwordRegister, setPasswordRegister] = React.useState("");
        const handleChangePasswordRegister = (event) => {
            setPasswordRegister(event.target.value);
            if (checkIsValidPassword(event.target.value)) {
                setErrorPasswordRegister(false);
            }
        };
    
        const [emailRegister, setEmailRegister] = React.useState("");
        const handleChangeEmailRegister = (event) => {
            setEmailRegister(event.target.value);
            if (checkIsValidEmail(event.target.value)) {
                setErrorEmailRegister(false);
            }
        };
    
        const [phoneRegister, setPhoneRegister] = React.useState("");
        const handleChangePhoneRegister = (event) => {
            setPhoneRegister(event.target.value);
            if (checkIsValidPhone(event.target.value)) {
                setErrorPhoneRegister(false);
            }
        };
    
        const [phoneCountryRegister, setPhoneCountryRegister] = React.useState("");
        const handleChangePhoneCountry = (event) => {
            setPhoneCountryRegister(event.target.value);
            if (checkIsValidCountryCode(event.target.value)) {
                setErrorPhoneCodeRegister(false);
            }
        };
    
        const [nameRegister, setNameRegister] = React.useState("");
        const handleChangeNameRegister = (event) => {
            setNameRegister(event.target.value);
            if (checkIsValidName(event.target.value)) {
                setErrorNameRegister(false);
            }
        };
    
        const [surnameRegister, setSurnameRegister] = React.useState("");
        const handleChangeSurnameRegister = (event) => {
            setSurnameRegister(event.target.value);
            if (checkIsValidSurname(event.target.value)) {
                setErrorSurnameRegister(false);
            }
        };
    
        const [addressRegister, setAddressRegister] = React.useState("");
        const handleChangeAddressRegister = (event) => {
            setAddressRegister(event.target.value);
        };
    
        const [country, setCountry] = React.useState("");
        const handleChangeCountry = (event) => {
            setCountry(event.target.value);
            if (checkIsValidCountry(event.target.value)) {
                setErrorCountryRegister(false);
            }
        }
    
        const [nationality, setNationality] = React.useState("");
        const handleChangeNationality = (event) => {
            setNationality(event.target.value);
            if (checkIsValidNationality(event.target.value)) {
                setErrorNationalityRegister(false);
            }
        }
    
        const [dateRegister, setDateRegister] = React.useState(new Date());
        const handleChangeDateRegister = (newValue) => {
            setDateRegister(newValue);
            if (checkIsValidDate(newValue)) {
                setErrorDateRegister(false);
            }
        };

        const [errorUsernameRegister, setErrorUsernameRegister] = React.useState(false);
        const [errorPasswordRegister, setErrorPasswordRegister] = React.useState(false);
        const [errorEmailRegister, setErrorEmailRegister] = React.useState(false);
        const [errorPhoneRegister, setErrorPhoneRegister] = React.useState(false);
        const [errorPhoneCodeRegister, setErrorPhoneCodeRegister] = React.useState(false);
        const [errorNameRegister, setErrorNameRegister] = React.useState(false);
        const [errorSurnameRegister, setErrorSurnameRegister] = React.useState(false);
        const [errorCountryRegister, setErrorCountryRegister] = React.useState(false);
        const [errorNationalityRegister, setErrorNationalityRegister] = React.useState(false);
        const [errorDateRegister, setErrorDateRegister] = React.useState(false);
    
        function setAllErrorsRegisterFalse() {
            setErrorUsernameRegister(false);
            setErrorPasswordRegister(false);
            setErrorEmailRegister(false);
            setErrorPhoneRegister(false);
            setErrorPhoneCodeRegister(false);
            setErrorNameRegister(false);
            setErrorSurnameRegister(false);
            setErrorCountryRegister(false);
            setErrorNationalityRegister(false);
            setErrorDateRegister(false);
        }
    
        function resetAllRegisterFields() {
            setUsernameRegister("");
            setPasswordRegister("");
            setEmailRegister("");
            setPhoneRegister("");
            setPhoneCountryRegister("");
            setNameRegister("");
            setSurnameRegister("");
            setAddressRegister("");
            setCountry("");
            setNationality("");
            setDateRegister(new Date());
        }

        function checkFields(usernameRegister, passwordRegister, emailRegister, nameRegister, surnameRegister, addressRegister, nationality, country, phoneCountryRegister, phoneRegister, dateBirthRegister) {
            var result = true
    
            if (!checkIsValidUsername(usernameRegister)) {
                setErrorUsernameRegister(true);
                result = false;
            }
    
            if (!checkIsValidPassword(passwordRegister)) {
                setErrorPasswordRegister(true);
                result = false;
            }
    
            if (!checkIsValidEmail(emailRegister)) {
                setErrorEmailRegister(true);
                result = false;
            }
    
            if (!checkIsValidName(nameRegister)) {
                setErrorNameRegister(true);
                result = false;
            }
    
            if (!checkIsValidSurname(surnameRegister)) {
                setErrorSurnameRegister(true);
                result = false;
            }
    
            if (!checkIsValidPhone(phoneRegister)) {
                setErrorPhoneRegister(true);
                result = false;
            }
    
            if (!checkIsValidDate(dateBirthRegister)) {
                setErrorDateRegister(true);
                result = false;
            }
    
            if (!checkIsValidCountryCode(phoneCountryRegister)) {
                setErrorPhoneCodeRegister(true);
                result = false;
            }
    
            if (!checkIsValidCountry(country)) {
                setErrorCountryRegister(true);
                result = false;
            }
    
            if (!checkIsValidNationality(nationality)) {
                setErrorNationalityRegister(true);
                result = false;
            }
    
            return result;
        }

        const handleCloseRegister = () => {
            resetAllRegisterFields();
            setAllErrorsRegisterFalse();
            setOpenRegister(false);
        };

        const handleSendRegister = () => {
            setAllErrorsRegisterFalse();
    
            if (checkFields(usernameRegister, passwordRegister, emailRegister, nameRegister, surnameRegister, addressRegister, nationality, country, phoneCountryRegister, phoneRegister, dateRegister)) {
                var dateBirthRegister = dateRegister.toLocaleDateString("en-US", { year: 'numeric' }) + "-" + dateRegister.toLocaleDateString("en-US", { month: 'numeric' }) + "-" + dateRegister.toLocaleDateString("en-US", { day: 'numeric' });
                fetch("http://127.0.0.1:5000/register", {
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
                        country: country,
                    }),
                })
                    .then((data) => {
                        if (data.status === 201) {
                            data.json().then((message) => {
                                handleCloseRegister();
                                setMessageRegister(message);
                                console.log(message);
                                handleClickOpenRegisterComplete();
                            });
    
                        } else if (data.status === 404 || data.status === 400 | data.status === 401) {
                            data.json().then((message) => {
                                handleCloseRegister();
                                setMessageRegister(message);
                                console.log(message)
                                handleClickOpenRegisterComplete();
                            });
                        } else {
                            handleCloseRegister();
                            setMessageRegister('Eroare');
                            handleClickOpenRegisterComplete();
                            throw new Error("Internal server error");
                        }
                    })
                    .catch((error) => {
                        handleCloseRegister();
                        setMessageRegister('Eroare');
                        console.log(error);
                        handleClickOpenRegisterComplete();
                    });
            }
        };

    return (
        <Dialog
            open={openRegister}
            onClose={handleCloseRegister}
            TransitionComponent={Transition}
            keepMounted
            style={{backdropFilter: 'blur(4px)'}}
        >
            <DialogTitle>Register</DialogTitle>
            <DialogContent>
                <TextField
                    autoFocus
                    margin="dense"
                    id="username"
                    error={errorUsernameRegister}
                    helperText={errorUsernameRegister ? "Bad username" : ""}
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
                    error={errorPasswordRegister}
                    helperText={errorPasswordRegister ? "Requires 1 upper, 1 digit, 1 lower, 1 special character, min length is 8" : ""}
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
                    error={errorEmailRegister}
                    helperText={errorEmailRegister ? "Bad email format" : ""}
                    label="Email"
                    type="email"
                    value={emailRegister}
                    onChange={handleChangeEmailRegister}
                    fullWidth
                />
                <Grid container spacing={2}
                    direction="row"
                >
                    <Grid item xs={7}>
                        <FormControl
                            error={errorPhoneCodeRegister}
                            margin="dense"
                            fullWidth>
                            <InputLabel id="countryphone-label">Country Phone</InputLabel>
                            <Select
                                labelId="countryPhone"
                                id="countryPhone"
                                value={phoneCountryRegister}
                                label="Country Phone"
                                onChange={handleChangePhoneCountry}
                            >
                                {countries.map((phoneCountry) => (
                                    <MenuItem
                                        value={phoneCountry.countryPhoneCode}
                                        key={phoneCountry.countryShortCode}
                                    >
                                        <ReactCountryFlag
                                            countryCode={phoneCountry.countryShortCode}
                                            style={{
                                                width: '1.5em',
                                                height: '1.5em',
                                            }}
                                            svg
                                        />
                                        &nbsp;
                                        {phoneCountry.countryName + " (+" + phoneCountry.countryPhoneCode + ")"}
                                    </MenuItem>
                                ))}
                            </Select>
                            <FormHelperText>{errorPhoneCodeRegister ? "Select a phone code" : ""}</FormHelperText>
                        </FormControl>
                    </Grid>
                    <Grid item xs={5}>
                        <Box>
                            <TextField
                                autoFocus
                                margin="dense"
                                id="phone"
                                type='numeric'
                                error={errorPhoneRegister}
                                helperText={errorPhoneRegister ? "Bad phone format" : ""}
                                label="Phone"
                                value={phoneRegister}
                                onChange={handleChangePhoneRegister}
                                fullWidth
                            />
                        </Box>
                    </Grid>
                </Grid>
                <Grid container spacing={2}
                    direction="row"
                >
                    <Grid item xs={6}>
                        <TextField
                            autoFocus
                            margin="dense"
                            id="name"
                            error={errorNameRegister}
                            helperText={errorNameRegister ? "Bad name format" : ""}
                            label="Name"
                            type="string"
                            value={nameRegister}
                            onChange={handleChangeNameRegister}
                            fullWidth
                        />
                    </Grid>
                    <Grid item xs={6}>
                        <TextField
                            autoFocus
                            margin="dense"
                            id="surname"
                            error={errorSurnameRegister}
                            helperText={errorSurnameRegister ? "Bad surname format" : ""}
                            label="Surname"
                            type="string"
                            value={surnameRegister}
                            onChange={handleChangeSurnameRegister}
                            fullWidth
                        />
                    </Grid>
                </Grid>
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

                <Grid container spacing={2}
                    direction="row"
                >
                    <Grid item xs={6}>
                        <FormControl
                            error={errorCountryRegister}
                            margin="dense"
                            fullWidth>
                            <InputLabel id="country-label">Country</InputLabel>
                            <Select
                                labelId="country"
                                id="country"
                                value={country}
                                label="Country"
                                onChange={handleChangeCountry}
                            >
                                {countries.map((country) => (
                                    <MenuItem
                                        value={country.countryShortCode}
                                        key={country.countryShortCode}
                                    >
                                        <ReactCountryFlag
                                            countryCode={country.countryShortCode}
                                            style={{
                                                width: '1.5em',
                                                height: '1.5em',
                                            }}
                                            svg
                                        />

                                        &nbsp;
                                        {country.countryName}
                                    </MenuItem>
                                ))}
                            </Select>
                            <FormHelperText>{errorCountryRegister ? "Select a country" : ""}</FormHelperText>
                        </FormControl>
                    </Grid>
                    <Grid item xs={6}>
                        <FormControl
                            error={errorNationalityRegister}
                            margin="dense"
                            fullWidth>
                            <InputLabel id="nationality-lable">Nationality</InputLabel>
                            <Select
                                labelId="nationality"
                                id="nationality"
                                value={nationality}
                                label="Nationality"
                                onChange={handleChangeNationality}
                            >
                                {countries.map((nationality) => (
                                    <MenuItem
                                        value={nationality.countryShortCode}
                                        key={nationality.countryShortCode}
                                    >
                                        <ReactCountryFlag
                                            countryCode={nationality.countryShortCode}
                                            style={{
                                                width: '1.5em',
                                                height: '1.5em',
                                            }}
                                            svg
                                        />

                                        &nbsp;
                                        {nationality.countryName}
                                    </MenuItem>
                                ))}
                            </Select>
                            <FormHelperText>{errorNationalityRegister ? "Select a nationality" : ""}</FormHelperText>
                        </FormControl>
                    </Grid>
                </Grid>
                <FormControl margin="dense" fullWidth>
                    <LocalizationProvider dateAdapter={AdapterDateFns}>
                        <Stack spacing={3}>
                            <DesktopDatePicker
                                label="Date of birth"
                                inputFormat="dd/MM/yyyy"
                                value={dateRegister}
                                onChange={handleChangeDateRegister}
                                renderInput={(params) =>
                                    <TextField {...params}
                                        error={errorDateRegister}
                                        helperText={errorDateRegister ? "Miminum 18 years old requested" : ""} />}
                            />
                        </Stack>
                    </LocalizationProvider>
                </FormControl>
            </DialogContent>
            <DialogActions>
                <Button onClick={handleSendRegister}>Register</Button>
            </DialogActions>
        </Dialog>
    )
}