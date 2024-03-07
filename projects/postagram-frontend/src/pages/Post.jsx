// src/components/Post.js
import React, { useState } from 'react';
import Comment from './Comment';

const Post = ({ post }) => {
  const [likes, setLikes] = useState(post.likes);
  const [comment, setComment] = useState('');
  const [comments, setComments] = useState(post.comments);

  const handleLike = () => {
    // Implement your like functionality here (e.g., using an API)
    // For simplicity, we'll just update the local state.
    setLikes(likes + 1);
  };

  const handleComment = () => {
    // Implement your comment functionality here (e.g., using an API)
    // For simplicity, we'll just update the local state.
    setComments([...comments, { user: 'Current User', content: comment }]);
    setComment('');
  };

  return (
    <div className="max-w-xl mx-auto my-4 bg-white shadow-md rounded-md p-4">
      <div className="flex items-center mb-4">
        <img src="path/to/user-avatar.jpg" alt="User Avatar" className="w-10 h-10 rounded-full mr-2" />
        <div>
          <p className="font-semibold">{post.user}</p>
          <p className="text-gray-500 text-sm">{post.createdAt}</p>
        </div>
      </div>
      <p className="mb-4">{post.content}</p>

      <div className="flex items-center space-x-2">
        <button onClick={handleLike} className="text-blue-500">Like</button>
        <span className="text-gray-500">·</span>
        <span>Likes: {likes}</span>
      </div>

      <div className="mt-4">
        <textarea
          value={comment}
          onChange={(e) => setComment(e.target.value)}
          placeholder="Add a comment"
          className="w-full border p-2 rounded-md"
        />
        <button onClick={handleComment} className="mt-2 bg-blue-500 text-white px-4 py-2 rounded-md">Comment</button>
      </div>

      <ul className="mt-4">
        {comments.map((comment, index) => (
          <Comment key={index} comment={comment} />
        ))}
      </ul>
    </div>
  );
};

export default Post;
