import React, { useState } from "react";
import { Form, Button } from "react-bootstrap";
import axios from "axios";
import { useNavigate } from "react-router-dom";

function RegistrationForm() {
    const navigate = useNavigate();
    const [validated, setValidated] = useState(false);
    const [form, setForm] = useState({});
    const [error, setError] = useState(null);
    const handleSubmit = (event) => {
        event.preventDefault();
        const registrationForm = event.currentTarget;
        if (registrationForm.checkValidity() === false) {
            event.stopPropagation();
        }
        setValidated(true);
        const data = {
            username: form.username,
            password: form.password,
            email: form.email,
            first_name: form.first_name,
            last_name: form.last_name,
            bio: form.bio,
        };
        axios.post("http://localhost:8000/api/auth/register/",
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
        <form action="" className="form-horizontal border-2 w-[512px] mx-auto bg-blue-100 rounded-lg">
                <div className="ml-10 mr-10">
                    <div className="form-group mb-3">
                        <div className="mb-4 mt-10">
                            <label htmlFor="" className="">First Name </label>
                        </div>
                        <input type="text" className="first_name w-full py-3 rounded-lg" placeholder="  Enter first name" />
                    </div>
                    <div className="form-group mb-3">
                        <div className="mb-4">
                            <label htmlFor="" className="">Last Name </label>
                        </div>
                        <input type="text" className="last_name w-full py-3 rounded-lg" placeholder="  Enter last name" />
                    </div>
                    <div className="form-group mb-3">
                        <div className="mb-4">
                            <label htmlFor="" className="">Username </label>
                        </div>
                        <input type="text" className="username w-full py-3 rounded-lg" placeholder="  Enter username" />
                    </div>
                    <div className="form-group mb-3">
                        <div className="mb-4 ">
                            <label htmlFor="" className="">Email address </label>
                        </div>
                        <input type="email" className="email w-full py-3 rounded-lg" placeholder="  Enter email" />
                    </div>
                    <div className="form-group mb-3">
                        <div className="mb-4 mt-4">
                            <label htmlFor="">Password </label>
                        </div>

                        <input type="password" className="password w-full py-3 rounded-lg" placeholder="  Enter password" />
                    </div>
                    <div className="form-group mb-4">
                        <div>
                            <label htmlFor="">Bio</label>
                        </div>
                        <input type="text" className="bio w-full rounded-lg py-10" placeholder="  A simple bio ... (Optional)" />
                    </div>
                    <div className="form-group mb-10">
                        <button type="submit" className="btn btn-primary px-7 py-3 rounded-lg border-2 bg-blue-600 text-white">
                            Register
                        </button>
                    </div>
                </div>

            </form>
    );
}
export default RegistrationForm;