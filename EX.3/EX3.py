Linux Shell Script Examples:
File: start_replica.sh (for Replication):
#!/bin/bash
mongod --replSet "rs0" --port 27017 --dbpath ./rs1/db --bind_ip localhost --fork --logpath ./rs1/mongo.log
mongod --replSet "rs0" --port 27018 --dbpath ./rs2/db --bind_ip localhost --fork --logpath ./rs2/mongo.log
mongod --replSet "rs0" --port 27019 --dbpath ./rs3/db --bind_ip localhost --fork --logpath ./rs3/mongo.log
mongo --port 27017 <<EOF
rs.initiate({
  _id: "rs0",
  members: [
    { _id: 0, host: "localhost:27017" },
    { _id: 1, host: "localhost:27018" },
    { _id: 2, host: "localhost:27019" }
  ]
})
EOF
File: start_shard.sh (for Sharding):
#!/bin/bash
mongod --configsvr --replSet configReplSet --port 26050 --dbpath ./config/db --bind_ip localhost --fork --logpath ./config/config.log
mongod --shardsvr --port 27020 --dbpath ./shard1/db --bind_ip localhost --fork --logpath ./shard1/mongo.log
mongod --shardsvr --port 27021 --dbpath ./shard2/db --bind_ip localhost --fork --logpath ./shard2/mongo.log
mongos --configdb configReplSet/localhost:26050 --bind_ip localhost --fork --logpath mongos.log --port 27017
mongo --port 27017 <<EOF
sh.addShard("localhost:27020")
sh.addShard("localhost:27021")
sh.enableSharding("college")
sh.shardCollection("college.students", { "rollno": 1 })
EOF

Sample MongoDB JS Insertion File: mongo_insert_test.js
use college
db.students.insertMany([
  { rollno: 101, name: "Raja", mark: 95 },
  { rollno: 102, name: "Pooja", mark: 85 },
  { rollno: 103, name: "Roja", mark: 75 }
])