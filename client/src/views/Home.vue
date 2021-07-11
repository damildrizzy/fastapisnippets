<template>
  <div class="px-6 py-8 bg-gray-100">
    <div class="container flex justify-between mx-auto">
      <div class="w-full lg:w-8/12">
        <SnippetList />
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import SnippetList from "@/components/SnippetList.vue";

export default {
  name: "Home",
  components: {
    SnippetList,
  },
};
</script>
