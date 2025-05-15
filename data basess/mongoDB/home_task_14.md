
# Домашнее задание №14

## 1. Из коллекции customers выяснить из какого города "Sven Ottlieb"

```
use ich
db.getCollection('customers').aggregate([
    {
    $match:
      {
        ContactName: "Sven Ottlieb"
      }
    },
    {
    $project:
      {
        City: 1
      }
    }
  ])
```

## 2. Из коллекции ich.US_Adult_Income найти возраст самого взрослого человека

```
use ich
db.getCollection('US_Adult_Income').aggregate([
    {
      $sort:
        {
          age: -1
        }
    },
    {
      $limit:
        1
    }
  ])
```

## 3. Из 2 задачи выясните, сколько человек имеют такой же возраст

```
use ich
db.getCollection('US_Adult_Income').aggregate([
    {
      $match: {
        age: 90
      }
    },
    {
      $count:
       "peopleWithMaxAge"
    }
  ])
```

## 4. Найти _id ObjectId документа, в котором education " IT-career-hub"
```
use ich
db.getCollection('US_Adult_Income').aggregate([
    {
      $match:
        {
          education: " IT-career-hub"
        }
    }
  ])
```

## 5. Выяснить количество людей в возрасте между 20 и 30 годами

```
use ich
db.getCollection('US_Adult_Income').aggregate([
  {
    $match:
      {
        age: {
          $gte: 20,
          $lte: 30
        }
      }
  },
  {
    $group: {
      _id: null,
      count: {
        $sum: 1
      }
    }
  }
])
```
