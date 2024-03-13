import { useState } from "react";
import axiosService from "../../helpers/axios";

function Comment({ post }) {
    const [comments, setComments] = useState(post.comments || []);
    const [newComment, setNewComment] = useState('');

    const handleCommentSubmit = async () => {
        try {
            if (!post.id) {
                console.error('Post ID is undefined.');
                return;
            }

            const response = await axiosService.post(`/post/${post.id}/comment/`, {
                content: newComment,
            });

            console.log('Comment created successfully:', response.data);

            const newCommentObj = {
                user: user.username,
                content: newComment,
                createdAt: response.data.createdAt,
            };

            setComments((prevComments) => [...prevComments, newCommentObj]);
            setNewComment('');
        } catch (error) {
            console.error('Error submitting comment:', error);
        }
    };

    return (
        <div className="mt-4">
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
