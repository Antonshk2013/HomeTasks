# Домашнее задание №19

## 1. Найдите трек с наивысшими показателями  Danceability и Energy. 
```
наивысший показатель  Danceability
db.Spotify_Youtube.aggregate([
  {
    $sort: {
      Danceability: -1
    }
  },
  {
    $limit: 1
  }
])
наивысший показатель  Energy
db.Spotify_Youtube.aggregate([
  {
    $sort: {
      Energy: -1
    }
  },
  {
    $limit: 1
  }
])

```
## 2. У какого трека (но не compilation) самая большая длительность? +
```
db.Spotify_Youtube.aggregate([
  {
    $sort: {
      Duration_ms: -1
    }
  },
  {
    $limit: 1
  }
])

```

## 3. В каком одном альбоме самое большее количество треков? 
```
db.Spotify_Youtube.aggregate([
  {
    $group: {
      _id: "$Album",
      trackCount: {
        $sum: 1
      }
    }
  },
  {
    $sort:
      {
        trackCount: -1
      }
  },
  {
    $limit:
      1
  }
])
```
## 4. Сколько просмотров видео на youtube у трека с самым высоким количеством прослушиваний на spotify (Stream)? .
```
db.Spotify_Youtube.aggregate([
  {
    $sort: {
      Stream: -1
    }
  },
  {
    $limit: 1
  },
  {
    $project:
      {
        _id: 0,
        Views: 1
      }
  }
])
```
## 5.Экспортируйте 20 самых популярных (прослушивания или просмотры) треков по версиям youtube и spotify и импортируйте в базу ich_edit их с именами top20youtube и top20spotify, и добавьте им свои имена для уникальности.
```
db.top20spotify_Shkarupa.countDocuments()
db.top20youtube_Shkarupa.countDocuments()

```
