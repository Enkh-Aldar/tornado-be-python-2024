import React from "react";
import { Dropdown } from 'react-bootstrap';
import { getUser } from "../hooks/user.actions";

function NavigationBar() {
    const user = getUser();
    
    return (
        <nav className="bg-blue-600 border-gray-200 text-white py-2 px-4">
            <div className="flex flex-wrap items-center justify-between">
                <span className="text-2xl font-semibold dark:text-white p-2">Postagram</span>
                <div className="flex items-center ml-auto">
                    <img className="w-8 h-8 rounded-full" src={user.avatar} alt="user photo"/>
                    <Dropdown>
                        <Dropdown.Toggle variant="" id="dropdownUserAvatarButton" className="text-white mr-0">
                            <span className="sr-only">Open user menu</span>
                        </Dropdown.Toggle>
                        <Dropdown.Menu className="text-white">
                            <Dropdown.Item href="/profile">Profile</Dropdown.Item>
                            <Dropdown.Item href="/logout">Logout</Dropdown.Item>
                        </Dropdown.Menu>
                    </Dropdown>
                </div>
            </div>
        </nav>
    );
}

export default NavigationBar;
