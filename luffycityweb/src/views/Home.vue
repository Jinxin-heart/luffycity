<script setup>
import Header from "../components/Header.vue";
import Footer from "../components/Footer.vue";
import http from "../utils/http.js";

/*
// 测试CORS的跨域配置是否有问题
import axios from "axios"
const http = axios.create()

// 测试服务端的跨域是否配置成功
http.get("http://api.luffycity.cn:8000/home/test").then(response=>{
  console.log(response.data);
})
*/

http.get("/home/test").then(response => {
  console.log(response.data);
})


</script>

<template>
  <div class="home">
    <Header></Header>
    <Footer></Footer>
  </div>
</template>

<style scoped>

</style>