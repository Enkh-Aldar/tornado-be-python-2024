import React, { useState } from "react";
import { Form, Button } from "react-bootstrap";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import { useUserActions } from "../../hooks/user.actions.js";

function LoginForm() {
    
    const navigate = useNavigate();
    const [validated, setValidated] = useState(false);
    const [form, setForm] = useState({});
    const [error, setError] = useState(null);
    const userActions = useUserActions();

    const handleSubmit = (event) => {
        event.preventDefault();
        const loginForm = event.currentTarget;
        if (loginForm.checkValidity() === false) {
            event.stopPropagation();
        }
        setValidated(true);
        const data = {
            username: form.username,
            password: form.password,
        };
        axios.post("http://localhost:8000/api/auth/login/",
            data)
            .then((res) => {
                // Registering the account and tokens in the
                // store
                localStorage.setItem("auth", JSON.stringify({
                    access: res.data.access,
                    refresh: res.data.refresh,
                    user: res.data.user,
                }));
                navigate("/");
            })
            .catch((err) => {
                if (err.message) {
                    setError(err.request.response);
                }
            });
    };
    return (
        <form action="" className="border-2 w-[512px] mx-auto bg-blue-100 rounded-lg">
                <div className="ml-10 mr-10">
                    <div className="mb-3">
                        <div className="mb-4 mt-10">
                            <label htmlFor="" className="">Email address </label>
                        </div>
                        <input type="email" className="email w-full py-3 rounded-lg" placeholder="  Enter email" />
                    </div>
                    <div className="mb-3">
                        <div className="mb-4 mt-4">
                            <label htmlFor="">Password </label>
                        </div>

                        <input type="password" className="password w-full py-3 rounded-lg" placeholder="  Enter password" />
                    </div>
                    <div className="mb-3">
                        <div className="custom-control custom-checkbox">
                            <input type="checkbox" className="custom-control-input" id="customCheck1" />

                            <label htmlFor="customCheck1" className="custom-control-label">Remember me</label>
                        </div>
                    </div>
                    <div className="mb-10">
                        <button type="submit" className="btn btn-primary px-7 py-3 rounded-lg border-2 bg-blue-600 text-white">
                            Login
                        </button>
                    </div>
                </div>
            </form>
    );
}
export default LoginForm;