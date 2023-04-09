const http = require('http');

const hostname = '0.0.0.0';
const port = 3000;

const server = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  res.end('Hello World');
});

server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});

// const MongoClient = require('mongodb').MongoClient;
// const url = 'mongodb://localhost:27017/mydb';

// MongoClient.connect(url, function(err, db) {
//   if (err) throw err;
//   const collection = db.collection('keys');
//   collection.find({}).toArray(function(err, keys) {
//     if (err) throw err;
//     console.log(keys);
//     db.close();
//   });
// });