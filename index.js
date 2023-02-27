const express = require('express')
const mongoose = require('mongoose')
const path = require('path')
const app = express()
const ejsmate = require('ejs-mate')
const { name } = require('ejs')

app.set(express.urlencoded({extended: true}))
app.set('view engine', 'ejs')
app.engine('ejs', ejsmate)
app.set('views', path.join(__dirname, 'views'))
app.set(express.static('public'))
app.listen(3000, ()=> console.log("Listening...."))

mongoose.connect('mongodb://127.0.0.1:27017/destinations', { useNewUrlParser:true } )
.then(()=>console.log("Working"))
.catch((err)=>{
    console.log("error")
    console.log(err)})


const destination = mongoose.Schema({
    name:{
      type: String,
      required: True

    },
    description:{
      type: String,
      required: True

    },
    location:{
      type: String,
      default: "https://www.google.com/maps/place/"+name

    },
    category:{
      type: String,
      default: [name.split()]
    }

}
)

const places = mongoose.model('place', destination)



app.get('/', (req, res)=>{
    res.render("home")
})
places.find({}).then((x)=> console.log(x))
