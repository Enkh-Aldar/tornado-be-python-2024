import React, { useState } from "react";
import axios from "axios";

const Login = () => {
    return (
        <div className="mx-auto">
            <div className="my-5 text-center">
                <h1 className="text-blue-700 text-3xl">Welcome to Postagram!</h1>
                <p className="mt-10">Login now and start enjoying!</p>
                <p className="">Or if you do not have an account, please <a className="text-green-700 underline" href="#">register.</a></p>
            </div>
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
        </div>
    )
}
export default Login;