import React, { useState } from 'react';
import { getUser } from '../hooks/user.actions';
import { useEffect } from 'react';
import axiosService from '../helpers/axios';
import axios from 'axios';
import Comments from './comments/Comments';
import Comment from './comments/Comment';

function Post({ post }) {
  const user = getUser();

  const [PostList, setPostList] = useState(post);


  const [likes, setLikes] = useState(post.likes || 0);



  const handleLike = async () => {
    try {
      const response = await axiosService.post(`/post/${post.id}/like/`);
      console.log(response.data)
      setLikes((prevLikes) => prevLikes + 1);
    } catch (error) {
      console.error('Error liking the post:', error);
    }
    setLikes((prevLikes) => prevLikes + 1);
  };

  return (
    <div className="w-full mx-auto my-4 border-1 rounded-lg p-4">
      <ul>
        <li className="">
          <div className='flex text-3xl'>
            <img src={user.avatar} className='w-14 h-14 border-2 border-indigo-700 rounded-full' alt="" />
            <div className='ml-3 mt-1 font-semibold'>
              {post.author.username}
            </div>
          </div>
          <div className=' py-3'>
            {post.body}
          </div>
          <div>
            <Comment post={post} />
            <div className="flex items-center space-x-4">
              <button onClick={handleLike} className="text-blue-500">Like</button>
              <span>{likes} Likes</span>
              <ul className="mt-4">
                <Comments />
              </ul>
            </div>
          </div>
        </li>
      </ul>
    </div>
  );
}

export default Post;
