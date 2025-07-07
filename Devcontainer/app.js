const express = require('express');
const app = express();
const port = 3000;

app.get('/platzi', (req, res) => {
    res.send('Hola desde mi app de Platzi');
});

app.listen(port, () => {
    console.log(`App listening at http://localhost:${port}/platzi`);
});

