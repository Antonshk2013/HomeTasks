# Домашнее задание №17

## 1. Тестовая коллекция в mongo atlas  sample_mflix.theaters Найти все кинотеатры в Калифорнии и посчитать их количество 
```
db.theaters.aggregate([{
    $match: {
      "location.address.city": "California"
    }
  },
  {
    $group:
      /**
       * _id: The id of the group.
       * fieldN: The first field name.
       */
      {
        _id: null,
        count: {
          $sum: 1
        }
      }
  }])
```
## 2. Тестовая коллекция в mongo atlas  sample_airbnb.listingsAndReviews  Найти недвижимость с самым большим количеством спален (bedrooms) и напишите ее название 
```
db["listingsAndReviews"].aggregate([
  {
    $sort: {
      bedrooms: -1
    }
  },
  {
    $limit: 1
  },
  {
    $project: {
      _id: 0,
      name: 1
    }
  }
])
```
## 3. Тестовая коллекция в mongo atlas  sample_airbnb.listingsAndReviews Найти недвижимость с самым высоким рейтингом  review_scores_rating при минимальном количестве отзывов 50 (number_of_reviews) и напишите ее название 
```
db.listingsAndReviews.aggregate([
  {
    $match: {
      number_of_reviews: { $gte: 50 }   
    }
  },
  {
    $sort: {
      "review_scores.review_scores_rating": -1  
    }
  },
  {
    $limit: 1   
       },
  {
    $project: {
      _id: 0,
      name: 1,
      number_of_reviews: 1,
      review_scores_rating: "$review_scores.review_scores_rating"
    }
  }
])
```
