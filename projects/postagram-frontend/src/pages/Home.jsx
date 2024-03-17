import React, { useEffect, useState } from "react";
import NavigationBar from "./NavigationBar";
import CreatePost from "../posts/CreatePost";
import { getUser } from "../hooks/user.actions";
import { fetcher } from "../helpers/axios";
import useSWR from 'swr'
import Post from "../posts/Post";
import Posts from "../posts/Posts";
import Comments from "../posts/comments/Comments";

function Home(post) {
    const user = getUser();
    const posts = useSWR("/post/", fetcher, {
        refreshInterval: 20000,
    });
    console.log(posts.data)
    // const comments = useSWR(`/post/${post.id}/comment/`, fetcher, {
    //     refreshInterval: 20000,
    // });
    // console.log(comments.data)

    const profiles = useSWR("/user/?limit=5", fetcher);


    return (
        <div>
            <NavigationBar />
            <main className="p-4 flex-grow grid grid-cols-4 gap-4">
                <div className="lg:col-span-3 col-span-4 flex flex-col space-y-3">
                    <div className="flex items-center border px-4 rounded-lg w-full gap-2">
                        <img src={user.avatar} className="w-10 h-10 rounded-full" alt="" />
                        <CreatePost refresh={posts.mutate} />
                    </div>
                    <Posts posts={posts.data} refresh={posts.mutate}/>
                    {/* <Comments comments={comments.data} refresh={comments.mutate} /> */}
                </div>

                <div className="lg:col-span-1 col-span-4 border rounded-lg p-4 flex flex-col space-y-3">
                    <div className="text-xl text-center text-blue-500 font-semibold">
                        Other profiles
                    </div>
                    {profiles.data?.results?.map((profile, index) => (
                        <ProfileCard key={index} user={profile} />
                    ))}
                </div>
            </main>
        </div>
    );
}

export default Home;
