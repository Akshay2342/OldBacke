const express = require('express')
const app = express()
const cors = require('cors')
const port = 4000
const path = require('path')
const { spawn } = require('child_process');
const { json } = require('body-parser')

app.use('/images', express.static(path.join(__dirname)));
app.use(cors())
app.use(express.json());

app.get('/try', (req, res) => {
  console.log("Hello World!")
  res.send('Hello World!')
}); 

app.post('/UpdateRows', (req, res) => {
  let dataToSend = req.body;
  // let dataToSend

  console.log(dataToSend)
  dataToSend= JSON.stringify(dataToSend);
  const python = spawn('python', ['UpdateRows.py' , dataToSend]);
  let jsonData = '';

  python.stdout.on('data', (data) => {
    jsonData += data.toString();
  });

  python.on('close', (code) => {
    console.log(`child process close all stdio with code ${code}`);
    let jsonObject;

    try {
        jsonObject = JSON.parse(jsonData);
    } catch (error) {
        console.error('Unable to parse JSON:', error);
        jsonObject = jsonData;
    }

    const firstBrace = jsonData.indexOf('{');
    const lastBrace = jsonData.lastIndexOf('}');
    // Extract the substring from the first { to the last }
    jsonObject = jsonData.substring(firstBrace, lastBrace + 1);
    console.log(typeof jsonData)
    res.send(jsonObject);
  });

  python.on('error', (error) => {
    console.error(`Error occurred while executing Python script: ${error.message}`);
    res.status(500).send('Internal Server Error');
  });
});

// give city name it will get the food list 
app.get('/getFoodList', (req, res) => {
  const dataToSend = "Hyderabad";
  const python = spawn('python', ['script.py', dataToSend]);
  const scriptExecution = new Promise((resolve, reject) => {
    let JsonStr = "";
    python.stdout.on('data', (data) => {
      JsonStr += data.toString();
    });
    try {
      JSON.parse(jsonData); // Try to parse the JSON
      res.send(jsonData);
    } catch (error) {
      console.error(`Error parsing JSON: ${error.message}`);
      res.status(500).send('Internal Server Error');
    }
    console.log(jsonData)
    python.on('close', (code) => {
      console.log(`child process close all stdio with code ${code}`);
      resolve(JsonStr);
    });

    python.on('error', (error) => {
      reject(error);
    });
  });

  // Wait for the promise to resolve, then send the response
  scriptExecution.then((jsonData) => {
    res.send({jsonData});
  }).catch((error) => {
    res.status(500).send(error);
  });
});

app.post('/UpdateBucket', (req, res) => {
  const arr = ["idli" , 'dosa' , 'vada'];
  const dataToSend = req.body.data ? req.body.data : arr;
  console.log(dataToSend)
  const args = ['txt2Bucket.py'].concat(dataToSend);
  const python = spawn('python', args);

  // Create a new promise that resolves when the python script has finished
  const scriptExecution = new Promise((resolve, reject) => {
    let imageStr = "";

    python.stdout.on('data', (data) => {
      imageStr += data.toString();
    });

    python.on('close', (code) => {
      console.log(`child process close all stdio with code ${code}`);
      resolve(imageStr);
    });

    python.on('error', (error) => {
      reject(error);
    });
  });

  scriptExecution.then((imageStr) => {
    const firstBrace = imageStr.indexOf('{');
    const lastBrace = imageStr.lastIndexOf('}');
    // Extract the substring from the first { to the last }
    imageStr = imageStr.substring(firstBrace, lastBrace + 1);
    console.log({imageStr})
    res.send(imageStr);
  }).catch((error) => {
    res.status(500).send(error);
  });
});

app.listen(port, () => {
  console.log(`Server running on port ${port}`);
});