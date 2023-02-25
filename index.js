const express = require('express')
const mongoose = require('mongoose')
const path = require('path')
const app = express()

app.set(express.urlencoded({extended: true}))
app.set('view engine', 'ejs')
app.set('views', path.join(__dirname, 'views'))

app.listen(3000, ()=> console.log("Listening...."))

app.get('/', (req, res)=>{
    res.send("hello")
})