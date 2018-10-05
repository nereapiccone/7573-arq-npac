const express = require("express");

const app = express(); // instancio la web app

const PORT = 3000;



app.get('/', function(req,res){
    res.send('respuesta veloz');
});

app.get('/slow', function(req,res){
    res.send('soy leeeeento y tengo caaaaarga');
});

app.get("/delay", (req, res) => {
  setTimeout(function(){ 
     res.send("Hola, mundo lennto JS!")
  }, 1000);

});




app.listen(PORT, () => {
  console.log("Escuchando en el puerto ", PORT);
});


