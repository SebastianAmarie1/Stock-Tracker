<script>

export default {
  props: {
    item: Object,
  },
  data(){
    return {
      info: {
        name: this.item.name,
        quantity: this.item.quantity,
        email: this.item.email,
        price: this.item.price,
      }
    }
  },
  mounted(){
    console.log(this.info)
  },  
  methods: {
    seeId(){
      console.log(this.item.id, "Ran")
    },
    //handleDelete will send a DELETE fetch request with a ID  
    // it will then set data with the response we get

    async handleDelete(e){
      e.preventDefault()

      try {
        await fetch(`http://127.0.0.1:8000/api/stocks/${this.item.id}`, {
          method: "DELETE"
        })
          .then((res) => res.json())
          .then(data => this.$emit('updateData',data))
      } catch (error) {
        console.log(error)
      }
    },
    async handleEdit(e) {
      //handleEdit will send a fetch request to a URL with a ID with data in its body.
      //It will then set data with the reponse we get
    
      e.preventDefault()

      let inStock = false
      if(this.info.quantity > 0) {
        inStock = true
      }
      
      try {
        await fetch(`http://127.0.0.1:8000/api/stocks/${this.item.id}/`, {
          method: "PUT",
          body: JSON.stringify({
            name: this.info.name,
            quantity: this.info.quantity,
            email: this.info.email,
            price: this.info.price,
            in_stock: inStock,
          }) 
        })
          .then((res) => res.json())
          .then(data => this.$emit('updateData',data))
      } catch (error) {
        console.log(error)
      }
    }
  },
}
</script>

<template>
  <div class="row text-light mb-2">
        <div class="col">
          {{ item.name }}
        </div>
        <div class="col">
          {{ item.quantity }}
        </div>
        <div class="col">
          {{ item.email }}
        </div>
        <div class="col">
          £{{ item.price }}
        </div>
        <div class="col d-flex align-items-center justify-content-center">
          <div v-if="item.quantity > 0" class="available"></div>
          <div v-if="item.quantity <= 0" class="unavailable"></div>
        </div>
        <div class="col">
          <div class="modal fade" :id="'EditModal'+this.item.id" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
            <div class="modal-dialog">
              <div class="modal-content">
                <div class="modal-header">
                  <h1 class="modal-title fs-5 text-dark " id="exampleModalLabel">Edit Stock</h1>
                  <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                  <form @submit="handleEdit">
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
          <button @click="seeId" type="button" class="btn btn-outline-success" data-bs-toggle="modal" :data-bs-target="'#EditModal'+this.item.id">
            Edit
          </button>
          <button type="danger" @click="handleDelete" class="btn btn-danger ms-2">Delete</button>
        </div>
      </div>

</template>

<style >
.available{
  width: 20px;
  height: 20px;

  background-color: green;
}
.unavailable{
  width: 20px;
  height: 20px;

  background-color: red;
}

.pos-checkbox{
  margin-left: -23em;
}

</style>
