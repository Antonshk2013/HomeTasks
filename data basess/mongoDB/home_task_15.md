
# Домашнее задание №15

## 1. Коллекция imdb : Используя оператор $size , найдите фильмы, написанные 3 сценаристами (writers) и снятые 2 режиссерами (directors)

```
use ich
db.getCollection('imdb').aggregate([
  {
    $match:
      {
        writers: {
          $size: 3
        },
        directors: {
          $size: 2
        }
      }
  }
])
```

## 2. Коллекция bookings: Найдите адрес нахождения автомобиля с vin WME4530421Y135045 по самой последней дате (и времени) final_date

```
use ich
db.getCollection('bookings').aggregate([
  {
    $match:
      {
        vin: "WME4530421Y135045"
      }
  },
  {
    $sort:
      {
        final_date: -1,
        final_time: -1
      }
  },
  {
    $limit:
      1
  }
])
```

## 3. Коллекция bookings: подсчитайте, у скольких автомобилей при окончании аренды закончилось топливо (final_fuel)

```
use ich
db.getCollection('bookings').aggregate([
  {
    $match:
        {
        final_fuel: 0
      }
  },
  {
    $count:
      "count_final_fuel"
  }
])
```

## 4.  //Коллекция bookings: найдите номерной знак и vin номер авто, с самым большим километражом (distance)
```
use ich
db.getCollection('bookings').aggregate([
  {
    $sort:
      {
        distance: -1
      }
  },
  {
    $limit:
      1
  },
  {
    $project:
      {
        _id: 0,
        vin: 1,
        plate: 1
      }
  }
])
```

## 5. Коллекция imdb. Найдите фильм с участием "Brad Pitt" с самым высоким рейтингом (imdb.rating)

```
use ich
db.getCollection('imdb').aggregate([
  {
    $match:
      {
        cast: "Brad Pitt"
      }
  },
  {
    $sort:
      {
        "imdb.rating": -1
      }
  },
  {
    $limit:
      1
  }
])
```
