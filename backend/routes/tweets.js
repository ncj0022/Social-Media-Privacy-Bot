const router = require('express').Router();
let Tweet = require('../models/tweet.model.js');

// GET ALL
router.route('/').get((req, res) => {
    Tweet.find()
    .then(tweets => res.json(tweets))
    .catch(err => res.status(400).json('Error: ' + err));
});

// GET A RANDOM DOCUMENT FROM THE DATABASE
router.route('/rand').get((req, res) => {
    Tweet.collection.estimatedDocumentCount((err, count) => {
        var random = Math.floor(Math.random() * count);

        Tweet.findOne().skip(random)
        .then(tweet => res.json(tweet))
        .catch(err => res.status(400).json('Error: ' + err));
    });
});

// UDPATE BY ID
router.route('/update/:id').post((req, res) => { 
    Tweet.findById(req.params.id)
    .then(tweet => {
        tweet.contents = req.body[0].contents;
        tweet.label = req.body[0].label;

        newTweet.save()
        .then(() => res.json('New Tweet Added!'))
        .catch(err => res.status(400).json('Error: ' + err));
    })
    .catch(err => res.status(400).json('Error: ' + err));
});

module.exports = router;