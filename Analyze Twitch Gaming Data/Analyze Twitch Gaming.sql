-- TASK : 1 = Select the first 20 rows from each of the two tables

SELECT *
FROM stream
LIMIT 20;

SELECT *
FROM chat
LIMIT 20;


-- TASK : 2 = unique games in the stream table

SELECT DISTINCT game
FROM stream;


-- TASK : 3 = unique channels in the stream table

SELECT DISTINCT channel
FROM stream;


-- TASK : 4 = most popular games in the stream table

SELECT game, COUNT(*)
FROM stream
GROUP BY 1
ORDER BY 2 DESC;


-- TASK : 5

SELECT country, COUNT(*)
FROM stream
WHERE game = 'League of Legends'
GROUP BY 1
ORDER BY 2 DESC
LIMIT 10;


-- TASK : 6

SELECT player, COUNT(*)
FROM stream
GROUP BY 1
ORDER BY 2 DESC
LIMIT 10;


-- TASK : 7

SELECT game,
  CASE
      WHEN game = 'Dota 2'
      THEN 'MOBA'
  WHEN game = 'League of Legends' 
      THEN 'MOBA'
  WHEN game = 'Heroes of the Storm'
      THEN 'MOBA'
    WHEN game = 'Counter-Strike: Global Offensive'
      THEN 'FPS'
    WHEN game = 'DayZ'
      THEN 'Survival'
    WHEN game = 'ARK: Survival Evolved'
      THEN 'Survival'
  ELSE 'Other'
  END AS 'genre',
  COUNT(*)
FROM stream
GROUP BY 1
ORDER BY 3 DESC;


-- TASK : 8

SELECT time
FROM stream
LIMIT 10;


-- TASK : 9 & 10

SELECT strftime('%H', time) AS 'Hours', COUNT(*)
FROM stream
WHERE country = 'US'
GROUP BY 1
LIMIT 20;


-- TASK : 11 - joining the two tables

SELECT *
FROM stream
JOIN chat
  ON stream.device_id = chat.device_id;


