const express = require('express');
const cors = require('cors');

const app = express();

// Allow requests from the specified origin
app.use(cors({
  origin: 'http://postagram-project-app.s3-website-ap-southeast-1.amazonaws.com'
}));

// Your routes and other middleware...

app.listen(3000, () => {
  console.log('Server is running on port 3000');
});
