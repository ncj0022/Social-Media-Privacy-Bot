const app = require("../server");
const Tweet = require("../models/tweet.model.js");
const mongoose = require("mongoose");
const supertest = require("supertest");

beforeEach((done) => {
    const uri = process.env.ATLAS_URI;
    mongoose.connect(uri, { useNewUrlParser: true, useCreateIndex: true, useUnifiedTopology: true},
        () => done());
});

afterEach((done) => {
    mongoose.connection.close(() => done())
});


test("GET /tweets", async () => {
//  const tweet = await Tweet.create({ contents: "Tweet", label: false });

    await supertest(app).get("/tweets")
        .expect(200)
        .then((response) => {
        // Check type and length
            expect(Array.isArray(response.body)).toBeTruthy();
            expect(response.body.length > 0).toBeTruthy();

        /* Check data
            expect(response.body[0]._id).toBe(tweet.id);
            expect(response.body[0].title).toBe(tweet.contents);
            expect(response.body[0].content).toBe(tweet.label);
        */
    });
});

test("GET /tweets/rand", async () => {
    await supertest(app).get("/tweets/rand")
        .expect(200)
        .then((response) => {
        // Check type and length
            expect(typeof(response.body.contents) == "string").toBeTruthy();
            expect(response.body.label == 0 || response.body.label == 1 ).toBeTruthy();
      });
  });