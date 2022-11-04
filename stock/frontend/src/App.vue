<script>

import Item from "./components/Item.vue"

export default {
  data(){
    return {
      stocks: [],
      info: {
        name:null,
        quantity:null,
        email:null,
        price:null,
      }
    }
  },

  mounted() {
    try {
      fetch("http://127.0.0.1:8000/api/stocks/")
        .then((res) => res.json())
        .then((data) => this.stocks = data)
    } catch (error) {
      console.log(error)
    }
  },
  methods:{
    //updates values from child components
    updateData(value) {
      this.stocks = value
    },
    //handleAdditem will create a inStock variable where if quantity is over 0, it will be true
    //then it will send a fetch request to a  URL and pass all data through body
    async handleAddItem(e) {
      e.preventDefault()

      let inStock = false
      if(this.info.quantity > 0) {
        inStock = true
      }
 
      try {
        await fetch("http://127.0.0.1:8000/api/stocks/", {
          method: "POST",
          body: JSON.stringify({
            name: this.info.name,
            quantity: this.info.quantity,
            email: this.info.email,
            price: this.info.price,
            in_stock: inStock,
          }) 
        }).then((res) => res.json())
          .then(data => this.stocks = data)
      } catch (error) {
        console.log(error)
      }
    }
  },
  components: {
    Item,
  },
}
</script>

<template>
  <div class="vh-100 mw-100 bg-dark">
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark mb-5">
      <div class="container-fluid">
        <a class="navbar-brand">Stock Application</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav me-auto mb-2 mb-lg-0">
            <li class="nav-item">
              <a class="nav-link active" aria-current="page">Home</a>
            </li>
          </ul>
          <form class="d-flex" role="search">
            <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
            <button class="btn btn-outline-success" type="submit">Search</button>
          </form>
        </div>
      </div>
    </nav>

    <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h1 class="modal-title fs-5" id="exampleModalLabel">Add New Stock</h1>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <form @submit="handleAddItem" method="post">
              <input v-model="info.name" class="form-control w-75 mb-2 ms-3 mt-3" type="text" placeholder="Item Name" aria-label="default input example">
              <input v-model="info.price" class="form-control w-75 mb-2 ms-3" type="number" placeholder="Price" aria-label="default input example">
              <input v-model="info.quantity" class="form-control w-75 mb-2 ms-3" type="number" placeholder="Quantity" aria-label="default input example">
              <input v-model="info.email" class="form-control w-75 mb-2 ms-3" type="email" placeholder="Email" aria-label="default input example">
              <button type="submit" class="btn btn-primary" data-bs-dismiss="modal">Add Stock</button>
            </form>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
          </div>
        </div>
      </div>
    </div>

    <div class="w-100 d-flex justify-content-center mb-4">
      <button type="button" class="btn btn-outline-success" data-bs-toggle="modal" data-bs-target="#exampleModal">
        Add Item
      </button>
    </div>

    <div class="container text-center">
      <div class="row text-light mb-2">
        <div class="col">
          Name
        </div>
        <div class="col">
          Quantity
        </div>
        <div class="col">
          Seller
        </div>
        <div class="col">
          Price
        </div>
        <div class="col">
          In Stock
        </div>
        <div class="col">
          Action
        </div>
      </div>
      <div class="break w-100 bg-light "></div>
      <br />
      <div v-for="(stock) in stocks.stocks"><Item :key="stock.id" @updateData="updateData($event)" :item="stock"/></div>
    </div>

  </div>
</template>

<style>
.break{
  height: 2px;
}
</style>
