const mongoose = require("mongoose");
const Schema = mongoose.Schema;

const carSchema = new mongoose.Schema({
    speed: String,
    fuelLevel: String,
    distanceTravelled: String,
    timestamp: { type: Date, default: Date.now }
});

module.exports = mongoose.model('Car', carSchema);