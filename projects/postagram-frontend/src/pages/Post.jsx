import React, { useState } from 'react';
import Comment from './Comment';
import { getUser } from '../hooks/user.actions';
import { useEffect } from 'react';

function Post({ post }) {

  const user = getUser();

  return (
    <div className="w-full mx-auto my-4 border-1 rounded-lg p-4">
      <ul>
        <li className="">
          <div className='flex text-3xl'>
            <img src={user.avatar} className='w-8 h-8' alt="" />
            {post.author.username}
          </div>
          {post.body}
        </li>

      </ul>
    </div>
  );
};

export default Post;
