import { Routes, Route } from "react-router-dom";
import './index.css'
import Login from "./components/Login";
import Register from "./components/Register";
import { useEffect } from "react";
import axios from "axios";

function App() {
  const fetchData = async () => {
    const bodyData = 
      {
        "username": "mouse21",
        "first_name": "Mickey",
        "last_name": "Mouse",
        "password": "12345678",
        "email": "mouse@yopmail.com"
      }
      
    const response = await axios.post("http://127.0.0.1:8000/api/auth/register/", bodyData);
    console.log(response)
    const jsonData = await response.data
    setData(jsonData)
    console.error('Error Fetching Data;', error)
  }
  useEffect(() => {
    fetchData()
  }, []);
  return (
    <div>

      < Register />
    </div>
  )
}

export default App;
