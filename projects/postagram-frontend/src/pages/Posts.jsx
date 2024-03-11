import useSWR from "swr";
import { fetcher } from "../helpers/axios";
import Post from "./Post";

export default function Posts({posts}){
   
    console.log(posts)
    return (
        <div>
            {posts && posts.map((post, index) => <Post key={index} post={post}/>)}
        </div>

    );
}