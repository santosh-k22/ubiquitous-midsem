var express = require('express');
var router = express.Router();
const Car = require('../models/car'); 

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
});

// Route to display the most recent car data
router.get('/new', async (req, res) => {
  try {
      const latestData = await Car.findOne().sort({ timestamp: -1 });

      if (!latestData) {
          return res.render('d2', { data: { speed: 'N/A', fuelLevel: 'N/A', distanceTravelled: 'N/A' } });
      }

      res.render('d2', { data: latestData });
      // res.render('dashboard', { data: latestData });
  } catch (err) {
      console.error(err);
      res.status(500).send('Server Error');
  }
});

// Route to add new car data
router.post('/add', async (req, res) => {
  const { speed, fuelLevel, distanceTravelled } = req.body;

  try {
      const newCarData = new Car({ speed, fuelLevel, distanceTravelled });
      await newCarData.save();
      res.status(201).send('Data added successfully');
  } catch (err) {
      console.error(err);
      res.status(500).send('Server Error');
  }
});

module.exports = router;
