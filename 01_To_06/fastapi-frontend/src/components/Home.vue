<template>
  <div>
    <h1>{{ message }}</h1>
    <button @click="getData">Get Data</button>
    <button @click="posthData">Post Data</button>
  </div>
</template>

<script>
export default {
  name: "DataComponent",
  data() {
    return {
      message: "This is some default message.",
    };
  },

  methods: {
    async getData() {
      try {
        const response = await fetch("http://127.0.0.1:8000/");
        const data = await response.json();
        this.message = data.message;
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    },

    async posthData() {
      try {
        const item = {
          name: "Test",
          price: 100.0,
          description: "This is an example item.",
        };
        const response = await fetch("http://127.0.0.1:8000/items", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(item),
        });
        const data = await response.json();
        this.message = `name: "${data.item_name}", price: ${data.item_price}`;
        // this.message = data.item_name;
      } catch (error) {
        console.error("Error posting data:", error);
      }
    },
  },
};
</script>