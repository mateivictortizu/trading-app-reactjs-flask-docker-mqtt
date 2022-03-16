export function checkIsValidUsername(fieldUsername){
    
    return false;
}

export function checkIsValidPassword (fieldPassword) {
        
    if(fieldPassword.match(/^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])[0-9a-zA-Z]{8,}$/))
    {
        return true;
    }
    else
    {
        return false;
    }
}

export function checkIsValidEmail(fieldEmail){
    
    if(fieldEmail.match(  /^(([^<>()[\]\.,;:\s@\"]+(\.[^<>()[\]\.,;:\s@\"]+)*)|(\".+\"))@(([^<>()[\]\.,;:\s@\"]+\.)+[^<>()[\]\.,;:\s@\"]{2,})$/))
    {
        return true;
    }
    else
    {
        return false;
    }
}

export function checkIsValidPhone(fieldPhone){
    
    return false;
}

export function checkIsValidName(fieldName){
    
    return false;
}

export function checkIsValidSurname(fieldSurname){
    
    return false;
}

export function checkIsValidDate(fieldDate){
    
    return false;
}