
import React, { createContext, useState, useEffect } from 'react';
import { refreshAccessToken, setAccessToken } from '../hooks/user.actions';

const AuthContext = createContext();

const AuthProvider = ({ children }) => {
  const [accessToken, setAccessToken] = useState(null);

  useEffect(() => {
    const refreshAccessToken = async () => {
      try {
        const newAccessToken = await refreshToken();
        setAccessToken(newAccessToken);
      } catch (error) {
        console.error('Error refreshing token:', error);
        // Handle token refresh failure (e.g., log out user)
      }
    };

    const tokenExpirationTime = "";
    const tokenRefreshInterval = "";

    const refreshTimer = setTimeout(refreshAccessToken, tokenRefreshInterval);

    return () => clearTimeout(refreshTimer);
  }, [accessToken]);

  return (
    <AuthContext.Provider value={{ accessToken, setAccessToken }}>
      {children}
    </AuthContext.Provider>
  );
};

export { AuthProvider, AuthContext };
