import React from "react";
import countries from '../../../../Utils/Extra/Countries';
import AdapterDateFns from '@mui/lab/AdapterDateFns'
import { LocalizationProvider, DesktopDatePicker } from '@mui/lab';
import {
    Button, TextField, Grid, Stack, FormControl, Select, MenuItem, InputLabel,
    FormHelperText, Box, Dialog, DialogActions, DialogContent, DialogTitle
} from '@mui/material';
import {
    checkIsValidUsername, checkIsValidPassword, checkIsValidEmail, checkIsValidPhone, checkIsValidName,
    checkIsValidCountryCode, checkIsValidNationality, checkIsValidCountry, checkIsEmpty, checkIsValidSurname, checkIsValidDate,
} from '../../../../Utils/Extra/Validator';
import ReactCountryFlag from "react-country-flag";
import './CustomRegister.css';
import { USER_HOST } from "../../../../Utils/Extra/Hosts";

export function CustomRegister({ openRegister, Transition, setOpenRegister, setMessageRegister, handleClickOpenRegisterComplete }) {

    const [usernameRegister, setUsernameRegister] = React.useState("");
    const handleChangeUsernameRegister = (event) => {
        setUsernameRegister(event.target.value);
        if (checkIsValidUsername(event.target.value)) {
            setErrorUsernameRegisterMessage("");
        }
    };

    const [passwordRegister, setPasswordRegister] = React.useState("");
    const handleChangePasswordRegister = (event) => {
        setPasswordRegister(event.target.value);
        if (checkIsValidPassword(event.target.value)) {
            setErrorPasswordRegisterMessage("");
        }
    };

    const [emailRegister, setEmailRegister] = React.useState("");
    const handleChangeEmailRegister = (event) => {
        setEmailRegister(event.target.value);
        if (checkIsValidEmail(event.target.value)) {
            setErrorEmailRegisterMessage("");
        }
    };

    const [phoneRegister, setPhoneRegister] = React.useState("");
    const handleChangePhoneRegister = (event) => {
        setPhoneRegister(event.target.value);
        if (checkIsValidPhone(event.target.value)) {
            setErrorPhoneRegisterMessage("");
        }
    };

    const [phoneCountryRegister, setPhoneCountryRegister] = React.useState("");
    const handleChangePhoneCountry = (event) => {
        setPhoneCountryRegister(event.target.value);
        if (checkIsValidCountryCode(event.target.value)) {
            setErrorPhoneCodeRegisterMessage("");
        }
    };

    const [nameRegister, setNameRegister] = React.useState("");
    const handleChangeNameRegister = (event) => {
        setNameRegister(event.target.value);
        if (checkIsValidName(event.target.value)) {
            setErrorNameRegisterMessage("");
        }
    };

    const [surnameRegister, setSurnameRegister] = React.useState("");
    const handleChangeSurnameRegister = (event) => {
        setSurnameRegister(event.target.value);
        if (checkIsValidSurname(event.target.value)) {
            setErrorSurnameRegisterMessage("");
        }
    };

    const [addressRegister, setAddressRegister] = React.useState("");
    const handleChangeAddressRegister = (event) => {
        setAddressRegister(event.target.value);
        if (checkIsEmpty(event.target.value)) {
            setErrorAddressRegisterMessage("");
        }
    };

    const [country, setCountry] = React.useState("");
    const handleChangeCountry = (event) => {
        setCountry(event.target.value);
        if (checkIsValidCountry(event.target.value)) {
            setErrorCountryRegisterMessage("");
        }
    }

    const [nationality, setNationality] = React.useState("");
    const handleChangeNationality = (event) => {
        setNationality(event.target.value);
        if (checkIsValidNationality(event.target.value)) {
            setErrorNationalityRegisterMessage("");
        }
    }

    const [dateRegister, setDateRegister] = React.useState(new Date());
    const handleChangeDateRegister = (newValue) => {
        setDateRegister(newValue);
        if (checkIsValidDate(newValue)) {
            setErrorDateRegisterMessage("");
        }
    };


    const [errorUsernameRegisterMessage, setErrorUsernameRegisterMessage]=React.useState("");
    const [errorPasswordRegisterMessage, setErrorPasswordRegisterMessage]=React.useState("");
    const [errorEmailRegisterMessage, setErrorEmailRegisterMessage]=React.useState("");
    const [errorPhoneRegisterMessage, setErrorPhoneRegisterMessage]=React.useState("");
    const [errorPhoneCodeRegisterMessage, setErrorPhoneCodeRegisterMessage]=React.useState("");
    const [errorNameRegisterMessage, setErrorNameRegisterMessage]=React.useState("");
    const [errorSurnameRegisterMessage, setErrorSurnameRegisterMessage]=React.useState("");
    const [errorCountryRegisterMessage, setErrorCountryRegisterMessage]=React.useState("");
    const [errorAddressRegisterMessage, setErrorAddressRegisterMessage]=React.useState("");
    const [errorNationalityRegisterMessage, setErrorNationalityRegisterMessage]=React.useState("");
    const [errorDateRegisterMessage, setErrorDateRegisterMessage]=React.useState("");


    function resetAllErrorsMessage(){
        setErrorUsernameRegisterMessage("");
        setErrorPasswordRegisterMessage("");
        setErrorEmailRegisterMessage("");
        setErrorPhoneRegisterMessage("");
        setErrorPhoneCodeRegisterMessage("");
        setErrorNameRegisterMessage("");
        setErrorSurnameRegisterMessage("");
        setErrorCountryRegisterMessage("");
        setErrorAddressRegisterMessage("");
        setErrorNationalityRegisterMessage("");
        setErrorDateRegisterMessage("");
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
            setErrorUsernameRegisterMessage("Bad username format");
            result = false;
        }

        if (!checkIsValidPassword(passwordRegister)) {
            setErrorPasswordRegisterMessage("Requires 1 upper, 1 digit, 1 lower, 1 special character, min length is 8")
            result = false;
        }

        if (!checkIsValidEmail(emailRegister)) {
            setErrorUsernameRegisterMessage("Bad email format");
            result = false;
        }

        if (!checkIsValidName(nameRegister)) {
            setErrorNameRegisterMessage("");
            result = false;
        }

        if (!checkIsValidSurname(surnameRegister)) {
            setErrorSurnameRegisterMessage("");
            result = false;
        }

        if (!checkIsValidPhone(phoneRegister)) {
            setErrorPhoneRegisterMessage("");
            result = false;
        }

        if (!checkIsValidDate(dateBirthRegister)) {
            setErrorDateRegisterMessage("Minimum 18 years old required");
            result = false;
        }

        if (!checkIsValidCountryCode(phoneCountryRegister)) {
            setErrorPhoneCodeRegisterMessage("Select a phone code");
            result = false;
        }

        if (!checkIsValidCountry(country)) {
            setErrorCountryRegisterMessage("Select a country");
            result = false;
        }

        if (!checkIsEmpty(addressRegister)) {
            setErrorAddressRegisterMessage("Use an address");
            result = false;
        }

        if (!checkIsValidNationality(nationality)) {
            setErrorNationalityRegisterMessage("Select your nationality");
            result = false;
        }

        return result;
    }

    const handleCloseRegister = () => {
        setOpenRegister(false);
        resetAllErrorsMessage();
        resetAllRegisterFields();
    };

    const handleSendRegister = () => {

        if (checkFields(usernameRegister, passwordRegister, emailRegister, nameRegister, surnameRegister, addressRegister, nationality, country, phoneCountryRegister, phoneRegister, dateRegister)) {
            var dateBirthRegister = dateRegister.toLocaleDateString("en-US", { year: 'numeric' }) + "-" + dateRegister.toLocaleDateString("en-US", { month: 'numeric' }) + "-" + dateRegister.toLocaleDateString("en-US", { day: 'numeric' });
            fetch("http://"+USER_HOST+"/register", {
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
                            setMessageRegister(message.message);
                            handleClickOpenRegisterComplete();
                        });

                    } else if (data.status === 409) {
                        data.json().then((message) => {
                            console.log(message.error);
                            if(message.error==='User already exists')
                            {
                                setErrorUsernameRegisterMessage(message.error);
                            }
                            if(message.error==='Email already exists')
                            {
                                setErrorEmailRegisterMessage(message.error);
                            }
                            if(message.error==='Phone already exists')
                            {
                                setErrorPhoneRegisterMessage(message.error);
                            }
                        });
                    } else {
                        setMessageRegister('Internal server error');
                        throw new Error("Internal server error");
                    }
                })
                .catch((error) => {
                    handleCloseRegister();
                    setMessageRegister('Eroare');
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
            PaperProps={{
                style: { borderRadius: 10 }
              }}
        >
            <DialogTitle>Register</DialogTitle>
            <DialogContent>
                <TextField
                    autoFocus
                    margin="dense"
                    id="username"
                    error={errorUsernameRegisterMessage!==""}
                    helperText={errorUsernameRegisterMessage}
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
                    error={errorPasswordRegisterMessage!==""}
                    helperText={errorPasswordRegisterMessage}
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
                    error={errorEmailRegisterMessage!==""}
                    helperText={errorEmailRegisterMessage}
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
                            error={errorPhoneCodeRegisterMessage!==""}
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
                            <FormHelperText>{errorPhoneCodeRegisterMessage}</FormHelperText>
                        </FormControl>
                    </Grid>
                    <Grid item xs={5}>
                        <Box>
                            <TextField
                                autoFocus
                                margin="dense"
                                id="phone"
                                type='numeric'
                                error={errorPhoneRegisterMessage!==""}
                                helperText={errorPhoneRegisterMessage}
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
                            error={errorNameRegisterMessage!==""}
                            helperText={errorNameRegisterMessage}
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
                            error={errorSurnameRegisterMessage!==""}
                            helperText={errorSurnameRegisterMessage}
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
                    error={errorAddressRegisterMessage!==""}
                    helperText={errorAddressRegisterMessage}
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
                            error={errorCountryRegisterMessage!==""}
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
                            <FormHelperText>{errorCountryRegisterMessage}</FormHelperText>
                        </FormControl>
                    </Grid>
                    <Grid item xs={6}>
                        <FormControl
                            error={errorNationalityRegisterMessage!==""}
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
                            <FormHelperText>{errorNationalityRegisterMessage}</FormHelperText>
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
                                        error={errorDateRegisterMessage!==""}
                                        helperText={errorDateRegisterMessage} />}
                            />
                        </Stack>
                    </LocalizationProvider>
                </FormControl>
            </DialogContent>
            <DialogActions>
                <Button fullWidth id='buttonRegister' onClick={handleSendRegister}>Register</Button>
            </DialogActions>
        </Dialog>
    )
}