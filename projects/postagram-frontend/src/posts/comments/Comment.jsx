import React, { useState } from "react";
import axiosService from "../../helpers/axios";
import { getUser } from "../../hooks/user.actions";

function Comment({ post }) {
    const [comments, setComments] = useState(post.comments || []);
    const [newComment, setNewComment] = useState('');
    const user = getUser();

    const handleCommentSubmit = async () => {
        try {
            if (!post.id) {
                console.error('Post ID is undefined.');
                return;
            }
            const newCommentObj = {
                author: user.id,
                body: newComment,
                post: post.id
            };

            const response = await axiosService.post(`/post/${post.id}/comment/`, {
                body: newCommentObj,
            });

            console.log('Comment created successfully:', response.data);

            // Add the new comment to the comment list
            setComments([...comments, newCommentObj]);

            setNewComment('');
        } catch (error) {
            console.error('Error submitting comment:', error);
        }
    };

    return (
        <div className="mt-4">
            <div className="comment-list">
                {comments.map((comment, index) => (
                    <div key={index} className="comment">
                        <p>Author: {comment.author} {comment.body}</p>
                    </div>
                ))}
            </div>
            <textarea
                value={newComment}
                onChange={(e) => setNewComment(e.target.value)}
                placeholder="Add a comment"
                className="w-full border p-2 rounded-md"
            />
            <button onClick={handleCommentSubmit} className="mt-2 bg-blue-500 text-white px-4 py-2 rounded-md">
                Comment
            </button>
        </div>
    );
}

export default Comment;
