import React, { useState } from "react";
import { Link } from "react-router-dom";
import axios from "axios";
import RegistrationForm from "../components/authentication/RegistrationForm";

function Register() {

    return (
        <div className="container">
            <div className="mx-auto">
                <div className="my-5 text-center">
                    <h1 className="text-blue-700 text-3xl">Welcome to Postagram!</h1>
                    <p className="mt-10">This is a new social media site that will allow you to share your thoughts and experiences with your friends.</p>
                    <p className="">Register now and start enjoying</p>
                    <p className="">Or if you already have an account, please {" "} <Link to="/login/"> login</Link>.</p>
                </div>
            </div>
            <div className="col-md-6 p-5 mx-auto">
                <RegistrationForm />
            </div>
        </div>
    );
}
export default Register;