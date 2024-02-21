import React, { useState } from "react";
import axios from "axios";

const Register = () => {
    

    return (
        <div className="mx-auto">
            <div className="my-5 text-center">
                <h1 className="text-blue-700 text-3xl">Welcome to Postagram!</h1>
                <p className="mt-10">This is a new social media site that will allow you to share your thoughts and experiences with your friends.</p>
                <p className="">Register now and start enjoying</p>
                <p className="">Or if you already have an account, please <a className="text-green-700 underline" href="#">login.</a></p>
            </div>
            <form action="" className="border-2 w-[512px] mx-auto bg-blue-100 rounded-lg">
                <div className="ml-10 mr-10">
                    <div className="mb-3">
                        <div className="mb-4 mt-10">
                            <label htmlFor="" className="">First Name </label>
                        </div>
                        <input type="text" className="first_name w-full py-3 rounded-lg" placeholder="  Enter first name" />
                    </div>
                    <div className="mb-3">
                        <div className="mb-4">
                            <label htmlFor="" className="">Last Name </label>
                        </div>
                        <input type="text" className="last_name w-full py-3 rounded-lg" placeholder="  Enter last name" />
                    </div>
                    <div className="mb-3">
                        <div className="mb-4">
                            <label htmlFor="" className="">Username </label>
                        </div>
                        <input type="text" className="username w-full py-3 rounded-lg" placeholder="  Enter username" />
                    </div>
                    <div className="mb-3">
                        <div className="mb-4 ">
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
                    <div className="mb-4">
                        <div>
                            <label htmlFor="">Bio</label>
                        </div>
                        <input type="text" className="bio w-full rounded-lg py-10" placeholder="  A simple bio ... (Optional)" />
                    </div>
                    <div className="mb-10">
                        <button type="submit" className="btn btn-primary px-7 py-3 rounded-lg border-2 bg-blue-600 text-white">
                            Register
                        </button>
                    </div>
                </div>

            </form>
        </div>
    )
}
export default Register;