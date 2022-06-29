const mongoose = require('mongoose');

const Schema = mongoose.Schema;

const tweetSchema = new Schema({
    contents: { type: String, required: true },
    label: { type: Boolean, required: true }
});

const Tweet = mongoose.model('Tweet', tweetSchema);

module.exports = Tweet;