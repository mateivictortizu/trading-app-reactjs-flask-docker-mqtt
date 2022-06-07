export function checkIsValidUsername(fieldUsername) {

    if (fieldUsername.match(/^[a-zA-Z][a-zA-Z0-9]{7,20}$/)) {
        return true;
    }
    else {
        return false;
    }
}

export function checkIsValidPassword(fieldPassword) {

    if (fieldPassword.match(/^(?=.*\d)(?=.*[!@#$%^&*])(?=.*[a-z])(?=.*[A-Z])[0-9a-zA-Z!@#$%^&*]{8,}$/)) {
        return true;
    }
    else {
        return false;
    }
}

export function checkIsValidEmail(fieldEmail) {

    if (fieldEmail.match(/^(([^<>()[\]\.,;:\s@\"]+(\.[^<>()[\]\.,;:\s@\"]+)*)|(\".+\"))@(([^<>()[\]\.,;:\s@\"]+\.)+[^<>()[\]\.,;:\s@\"]{2,})$/)) {
        return true;
    }
    else {
        return false;
    }
}

export function checkIsValidPhone(fieldPhone) {
    if (fieldPhone.match(/^[0-9]{8,12}$/)) {
        return true;
    }
    else {
        return false;
    }
}

export function checkIsValidName(fieldName) {
    if (fieldName.match(/^[a-zA-Z][a-zA-Z'-]+[a-zA-Z]$/)) {
        return true;
    }
    else {
        return false;
    }
}

export function checkIsValidCountry(fieldCountry) {
    if (fieldCountry.match(/^[A-Z]{1,3}$/)) {
        return true;
    }
    else {
        return false;
    }
}

export function checkIsValidNationality(fieldNationality) {
    if (fieldNationality.match(/^[A-Z]{1,3}$/)) {
        return true;
    }
    else {
        return false;
    }
}

export function checkIsValidCountryCode(fieldCountryCode) {
    if (fieldCountryCode.match(/^[0-9]{1,3}$/)) {
        return true;
    }
    else {
        return false;
    }
}

export function checkIsValidSurname(fieldSurname) {
    if (fieldSurname.match(/^[a-zA-Z][a-zA-Z'-]+[a-zA-Z]$/)) {
        return true;
    }
    else {
        return false;
    }
}

export function checkIsEmpty(field) {
    if (field.length == 0) {
        return false;
    }
    return true;
}

export function checkIsValidDate(fieldDate) {
    var today = new Date();
    var birthDate = fieldDate;
    var age = today.getFullYear() - fieldDate.getFullYear();
    var m = today.getMonth() - birthDate.getMonth();
    if (m < 0 || (m === 0 && today.getDate() < birthDate.getDate())) {
        age--;
    }
    if (age < 18) {
        return false;
    }
    else {
        return true;
    }

}