// src/components/Comment.js
import React from 'react';

const Comment = ({ comment }) => (
  <li className="mb-2">
    <span className="font-semibold">{comment.user}</span>
    <span className="text-gray-500">{comment.createdAt}</span>
    <p>{comment.content}</p>
  </li>
);

export default Comment;
