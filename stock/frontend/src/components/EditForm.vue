<script>
export default {

    props: {
    items: Object,
  },
  data(){
    return {
      infoF: {
        nameF: this.items.name,
        quantityF: this.items.quantity,
        emailF: this.items.email,
        priceF: this.items.price,
      }
    }
  },
  methods: {
    async handleEdit(e) {
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
    <form @submit="handleAddItem" method="post">
        <input v-model="infoF.nameF" class="form-control w-75 mb-2 ms-3 mt-3" type="text" placeholder="Item Name" aria-label="default input example">
        <input v-model="infoF.priceF" class="form-control w-75 mb-2 ms-3" type="number" placeholder="Price" aria-label="default input example">
        <input v-model="infoF.quantityF" class="form-control w-75 mb-2 ms-3" type="number" placeholder="Quantity" aria-label="default input example">
        <input v-model="infoF.emailF" class="form-control w-75 mb-2 ms-3" type="email" placeholder="Email" aria-label="default input example">
        <button type="submit" class="btn btn-primary" data-bs-dismiss="modal">Add Stock</button>
    </form>

</template>

<style>

</style>