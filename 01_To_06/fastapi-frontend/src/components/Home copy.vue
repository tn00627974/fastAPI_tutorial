<template>
  <div>
    <h1>Data from FastAPI & Vue</h1>
    <p>{{ message }}</p>
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
  mounted() {
    this.fetchData();
  },
  methods: {
    async fetchData() {
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
        const response = await fetch("http://127.0.0.1:8000/items", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ message: "This is some posted data." }),
        });
        const data = await response.json();
        this.message = data.message;
      } catch (error) {
        console.error("Error posting data:", error);
      }
    },
  },
};
</script>
