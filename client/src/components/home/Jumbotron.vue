<template>
    <div>
        <div class="main-image">
        <div class="title-div">
            <h1 class="center">My Library</h1>
            <hr />
            <h3 class="center">A Vast Collection of Stories and Knowledge</h3>
        </div>
        </div>
    </div>
</template>

<script>
</script>

<style scoped>

.main-image {
  margin: 28px 0 28px 0;
  height: 80vh;
  background: url("../../assets/images/books.jpg") center/contain no-repeat;
  background-position: center center;
  background-size: 70%; /* Slightly increases the width */
  display: flex;
  justify-content: center;
  align-items: center;
}

.title-div {
  background-color: rgba(0, 0, 0, 0.6);
  border-radius: 15px;
  color: white;
  padding: 20px;
}

.center {
  text-align: center;
}

</style>