import React from "react";

const Logout = () => {
  const handleLogout = () => {
    // Perform any necessary logout actions here
    // For example, clear user session, remove tokens, etc.

    // Redirect to the login page after logout
    window.location.href = "/login";
  };

  return (
    <div>
      <h2>Logout</h2>
      <p>Are you sure you want to logout?</p>
      <button onClick={handleLogout}>Logout</button>
    </div>
  );
};

export default Logout;
