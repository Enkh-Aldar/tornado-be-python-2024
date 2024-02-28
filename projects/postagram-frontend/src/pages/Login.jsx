import React from "react";
import { Link } from "react-router-dom";
import LoginForm from "../components/authentication/LoginForm";
const Login = () => {
    return (
        <div className="container">
            <div className="my-5 text-center">
                <h1 className="text-blue-700 text-3xl">Welcome to Postagram!</h1>
                <p className="mt-10">Login now and start enjoying!</p>
                <p className="">Or if you do not have an account, please please {" "} <Link to="/register/"> register</Link>.</p>
            </div>
            <div className="col-md-6 p-5 mx-auto">
                <LoginForm />
            </div>
        </div>
    );
}
export default Login;