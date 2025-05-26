# Домашнее задание №18

## 1. Из коллекции sample_airbnb.listingsAndReviews найдите среднюю цену за сутки проживания на Гавайских островах. Островов несколько, поэтому либо используем {'address.location': {$geoWithin: { $centerSphere …. Либо перечисляем все возможные острова в поле market
```
db.sample_airbnb.listingsAndReviews.aggregate([

  {

    $match: {

      "address.location.coordinates": {

        $geoWithin: {

          $centerSphere: [

            [-157.5, 20.5],

            250 / 3963.2

          ]

        }

      }

    }

  },

  {

    $group: {

      _id: null,

      avg_price: {

        $avg: "$price"

      }

    }

  },

  {

    $project: {

      _id: 0,

      avg_price: {

        $round: ["$avg_price", 2]

      }

    }

  }

])
```
## 2. Подсчитайте в коллекции sample_mflix.movies, сколько фильмов имеют imdb рейтинг выше 8 и выходили в период с 2015 до 2023 года (используем year) Какой из них имеет самый высокий рейтинг ?
```
db.movies.aggregate([
  {
    $match: {
      "tomatoes.critic.rating": {
        $gt: 8
      },
      year: {
        $gte: 2015,
        $lt: 2025
      }
    }
  },
  {
    $sort: {
      "tomatoes.critic.rating": -1
    }
  },
  {
    $limit:
      /**
       * Provide the number of documents to limit.
       */
      1
  },
  {
    $project:
      /**
       * specifications: The fields to
       *   include or exclude.
       */
      {
        _id: 0,
        title: 1
      }
  }
])
```