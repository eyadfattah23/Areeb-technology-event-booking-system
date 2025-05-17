document.querySelector('.img__btn').addEventListener('click', function () {
    document.querySelector('.cont').classList.toggle('s--signup');
});
document.querySelector('#signin-form input[type="email"]').focus();

const loginForm = document.getElementById('signin-form');
const signupForm = document.getElementById('signup-form');
const baseEndpoint = "http://localhost:8000/auth";
if (loginForm)
    loginForm.addEventListener('submit', handleLogin);

if (signupForm)
    signupForm.addEventListener('submit', handleSignup);
function handleLogin(event) {
    event.preventDefault();
    const submitButton = event.target.querySelector('button[type="submit"]');
    submitButton.disabled = true;
    submitButton.textContent = 'Processing...';

    const loginEndpoint = `${baseEndpoint}/jwt/create/`;
    let loginFormData = new FormData(loginForm);
    let loginObjectData = Object.fromEntries(loginFormData);
    let bodyStr = JSON.stringify(loginObjectData);

    const options = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: bodyStr,
    };

    fetch(loginEndpoint, options)
        .then(response => {
            if (!response.ok) {
                return response.json().then(err => { throw err; });
            }
            return response.json();
        })
        .then(data => {
            console.log(data);

            localStorage.setItem('access', data.access);
            localStorage.setItem('refresh', data.refresh);

            window.addEventListener('beforeunload', () => {
                if (!window.location.href.includes('/events')) {
                    localStorage.removeItem('access');
                    localStorage.removeItem('refresh');
                }
            });

            window.location.href = '/events';
        })
        .catch(error => {
            alert(error.detail || Object.values(error)[0] || 'Login failed');
        }).finally(() => {
            if (submitButton) {
                submitButton.disabled = false;
                submitButton.textContent = 'Sign In';
            }
        });

}

function handleSignup(event) {
    event.preventDefault();

    const submitButton = event.target.querySelector('button[type="submit"]');
    submitButton.disabled = true;
    submitButton.textContent = 'Processing...';


    const signupEndpoint = `${baseEndpoint}/users/`;
    let signupFormData = new FormData(signupForm);
    let signupObjectData = Object.fromEntries(signupFormData);

    if (signupObjectData.password !== signupObjectData.re_password) {
        alert("Passwords don't match!");
        submitButton.disabled = false;
        submitButton.textContent = 'Sign Up';
        return;
    }

    let bodyStr = JSON.stringify(signupObjectData);
    const options = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: bodyStr,
    };
    fetch(signupEndpoint, options)
        .then(response => {
            if (!response.ok) {
                return response.json().then(err => { throw err; });
            }
            return response.json();
        })
        .then(data => {
            console.log(data);
            alert('Signup successful! Please log in.');
            document.querySelector('.cont').classList.toggle('s--signup');
        })
        .catch(error => {
            console.error('Error:', error);
            alert(
                error.detail ||
                Object.values(error)[0]?.toString() ||
                'Signup failed. Please check your details.'
            );
        }).finally(() => {
            if (submitButton) {
                submitButton.disabled = false;
                submitButton.textContent = 'Sign Up';
            }
        });

}
