export function getAccessToken() {
    return localStorage.getItem('access_token');
}

export async function refreshToken() {
    const refresh = localStorage.getItem('refresh_token');
    const response = await fetch('http://localhost:8000/auth/jwt/refresh/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ refresh }),
    });
    const data = await response.json();
    localStorage.setItem('access_token', data.access);
    return data.access;
}

export function isAuthenticated() {
    return !!getAccessToken();
}
