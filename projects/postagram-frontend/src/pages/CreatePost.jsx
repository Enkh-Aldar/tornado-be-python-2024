import React, { useState } from "react";
import { getUser } from "../hooks/user.actions";
import axiosService from "../helpers/axios";

function CreatePost({refresh}) {

    const [form, setForm] = useState("");
    const [toastMessage, setToastMessage] = useState("");
    const [toastType, setToastType] = useState("");
    const user = getUser();

    const handleClose = () => {
        // Implement your handleClose logic here
    };


    const handlePost = () => {
        // Define the data for the post request
        const data = {
            author: user.id,
            body: form, // Assuming your data structure includes a 'message' field
            // Add other necessary fields for the post request
        };

        axiosService
            .post("/post/", data)
            .then((response) => {

                const responseData = response.data;

                handleClose();
                setToastMessage("Post Created.");
                setToastType("success");
                setForm("");
                refresh();

                console.log("Response data", responseData);
            })
            .catch(() => {
                setToastMessage("An error occurred.");
                setToastType("danger");
            });
    };

    return (
        <div className="mt-4 w-full mr-6 border-gray-200 py-4 rounded-2xl">
            <textarea
                id="message"
                rows="4"
                className="border-2 border-indigo-700 ml-4 pl-4 py-1 w-full rounded-full placeholder-blue-700"
                placeholder="Write a post"
                value={form}
                onChange={(e) => setForm(e.target.value)}
            ></textarea>
            <button onClick={handlePost}>Post</button>
        </div>
    );
}

export default CreatePost;
