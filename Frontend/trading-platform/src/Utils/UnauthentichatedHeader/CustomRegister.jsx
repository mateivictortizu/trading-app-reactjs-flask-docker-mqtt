import "./UnauthentichatedHeader.css";
import React from "react";
import countries from '../countries';
import AdapterDateFns from '@mui/lab/AdapterDateFns'
import { LocalizationProvider, DesktopDatePicker } from '@mui/lab';
import {
    Button, TextField, Grid, Stack, FormControl, Select, MenuItem, InputLabel,
    FormHelperText, Box, Dialog, DialogActions, DialogContent, DialogTitle
} from '@mui/material';
import ReactCountryFlag from "react-country-flag";

export function CustomRegister({ openRegister, handleCloseRegister, Transition, errorUsernameRegister, usernameRegister, handleChangeUsernameRegister,
    errorPasswordRegister, passwordRegister, handleChangePasswordRegister, errorEmailRegister, emailRegister,
    handleChangeEmailRegister, errorPhoneCodeRegister, phoneCountryRegister, handleChangePhoneCountry,
    errorPhoneRegister, phoneRegister, handleChangePhoneRegister, errorNameRegister, nameRegister, handleChangeNameRegister,
    errorSurnameRegister, surnameRegister, handleChangeSurnameRegister, addressRegister, handleChangeAddressRegister, errorCountryRegister,
    country, handleChangeCountry, errorNationalityRegister, nationality, handleChangeNationality, dateRegister, handleChangeDateRegister, errorDateRegister,
    handleSendRegister }) {
    return (
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