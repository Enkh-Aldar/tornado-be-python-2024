import axios from "axios";
import { useNavigate } from "react-router-dom";

function useUserActions() {
    const navigate = useNavigate();
    const baseURL = "https://aldar.ilearn.mn/api";
    return {
        login,
        register,
        logout,
    };

    // Login the user
    function login(data) {
        return axios.post(`${baseURL}/auth/login/`,
            data).then((res) => {
                // Registering the account and tokens in the
                // store
                setUserData(res.data);
                navigate("/");
            });
    }
    // Logout the user
    function logout() {
        localStorage.removeItem("auth");
        navigate("/login");
    }
    function register(data) {
        return axios.post(`${baseURL}/auth/register/`, data).then((res) => {
                // Registering the account and tokens in the
                // store
                setUserData(res.data);
                navigate("/");
            });
            
    }
}
// Get the user
function getUser() {
    const auth =
        JSON.parse(localStorage.getItem("auth"));
    return auth?.user;
}
// Get the access token
function getAccessToken() {
    const auth =
        JSON.parse(localStorage.getItem("auth"));
    return auth?.access;
}
// Get the refresh token
function getRefreshToken() {
    const auth =
        JSON.parse(localStorage.getItem("auth"));
    return auth?.refresh;
}
// Set the access, token and user property

function setUserData(data) {
    console.log(data)
    localStorage.setItem(
        "auth",
        JSON.stringify({
            access: data.access,
            refresh: data.refresh,
            user: data.user,
        })
    );
}
async function refreshAccessToken(refreshToken) {
    try {
        const res = await axios.post(`${baseURL}/auth/refresh/`, { refresh: refreshToken });
        setAccessToken(res.data.access);
        return res.data.access;
    } catch (error) {
        console.error("Error refreshing access token:", error);
        throw error;
    }
}

// Function to set access token in local storage
function setAccessToken(accessToken) {
    const authData = JSON.parse(localStorage.getItem("auth"));
    localStorage.setItem(
        "auth",
        JSON.stringify({
            ...authData,
            access: accessToken
        })
    );
}
export {useUserActions, getAccessToken, getRefreshToken, getUser, setAccessToken, refreshAccessToken};