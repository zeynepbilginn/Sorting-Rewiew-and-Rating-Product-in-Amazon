# Rating Product & Sorting Reviews in Amazon

## Introduction

In the e-commerce industry, accurately calculating post-purchase product ratings and effectively sorting reviews are paramount. These factors directly influence customer satisfaction, product visibility for sellers, and a seamless shopping experience for buyers. Addressing these challenges not only boosts sales for e-commerce platforms and sellers but also ensures customers complete their purchasing journey smoothly.

This project focuses on tackling two main problems:
1. Adjusting product ratings based on the recency of reviews to reflect a more accurate average rating.
2. Sorting product reviews in a way that prioritizes helpfulness to guide potential customers better.

## Objective

The primary objective of this project is to enhance the existing rating system by introducing a time-weighted average rating method. Additionally, we aim to develop a robust review sorting system that highlights the most helpful reviews, thereby mitigating the impact of misleading feedback.

## Methodology

To achieve our goals, we employed several statistical and computational techniques outlined below:

1. **Average Rating Calculation**: We calculated the existing average rating for comparison.
2. **Time-weighted Average Rating**: Implemented a method to weigh ratings based on the recency of the review, giving more importance to recent feedback.
3. **Review Sorting Metrics**: Developed three key metrics to sort reviews effectively:
   - Positive-Negative Score Difference
   - Average Rating Score
   - Wilson Lower Bound Score

These metrics take into account the helpfulness votes (upvotes and downvotes) to prioritize reviews that provide the most value to potential customers.

## Dataset

The dataset used in this project comprises Amazon product data, focusing on the Electronics category with extensive reviews and ratings for the most commented products. It includes the following variables:
- `reviewerID`: User ID
- `asin`: Product ID
- `reviewerName`: User Name
- `helpful`: Helpfulness vote count
- `reviewText`: Review text
- `overall`: Product rating
- `summary`: Review summary
- `unixReviewTime`: Review time (Unix time)
- `reviewTime`: Review time (raw)
- `day_diff`: Days since the review was posted
- `helpful_yes`: Number of helpful votes
- `total_vote`: Total number of votes

For a detailed analysis and methodology, refer to the [Kaggle Notebook](https://www.kaggle.com/code/zeynepbilgin/sorting-reviews-rating-product-in-amazon).

## Results

By applying the time-weighted average rating and the Wilson Lower Bound score for review sorting, we can significantly improve the accuracy of product ratings and the usefulness of product reviews. These methods provide a more dynamic and helpful perspective to potential customers, enhancing the overall e-commerce experience.

## Conclusion

This project illustrates the importance of adapting traditional rating and review sorting methods to meet the evolving needs of the e-commerce landscape. Through our analysis, we've demonstrated that incorporating the recency of reviews and the helpfulness of feedback can lead to a more accurate and customer-friendly shopping environment.

For more insights and the complete code, visit the [Kaggle Notebook](https://www.kaggle.com/code/zeynepbilgin/sorting-reviews-rating-product-in-amazon). This project is an example of leveraging data science to solve real-world e-commerce challenges, aiming to benefit both customers and sellers on platforms like Amazon.
