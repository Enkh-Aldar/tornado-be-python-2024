import React, { useEffect, useState } from "react";
import NavigationBar from "./NavigationBar";
import CreatePost from "./CreatePost";

function Home() {
    const [data, setData] = useState([]);
    useEffect(() => {

        const fetchData = async () => {
            const result = await fetch("http://127.0.0.1:8000/api/post");
            const json = await result.json();
            setData(json);
            console.log(json);
        };
        fetchData();

    }, []);


    return (
        <div>
            <NavigationBar />
            <div>
                <CreatePost />
            </div>
            <h1>Profile</h1>
            <h1>HOME</h1>
            
            {data.length === 0 ? (
                <div>Loading</div>
            ) : (
                data.map((d, index) => (
                    <div key={index} className="text-3xl text-green-700">
                        {[d.body]} {[d.author.username]}
                    </div>
                ))
            )}
        </div>
    );
}
export default Home;