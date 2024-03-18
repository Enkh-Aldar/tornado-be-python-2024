import React from "react";

function ProfileCard({ user }) {
    
    return (
        <div className="flex items-center space-x-2">
            <img src={user.avatar} className="w-8 h-8 rounded-full" alt={user.username} />
            <span>{user.username}</span>
        </div>
    );
}

export default ProfileCard;