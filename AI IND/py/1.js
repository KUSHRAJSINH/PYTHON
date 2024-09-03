var v=require("validator");
const { error } = require('console')
const mg=require('mongoose')
mg.connect("mongodb://127.0.0.1:27017/mydb")
.then(()=>{
    console.log('connected')
})
.catch((error)=>{
    console.log(error)
})

const myschema=new mg.Schema({
    name:String,
    surname:String,
    age:Number,
    date:{
        type:Date,
        defult: new Date()
    },
    email:{
        type:String,
        validate(val)
        {
            if (!v.isEmail(val))
            {
                throw new Error("enter valid email id");
            }
        }
    }
})

const person=new mg.model('person',myschema)

const personData=new person({
    name:"test",
    surname:"test data",
    age:23,
    email:"dipanshugmail.com"
})

personData.save()