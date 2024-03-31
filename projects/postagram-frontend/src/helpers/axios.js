import axios from "axios";
import createAuthRefreshInterceptor from "axios-auth-refresh";
import { getRefreshToken, getAccessToken } from "../hooks/user.actions";
const axiosService = axios.create({
    baseURL: "http://aldar.ilearn.mn/api",
    headers: {
        "Content-Type": "application/json",
    },
});

axiosService.interceptors.request.use(async (config) => {
    /**
    * Retrieving the access token from the localStorage
    and adding it to the headers of the request
    */
    config.headers.Authorization = `Bearer ${getAccessToken()}`;
    return config;
});

axiosService.interceptors.response.use(
    (res) => Promise.resolve(res),
    (err) => Promise.reject(err),
);

const refreshAuthLogic = async (failedRequest) => {
    return axios
        .post("/auth/refresh/",
            {
                refresh: getRefreshToken(),
            }, 
            {
            baseURL: "http://aldar.ilearn.mn/api/",
        })
        .then((resp) => {
            const { access, refresh, user } = resp.data;
            failedRequest.response.config.headers[
                "Authorization"] = "Bearer " + access;
            localStorage.setItem("auth", JSON.stringify({
                access, refresh, user
            }))
                .catch(() => {
                    localStorage.removeItem("auth");
                });
        });
};
createAuthRefreshInterceptor(axiosService,
    refreshAuthLogic);
export async function fetcher(url) {
    return axiosService.get(url).then((res) => res.data);
}
export default axiosService;