
# Домашнее задание №16

## 1. Найдите средний возраст из коллекции ich.US_Adult_Income

```
use ich
db.getCollection('US_Adult_Income').aggregate( [
  {
    $group:
      {
        _id: null,
        averageAge: {
          $avg: "$age"
        }
      }
  }
])
```

## 2. Поменяв подключение к базе данных, создать коллекцию orders_NAME (для уникальности - добавим ваше имя в название) 

```
db.orders_ShkarupaAS.insertMany([
  {
    "id": 1,
    "customer": "Olga",
    "product": "Apple",
    "amount": 15.55,
    "city": "Berlin"
  },
  {
    "id": 2,
    "customer": "Anna",
    "product": "Apple",
    "amount": 10.05,
    "city": "Madrid"
  },
  {
    "id": 3,
    "customer": "Olga",
    "product": "Kiwi",
    "amount": 9.6,
    "city": "Berlin"
  },
  {
    "id": 4,
    "customer": "Anton",
    "product": "Apple",
    "amount":  20,
    "city": "Roma"
  },
  {
    "id": 5,
    "customer": "Olga",
    "product": "Banana",
    "amount": 8,
    "city": "Madrid"
  },
  {
    "id": 6,
    "customer": "Petr",
    "product": "Orange",
    "amount": 18.3,
    "city": "Paris"
  }
])
```

## 3. Найти сколько всего было совершено покупок:

```
db.orders_ShkarupaAS.countDocuments()
```
или
```
db.orders_ShkarupaAS.aggregate([
    {
        $group:{
            _id: null, 
            count:{ 
                $sum: 1
            }
        }
    }, 
    {
        $project: {
            _id: 0,
            count: 1
            }
        }
    ]
)       
```

## 4. Найти сколько всего раз были куплены яблоки:
```
db.orders_ShkarupaAS.aggregate([
{$match: {
    product: 'Apple'
    }
},
    
{
    $group:
        {
            _id: null, 
            count:{ 
                $sum: 1
            }
        }
    }, 
{
    $project: 
        {
            _id: 0, 
            count: 1
        }
    }
])
```
## 5. Вывести идентификаторы трех самые дорогих покупок
```
db.orders_ShkarupaAS.aggregate([
{ $sort: {
    amount: -1
    }
}, 
{ $limit: 3}, 
{ $project:{ 
    _id:1
    } 
}
])
```
## 6. Найти сколько всего покупок было совершено в Берлине
```
db.orders_ShkarupaAS.aggregate([
{$match: {
    city: 'Berlin'
    }
},
{
    $group:
        {
            _id: null, 
            count:{ 
                $sum: 1
            }
        }
    }, 
{
    $project: 
        {
            _id: 0, 
            count: 1
        }
    }
])
```
## 7. Найти количество покупок яблок в городах Берлин и Мадрид
```
db.orders_ShkarupaAS.aggregate([
  {
    $match: {
      product: "Apple",
      $or: [
        { city: "Berlin" },
        { city: "Madrid" }
      ]
    }, 
  },
  {
    $group:
        {
            _id: null, 
            count:{ 
                $sum: 1
            }
        }
    }, 
{
    $project: 
        {
            _id: 0, 
            count: 1
        }
    }
])
```
## 8. Найти сколько было потрачено каждым покупателем
```
db.orders_ShkarupaAS.aggregate([{
    $group:
        {
            _id : "$customer", 
            total:{ 
                $sum: "$amount"
            }
        }
    }])
```
## 9. Найти в каких городах совершала покупки Ольга
```
db.orders_ShkarupaAS.aggregate([
  {
    $match: { customer: "Olga" }
  },
  {$project: {
_id:0,city:1}}
])
