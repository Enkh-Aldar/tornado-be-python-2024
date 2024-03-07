import React from "react";
import { getUser } from "../hooks/user.actions";

function CreatePost() {

    const user = getUser();

    return (
        <div className="flex mt-4 w-9/12 border-2 border-gray-200 py-4 rounded-2xl">
            <img className="rounded-full w-8 h-8 ml-4 mt-1" src={user.avatar} alt="" />
            <textarea id="message" rows="4" class="border-2 border-indigo-700 ml-4 pl-4 py-1 w-7/12 rounded-full placeholder-blue-700" placeholder="Write a post"></textarea>
        </div>

    )
}
export default CreatePost;