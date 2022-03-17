import "./UnauthentichatedHeader.css";
import React from "react";
import {
    checkIsValidUsername, checkIsValidPassword, checkIsValidEmail, checkIsValidPhone, checkIsValidName, checkIsValidSurname, checkIsValidDate,
    checkIsValidCountryCode, checkIsValidNationality, checkIsValidCountry
} from '../validator';
import { Slide } from '@mui/material';
import { CustomAppBar } from "./CustomAppBar";
import { CustomLogin } from "./CustomLogin";
import { CustomRegister } from "./CustomRegister";

const Transition = React.forwardRef(function Transition(props, ref) {
    return <Slide direction="up" ref={ref} {...props} />;
});

export default function UnauthentichatedHeader() {
    const [openLogin, setOpenLogin] = React.useState(false);
    const [openRegister, setOpenRegister] = React.useState(false);

    const [identifierLogin, setIdentifierLogin] = React.useState("");
    const handleChangeIdentifierLogin = (event) => {
        setIdentifierLogin(event.target.value);
    };

    const [passwordLogin, setPasswordLogin] = React.useState("");
    const handleChangePasswordLogin = (event) => {
        setPasswordLogin(event.target.value);
    };

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

    const handleClickOpenLogin = () => {
        setOpenLogin(true);
    };

    const handleCloseLogin = () => {
        setIdentifierLogin("");
        setPasswordLogin("");
        setOpenLogin(false);
    };

    const handleSendLogin = () => {
        fetch("https://127.0.0.1:5001/login", {
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
                    data.json().then((message) => {
                        console.log(message);
                    });

                } else if (data.status === 404 || data.status === 400 | data.status === 401) {
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

    const handleClickOpenRegister = () => {
        setOpenRegister(true);
    };

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
                            console.log(message);
                        });

                    } else if (data.status === 404 || data.status === 400 | data.status === 401) {
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
        }
    };

    return (
        <header className="header">
            <div className="header_header-container header_accent">
                <CustomAppBar
                    handleClickOpenRegister={handleClickOpenRegister}
                    handleClickOpenLogin={handleClickOpenLogin}
                />

                <CustomLogin
                    openLogin={openLogin}
                    handleCloseLogin={handleCloseLogin}
                    Transition={Transition}
                    identifierLogin={identifierLogin}
                    handleChangeIdentifierLogin={handleChangeIdentifierLogin}
                    passwordLogin={passwordLogin}
                    handleChangePasswordLogin={handleChangePasswordLogin}
                    handleSendLogin={handleSendLogin}
                />

                <CustomRegister
                    openRegister={openRegister}
                    handleCloseRegister={handleCloseRegister}
                    Transition={Transition}
                    errorUsernameRegister={errorUsernameRegister}
                    usernameRegister={usernameRegister}
                    handleChangeUsernameRegister={handleChangeUsernameRegister}
                    errorPasswordRegister={errorPasswordRegister}
                    passwordRegister={passwordRegister}
                    handleChangePasswordRegister={handleChangePasswordRegister}
                    errorEmailRegister={errorEmailRegister}
                    emailRegister={emailRegister}
                    handleChangeEmailRegister={handleChangeEmailRegister}
                    errorPhoneCodeRegister={errorPhoneCodeRegister}
                    phoneCountryRegister={phoneCountryRegister}
                    handleChangePhoneCountry={handleChangePhoneCountry}
                    errorPhoneRegister={errorPhoneRegister}
                    phoneRegister={phoneRegister}
                    handleChangePhoneRegister={handleChangePhoneRegister}
                    errorNameRegister={errorNameRegister}
                    nameRegister={nameRegister}
                    handleChangeNameRegister={handleChangeNameRegister}
                    errorSurnameRegister={errorSurnameRegister}
                    surnameRegister={surnameRegister}
                    handleChangeSurnameRegister={handleChangeSurnameRegister}
                    addressRegister={addressRegister}
                    handleChangeAddressRegister={handleChangeAddressRegister}
                    errorCountryRegister={errorCountryRegister}
                    country={country}
                    handleChangeCountry={handleChangeCountry}
                    errorNationalityRegister={errorNationalityRegister}
                    nationality={nationality}
                    handleChangeNationality={handleChangeNationality}
                    dateRegister={dateRegister}
                    handleChangeDateRegister={handleChangeDateRegister}
                    errorDateRegister={errorDateRegister}
                    handleSendRegister={handleSendRegister}
                />
            </div>
        </header>
    );
}