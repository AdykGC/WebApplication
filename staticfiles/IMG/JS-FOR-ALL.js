////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//-----------------------------------------------------------------------------------------------------FALSE--ERROR--TRUE-----------------------------------------------------------------------------------------------------//
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
function ERROR_CONTEINER_LP() {
    var Form_Container_LOGIN = document.querySelector('.CONTEINER-LP');
    Form_Container_LOGIN.classList.add('I_NIGHT_I');
    setTimeout(function () {
        Form_Container_LOGIN.classList.remove('I_NIGHT_I');
    }, 300);
}
function ERROR_CONTEINER_RP() {
    var Form_Container_REGISTER = document.querySelector('.CONTEINER-RP');
    Form_Container_REGISTER.classList.add('I_NIGHT_I');
    setTimeout(function () {
        Form_Container_REGISTER.classList.remove('I_NIGHT_I');
    }, 300);
}
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//------------------------------------------------------------------------------------------------------ZONA OCHUZHDENIE------------------------------------------------------------------------------------------------------//
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
function REMOVE_CONTEINER(){
    // GET
    var Form_Container_Username = document.querySelector('#USERNAME'), Form_Container_Password = document.querySelector('#PASSWORD');
    var Error_Username = document.getElementById('USERNAME-error'), Error_Password = document.getElementById('PASSWORD-error');
    var Correct_Username = document.getElementById('USERNAME-correct'), Correct_Password = document.getElementById('PASSWORD-correct');
    var I = "", II = '#160004', III = '#ff0000';
    // SET
    Form_Container_Username.style.backgroundColor = II, Form_Container_Username.style.borderColor = III;
    Form_Container_Password.style.backgroundColor = II, Form_Container_Password.style.borderColor = III;
    Error_Username.textContent = I, Error_Password.textContent = I;
    Correct_Username.textContent = I, Correct_Password.textContent = I;
}
function CORRECT_CONTEINER_USERNAME() {
    var Correct_Username = document.getElementById('USERNAME-correct'), Form_Container_Username = document.querySelector('#USERNAME'), I = 'Correct!', II = '#00ca1e', III = '#88ee81';
    Form_Container_Username.style.borderColor = II, Form_Container_Username.style.backgroundColor = III, Correct_Username.textContent = I;
}
function CORRECT_CONTEINER_PASSWORD() {
    var Correct_Password = document.getElementById('PASSWORD-correct'), Form_Container_Password = document.querySelector('#PASSWORD'), I = 'Correct', II = '#00ca1e', III = '#88ee81';
    Form_Container_Password.style.borderColor = II, Form_Container_Password.style.backgroundColor = III, Correct_Password.textContent = I;
}
function NULL_CONTEINER_USERNAME() {
    var Error_Username = document.getElementById('USERNAME-error'), Form_Container_Username = document.querySelector('#USERNAME'), I = 'WTF! Write your username!', II = '#ca0025', III = '#ee8181';
    Form_Container_Username.style.borderColor = II, Form_Container_Username.style.backgroundColor = III, Error_Username.textContent = I;
}
function NULL_CONTEINER_PASSWORD() {
    var Error_Password = document.getElementById('PASSWORD-error'), Form_Container_Password = document.querySelector('#PASSWORD'), I = 'WTF! Write your password!', II = '#ca0025', III = '#ee8181';
    Form_Container_Password.style.borderColor = II, Form_Container_Password.style.backgroundColor = III, Error_Password.textContent = I;
}
function FALSE_CONTEINER_USERNAME() {
    var Error_Username = document.getElementById('USERNAME-error'), Form_Container_Username = document.querySelector('#USERNAME'), I = 'Username must contain 8 characters or more!', II = '#ca0025', III = '#ee8181';
    Form_Container_Username.style.borderColor = II, Form_Container_Username.style.backgroundColor = III, Error_Username.textContent = I;
}
function FALSE_CONTEINER_PASSWORD() {
    var Error_Password = document.getElementById('PASSWORD-error'), Form_Container_Password = document.querySelector('#PASSWORD'), I = 'Password must contain 8 characters or more!', II = '#ca0025', III = '#ee8181';
    Form_Container_Password.style.borderColor = II, Form_Container_Password.style.backgroundColor = III, Error_Password.textContent = I;
}
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//------------------------------------------------------------------------------------------------------ZONA IF I STUPID------------------------------------------------------------------------------------------------------//
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
function loginUser() {
    var username = document.getElementById('USERNAME').value, password = document.getElementById('PASSWORD').value;

    // NULL NULL ERROR
    if (password.length === 0 && username.length === 0) {
        REMOVE_CONTEINER();
        ERROR_CONTEINER_LP();
        // RESULT
        NULL_CONTEINER_USERNAME();
        NULL_CONTEINER_PASSWORD();
        return;
    } 
    // NULL FALSE ERROR
    else if (password.length === 0 && username.length >= 1 && username.length < 8) {
        REMOVE_CONTEINER();
        ERROR_CONTEINER_LP();
        // RESULT
        FALSE_CONTEINER_USERNAME();
        NULL_CONTEINER_PASSWORD();
    } 
    // FALSE NULL ERROR
    else if (password.length >= 1 && password.length < 8 && username.length === 0) {
        REMOVE_CONTEINER();
        ERROR_CONTEINER_LP();
        // RESULT
        NULL_CONTEINER_USERNAME();
        FALSE_CONTEINER_PASSWORD();
    } 
    // NULL TRUE ERROR
    else if (password.length === 0 && username.length >= 8) {
        REMOVE_CONTEINER();
        ERROR_CONTEINER_LP();
        // RESULT
        CORRECT_CONTEINER_USERNAME();
        NULL_CONTEINER_PASSWORD();
    } 
    // TRUE NULL ERROR
    else if (password.length >= 8 && username.length === 0) {
        REMOVE_CONTEINER();
        ERROR_CONTEINER_LP();
        // RESULT
        NULL_CONTEINER_USERNAME();
        CORRECT_CONTEINER_PASSWORD();
    } 
    // TRUE FALSE FALSE
    else if (password.length >= 8 && username.length >= 1 && username.length < 8) {
        REMOVE_CONTEINER();
        ERROR_CONTEINER_LP();
        // RESULT
        FALSE_CONTEINER_USERNAME();
        CORRECT_CONTEINER_PASSWORD();
    }
    // FALSE TRUE FALSE
    else if (password.length >= 1 && password.length < 8 && username.length >= 8) {
        REMOVE_CONTEINER();
        ERROR_CONTEINER_LP();
        // RESULT
        CORRECT_CONTEINER_USERNAME();
        FALSE_CONTEINER_PASSWORD();
        return;
    }
    // TRUE TRUE TRUE
    else if (password.length >= 8 && username.length >= 8) {
        REMOVE_CONTEINER();
        ERROR_CONTEINER_LP();
        // RESULT
        CORRECT_CONTEINER_USERNAME();
        CORRECT_CONTEINER_PASSWORD();
        // NEW WINDOW
    }
    // FALSE FALSE FALSE
    else if (password.length >= 1 && password.length < 8 && username.length >= 1 && username.length < 8) {
        REMOVE_CONTEINER();
        ERROR_CONTEINER_LP();
        // RESULT
        FALSE_CONTEINER_USERNAME();
        FALSE_CONTEINER_PASSWORD();
        return;
    }
}

function registerUser() {
    var username = document.getElementById('USERNAME').value, password = document.getElementById('PASSWORD').value;

    // NULL NULL ERROR
    if (password.length === 0 && username.length === 0) {
        REMOVE_CONTEINER();
        ERROR_CONTEINER_RP();
        // RESULT
        NULL_CONTEINER_USERNAME();
        NULL_CONTEINER_PASSWORD();
        return;
    } 
    // NULL FALSE ERROR
    else if (password.length === 0 && username.length >= 1 && username.length < 8) {
        REMOVE_CONTEINER();
        ERROR_CONTEINER_RP();
        // RESULT
        FALSE_CONTEINER_USERNAME();
        NULL_CONTEINER_PASSWORD();
    } 
    // FALSE NULL ERROR
    else if (password.length >= 1 && password.length < 8 && username.length === 0) {
        REMOVE_CONTEINER();
        ERROR_CONTEINER_RP();
        // RESULT
        NULL_CONTEINER_USERNAME();
        FALSE_CONTEINER_PASSWORD();
    } 
    // NULL TRUE ERROR
    else if (password.length === 0 && username.length >= 8) {
        REMOVE_CONTEINER();
        ERROR_CONTEINER_RP();
        // RESULT
        CORRECT_CONTEINER_USERNAME();
        NULL_CONTEINER_PASSWORD();
    } 
    // TRUE NULL ERROR
    else if (password.length >= 8 && username.length === 0) {
        REMOVE_CONTEINER();
        ERROR_CONTEINER_RP();
        // RESULT
        NULL_CONTEINER_USERNAME();
        CORRECT_CONTEINER_PASSWORD();
    } 
    // TRUE FALSE FALSE
    else if (password.length >= 8 && username.length >= 1 && username.length < 8) {
        REMOVE_CONTEINER();
        ERROR_CONTEINER_RP();
        // RESULT
        FALSE_CONTEINER_USERNAME();
        CORRECT_CONTEINER_PASSWORD();
    }
    // FALSE TRUE FALSE
    else if (password.length >= 1 && password.length < 8 && username.length >= 8) {
        REMOVE_CONTEINER();
        ERROR_CONTEINER_RP();
        // RESULT
        CORRECT_CONTEINER_USERNAME();
        FALSE_CONTEINER_PASSWORD();
        return;
    }
    // TRUE TRUE TRUE
    else if (password.length >= 8 && username.length >= 8) {
        REMOVE_CONTEINER();
        ERROR_CONTEINER_RP();
        // RESULT
        CORRECT_CONTEINER_USERNAME();
        CORRECT_CONTEINER_PASSWORD();
        // NEW WINDOW
        setTimeout(function () {
            window.location.href = 'NAVBAR.html';
            // 1000 ms = 1s 
        }, 1000);
    }
    // FALSE FALSE FALSE
    else if (password.length >= 1 && password.length < 8 && username.length >= 1 && username.length < 8) {
        REMOVE_CONTEINER();
        ERROR_CONTEINER_RP();
        // RESULT
        FALSE_CONTEINER_USERNAME();
        FALSE_CONTEINER_PASSWORD();
        return;
    }
}
