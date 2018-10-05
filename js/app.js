const express = require("express");

const app = express(); // instancio la web app

const PORT = 3000;



// defino la ruta y quien responde cuando llega el request
app.get("/delay", (req, res) => {
  setTimeout(function(){ 
     res.send("Hola, mundo lennto JS!")
  }, 1000);

});// esto tira el request y a los 10 segundos manda el response


app.get('/', function(req,res){
    res.send('respuesta veloz');
});

app.get('/slow', function(req,res){
    res.send('soy leeeeento y tengo caaaaarga');
});



/*
app.listen(3000, function () {
  console.log('Example app listening on port 3000!');
});
*/
/* version de la clase: */
app.get("/", (req, res) => {
  res.send("Hola, mundo JS!");
});// funcion anonima en el segundo parametro. parametros, flecha y el cuerpo de la funcion



app.listen(PORT, () => {
  console.log("Escuchando en el puerto ", PORT);
});


