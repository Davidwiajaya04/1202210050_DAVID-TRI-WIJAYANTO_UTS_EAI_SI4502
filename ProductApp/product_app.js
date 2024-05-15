const express = require('express')
const app = express()

const products = [
    {id:1, name:"Head & Shoulders", description:"Shampoo", price:32000},
    {id:2, name:"Teh Pucuk", description:"Minuman", price:5000},
    {id:3, name:"Mentos", description:"Candy", price:8000}
]

app.get('/products', (req, res) => {
    res.json(products)
})

app.get('/products/:product_id', (req, res) => {
    const productId = parseInt(req.params.product_id)
    const product = products.find(product => product.id === productId)

    if(product){
        res.json(product)
    }else{
        res.status(404).json({ error: "Product not found" })
    }
})

app.listen(5000, () => {
    console.log("Server is running.")
})