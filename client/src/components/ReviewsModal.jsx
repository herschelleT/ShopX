import React, { useState, useEffect } from 'react';
import './Modal.css';
import axios from "../api/axios"
import { useSelector } from "react-redux";

const Modal = ({ isOpen, onClose, id, children }) => {
  if (!isOpen) return null; // Render nothing if modal is not open
  const userInfo = useSelector((state) => state.user.userInfo);
	const [reviews, setReviews] = useState([]);
  const [averageRating, setAverageRating] = useState(null);

  const [reviewText, setReviewText] = useState("");
  const [rating, setRating] = useState("");

  const handlePostReview = () => {
    if (!reviewText || !rating) {
      alert("Please enter both a review and rating.");
      return;
    }
    // user_id=review.user_id,
    //     phone_id=review.phone_id,
    //     laptop_id=review.laptop_id,
    //     rating=review.rating,
    //     text=review.text
    // Create a new review object
    const newReview = {
      text: reviewText,
      rating: parseFloat(rating),
      user_id: userInfo.user_id, // replace with the user's email or ID
      phone_id: id
    };

    // Call the onPostReview function to handle submission
    //onPostReview(newReview);
    axios.post('/reviews', newReview).then((res) => {
      const newReview = {
        id: res.data.id,
        content: res.data.text,
        phone_id: res.data.phone_id,
        user_email: userInfo.user_email

      }
      console.log(res.data);
      
      setReviews((prev) => [...prev, newReview])
    })

    // Clear the inputs after posting
    setReviewText("");
    setRating(0);
  };

	useEffect(() => {
    const fetchReviews = async () => {
      try {
        const response = await axios.get('/reviews', {params: {phone_id: id}}); // Replace with actual API endpoint
        const reviewsData = response.data;
				console.log(reviewsData);
				
        setReviews(reviewsData);

        // Calculate the average rating
        const totalRating = reviewsData.reduce((sum, review) => sum + review.rating, 0);
        const avgRating = (totalRating / reviewsData.length).toFixed(1); // Rounded to 1 decimal place
        setAverageRating(avgRating);

      } catch (error) {
        console.error("Error fetching reviews:", error);
      }
    };

    if (isOpen) {
      fetchReviews();
    }
  }, [isOpen]);

  return (
    <div className="modal-overlay" onClick={onClose}>
  <div
    className="modal-content p-4 border border-secondary rounded"
    onClick={(e) => e.stopPropagation()}
    style={{
      maxWidth: "600px", // Limit the max width of the modal
      maxHeight: "80vh", // Limit the max height of the modal
      overflowY: "auto", // Allow scrolling if the content exceeds the modal height
    }}
  >
    <button
  className="modal-close btn-close"
  onClick={onClose}
  aria-label="Close"
  style={{ fontSize: "1.5rem", lineHeight: "1" }} // Optional style to make "X" larger
>
  &times;
</button>


    <h2>Customer Reviews</h2>
    {averageRating && <p>Average Rating: {averageRating} / 5</p>}

    <ul
      className="list-unstyled"
      style={{
        maxHeight: "200px", // Set a max height for the reviews section
        overflowY: "auto", // Enable vertical scrolling for the reviews
      }}
    >
      {reviews.map((review, index) => (
        <li key={index} className="mb-3">
          <p>
            <strong>{review.user_email}:</strong> {review.content}
          </p>
          <p>Rating: {review.rating} / 5</p>
        </li>
      ))}
    </ul>

    <hr className="my-4" />

    <h3 className="d-flex align-items-center mb-3">
      Leave a Review
      <span className="ms-3 text-muted">Add Rating (1-5)</span>
    </h3>
    <div className="d-flex align-items-center">
      <input
        type="number"
        value={rating}
        onChange={(e) => setRating(e.target.value)}
        placeholder="Rating (1-5)"
        min="1"
        max="5"
        className="form-control border border-secondary rounded"
        style={{ width: "50px" }}
      />
    </div>

    <textarea
      value={reviewText}
      onChange={(e) => setReviewText(e.target.value)}
      placeholder="Write your review here"
      className="form-control border border-secondary rounded mb-2"
      rows="4"
    />

    <button onClick={handlePostReview} className="btn btn-primary">
      Post Review
    </button>
  </div>
</div>

  );
};

export default Modal;
