
# Feature Selection Documentation

## Introduction
This document provides details on the pre-processing and selection of features used in the project.

## Categorical Features (High number of categories)
- **Point of Sale**: `point_of_sale` target-encoded with 81 unique values.
- **Geographical Location**: `geo_location_country` target-encoded with 134 unique values.
- **Destination ID**: `destination_id` target-encoded with 500 unique values.
- **Property ID**: `prop_id` target-encoded

## Categorical/Binary Features
- **Sort Type**: `sort_type` one-hot encoded or dropped, keep only recommended ones.
- **Search Day/Time Features**: Converted to categorical and one-hot encoded:
  - `checkin_day`
  - `checkout_day`
  - `checkin_month`
  - `prop_id`: used in some experiments
- **Binary Indicators**: Left as is (0,1) or rows dropped where applicable:
  - `is_travel_ad`
  - `is_mobile`
  - `is_free_cancellation`
  - `is_drr`

## Ordinal Features
- **Ratings and Buckets**:
  - `star_rating`: Drop NAs and keep as integers 1-5.
  - `review_rating`: Float64, drop when rating == 0.0 and convert to integers.
  - `price_bucket`: Float64, leave as is (no scaling) and convert to integers.
  - `ranknoad` (initial rank): Int64, leave as is (no scaling) or drop.
  - `rank`: dropped in some experiments.
  - `rank_noad`: dropped in some experiments

## Numerical Features
- Standard scaled features:
  - `adult_count`
  - `child_count`
 
  - `length_of_stay`
  - `booking_window`
  - `review_count` (drop count == 0)

## Not Used as Features
- `num_clicks`: Used for relevance label/y.
- `is_trans`: Used for relevance label
- `infant_count` (99% == 0) # dropped as majority values are 0
- `room_count` (99% == 1) # dropped as majority values are 1
- `user_id`


