import React, { useState } from "react";
import axiosService from "../../helpers/axios";
import { getUser } from "../../hooks/user.actions";
import useSWR from "swr"; // Import useSWR
import { fetcher } from "../../helpers/axios";

function Comment({ post }) {
    const [newComment, setNewComment] = useState('');
    const user = getUser();

    // Fetch comments using useSWR
    const { data: comments, error } = useSWR(`/post/${post.id}/comment/`, fetcher, async () => {
        const response = await axiosService.get(`/post/${post.id}/comment/`);
        return response.data;
    });

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

            // Automatically update comments when a new comment is posted
            setNewComment('');
        } catch (error) {
            console.error('Error submitting comment:', error);
        }
    };

    if (error) return <div>Error fetching comments</div>;
    if (!comments) return <div>Loading...</div>;

    return (
        <div className="mt-4">
            <div className="comment-list">
                {comments.map((comment, index) => (
                    <div key={index} className="comment">
                        <div className="flex align-middle items-center">
                        <p><img src={user.avatar} className="w-8 h-8" alt="" />
                        </p>
                        <p className="ml-3 text-2xl"> {comment.author.username}</p>
                        </div>
                        <div>
                            <p className=" text-xl">{comment.body}</p>
                        </div>
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
