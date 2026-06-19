# Student Segmentation and Personalized Course Recommendation System for EduPro

## Background and Context:
- Online learners are not homogeneous:
  - Some explore beginner courses across domains
  - Some specialize deeply in one subject
  - Others focus on career-oriented certifications

- Generic course recommendations fail to:

  - Maximize learner engagement

  - Improve course completion

  - Build long-term platform loyalty

- EduPro needs a data-driven personalization engine to:

  - Understand different learner types

  - Recommend relevant courses

  - Support personalized learning journeys

## Problem Statement

- EduPro currently faces:

  - One-size-fits-all course recommendations
 
  - Limited understanding of learner behavior patterns

  - No structured learner segmentation framework

- As a result: 

  - Learners struggle to discover relevant content  

  - Engagement and retention opportunities are lost

## Dataset Fields Utilized (High-Dimensional)

- Users Sheet

  - UserID

  - Age

  - Gender

- Courses Sheet

  - CourseID

  - CourseCategory

  - CourseType

  - CourseLevel

  - CourseRating

- Transactions Sheet

  - UserID

  - CourseID

  - TransactionDate

  - Amount

## Feature Engineering

- Key engineered learner-level features include:

 - Engagement Features
    - Total courses enrolled

  • Average courses per category

  • Enrollment frequency

Preference Features

  • Preferred course category

  • Preferred course level

  • Average course rating enrolled

Behavioral Features

  • Average spending per learner

  • Diversity score (number of categories explored)

  • Learning depth index (beginner vs advanced ratio)

## Data Science Methodology (Step-by-Step)

Learner-Level Aggregation

  • Aggregate transaction data at UserID level

  • Create learner profiles combining demographics and behavior

Data Preprocessing

  • Normalize numerical features

  • Encode categorical variables

  • Reduce noise from sparse enrollments

Learner Segmentation (Clustering)

Apply unsupervised algorithms:

  • K-Means Clustering

  • Hierarchical Clustering (validation)

  • Elbow & Silhouette methods for cluster selection

Personalized Recommendation Logic

Build cluster-aware recommendations using:

  • Content-based filtering

  • Similar learner profiles

  • Course popularity within cluster

  • Rating-weighted relevance

## Evaluation & Validation

<img width="1408" height="526" alt="image" src="https://github.com/user-attachments/assets/c493a1a4-e6bc-4016-a634-e389946432ea" />

##Streamlit Web Application Requirements

Core Modules

  • Learner profile explorer
  
  • Cluster visualization dashboard

  • Personalized course recommendations

  • Segment comparison panels
User Capabilities

  • Select a learner profile

  • View assigned segment

  • See recommended learning paths

  • Filter recommendations by level or category

## Deliverables and Submission

  • Research paper (EDA, insights, recommendations)

  • Streamlit dashboard (live analytics)

  • Executive summary for government stakeholders

## Conclusion

This project introduces student-centric intelligence to the EduPro platform. By shifting focus from predicting course demand to understanding and personalizing the learner journey, it enables EduPro to deliver meaningful, adaptive, and engaging learning experiences, making it completely different in purpose and methodology
